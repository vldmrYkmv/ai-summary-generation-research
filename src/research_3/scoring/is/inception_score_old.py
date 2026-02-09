import sys
import time
import numpy as np
import keras
from PIL import Image
import tensorflow as tf

sys.path.append('../../shared')
from constants import RESULTS_DIRECTORY_NAME
from common import get_files_list

# Just disables the warning, doesn't take advantage of AVX/FMA to run faster
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from math import floor
from numpy import ones
from numpy import expand_dims
from numpy import log
from numpy import mean
from numpy import std
from numpy import exp
from numpy.random import shuffle
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input

from keras.datasets import cifar10
from skimage.transform import resize
from numpy import asarray

# Enable eager execution to get more detailed error messages
# tf.config.run_functions_eagerly(True)

# scale an array of images to a new size
def scale_images(images, new_shape):
	images_list = list()
	for image in images:
		# resize with nearest neighbor interpolation
		new_image = resize(image, new_shape, 0)
		# store
		images_list.append(new_image)
	return asarray(images_list)

# assumes images have any shape and pixels in [0,255]
def calculate_inception_score(images, n_split=10, eps=1E-16):
  print('calculate_inception_score start')
  # load inception v3 model
  model = InceptionV3(include_top=True, weights='imagenet', pooling='avg')
  # enumerate splits of images/predictions
  scores = list()
  n_part = floor(images.shape[0] / n_split)
  print(n_part)
  for i in range(n_split):
    # retrieve images
    print(i)
    ix_start, ix_end = i * n_part, (i+1) * n_part
    subset = images[ix_start:ix_end]
    # convert from uint8 to float32
    subset = subset.astype('float32')
    # scale images to the required size
    subset = scale_images(subset, (299,299,3))
    # pre-process images, scale to [-1,1]
    subset = preprocess_input(subset)
    # predict p(y|x)
    p_yx = model.predict(subset)
    # calculate p(y)
    p_y = expand_dims(p_yx.mean(axis=0), 0)
    # calculate KL divergence using log probabilities
    kl_d = p_yx * (log(p_yx + eps) - log(p_y + eps))
    # sum over classes
    sum_kl_d = kl_d.sum(axis=1)
    # average over images
    avg_kl_d = mean(sum_kl_d)
    # undo the log
    is_score = exp(avg_kl_d)
    # store
    scores.append(is_score)
  # average across images
  is_avg, is_std = mean(scores), std(scores)
  print('Inception Score:', is_avg, '±', is_std)
  return is_avg, is_std

if __name__ == '__main__':
  try:
    start_time = time.time()
    # images_dir_path = "../../../ai-article-study/results2"
    images_dir_path = f"../{RESULTS_DIRECTORY_NAME}"
    print(f'Image path {images_dir_path}')
    files_list = get_files_list(images_dir_path, False)
    print(f'Found {len(files_list)} directories in "{images_dir_path}" directory...')
    for index, directory_name in enumerate([files_list[0]]):
      print(f'[{index + 1}/{len(files_list)}] Starting sequence for "{directory_name}" book...')
      pages_list = get_files_list(f"{images_dir_path}/{directory_name}")
      print(f'Found {len(pages_list)} pages directories...')
      images = []
      for page_index, page_directory_name in enumerate(pages_list):
        image_data_list = get_files_list(f"{images_dir_path}/{directory_name}/{page_directory_name}")
        for file_index, data_file_name in enumerate(image_data_list):
          # print(f'data_file_name {data_file_name}')
          if ".png" in data_file_name:
            img_path = f"{images_dir_path}/{directory_name}/{page_directory_name}/{data_file_name}"
            img = Image.open(img_path).convert('RGB')
            img = img.resize((32,32))
            images.append(np.array(img))
            # images.append(f"{images_dir_path}/{directory_name}/{page_directory_name}/{data_file_name}")
        # print(images)
    np_images = np.array(images)
    # print(np_images)
    shuffle(images)
    results = calculate_inception_score(np_images)
    print(results)
    print('\tFinished sequence for file')
    end_time = time.time()
    print("Execution time:", end_time - start_time)
  except Exception as error:
    print(f'Error running script: ', error)
