import sys
import time
import numpy as np
import keras
import json
from PIL import Image
import tensorflow as tf

sys.path.append('../../shared')
from constants import RESULTS_DIRECTORY_NAME
from common import get_files_list, is_prompt_directory, is_png_file, save_text_to_file

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
  # print('calculate_inception_score start')
  # load inception v3 model
  model = InceptionV3(include_top=True, weights='imagenet', pooling='avg')
  # print('calculate_inception_score 1')
  # enumerate splits of images/predictions
  scores = list()
  n_part = floor(images.shape[0] / n_split)
  print('calculate_inception_score 2', n_part, n_split, images.shape[0])
  # print(n_part)
  for i in range(n_split):
    # retrieve images
    # print(i)
    # print('calculate_inception_score 2.1')
    ix_start, ix_end = i * n_part, (i+1) * n_part
    # print('calculate_inception_score 2.1 test', ix_start, ix_end, n_part, i)
    subset = images[ix_start:ix_end]
    # print('calculate_inception_score 2.2', subset)
    # convert from uint8 to float32
    subset = subset.astype('float32')
    # print('calculate_inception_score 2.3', subset)
    # scale images to the required size
    # print('calculate_inception_score 3')
    subset = scale_images(subset, (299,299,3))
    # print('calculate_inception_score 3.1', subset)
    # pre-process images, scale to [-1,1]
    subset = preprocess_input(subset)
    # print('calculate_inception_score 3.2', subset)
    # predict p(y|x)
    p_yx = model.predict(subset)
    # print('calculate_inception_score 3.3')
    # calculate p(y)
    # print('calculate_inception_score 4')
    p_y = expand_dims(p_yx.mean(axis=0), 0)
    # calculate KL divergence using log probabilities
    # print('calculate_inception_score 5')
    kl_d = p_yx * (log(p_yx + eps) - log(p_y + eps))
    # sum over classes
    sum_kl_d = kl_d.sum(axis=1)
    # print('calculate_inception_score 6')
    # average over images
    avg_kl_d = mean(sum_kl_d)
    # print('calculate_inception_score 7')
    # undo the log
    is_score = exp(avg_kl_d)
    # print('calculate_inception_score 8')
    # store
    scores.append(is_score)
    # print('calculate_inception_score 9')
  # average across images
  is_avg, is_std = mean(scores), std(scores)
  # print('Inception Score:', is_avg, '±', is_std)
  return is_avg, is_std

if __name__ == '__main__':
  try:
    start_time = time.time()
    results_score = {}
    algorithms_types = ['claude3', 'gemini', 'gpt4']
    image_generator_service = ['dalle', 'stable-diffusion-6', 'midjourney']
    result_directory = f"../{RESULTS_DIRECTORY_NAME}"
    files_list = get_files_list(result_directory, False)
    print(f'Found {len(files_list)} directories in "{result_directory}" directory...')
    images = []

    for index, directory_name in enumerate(files_list):
      print(f'[{index + 1}/{len(files_list)}] Starting sequence for "{directory_name}" book...')
      if not os.path.isdir(f"{result_directory}/{directory_name}"):
        continue
      pages_list = get_files_list(f"{result_directory}/{directory_name}")
      print(f'Found {len(pages_list)} pages directories...')

      results_score[f'{directory_name}'] = {}
      for page_index, page_directory_name in enumerate(pages_list):
        print(f"Page directory: {page_directory_name}")
        text_dir_name = f"{result_directory}/{directory_name}/{page_directory_name}"
        text_files_list = get_files_list(text_dir_name)
        print(text_files_list)

        prompt_directories_list = list(filter(is_prompt_directory, text_files_list))
        print(prompt_directories_list)
        results_score[f'{directory_name}'][f'{page_directory_name}'] = {}
        for image_generator in image_generator_service:
          np_images = []
          images = []
          for algorithm in algorithms_types:
            for prompt_directory_index, prompt_directory_name in enumerate(prompt_directories_list):
              img_path = f"{result_directory}/{directory_name}/{page_directory_name}/{prompt_directory_name}/{algorithm}-{image_generator}.png"
              if not os.path.exists(img_path):
                print(f"should skip: {img_path}")
                continue
              img = Image.open(img_path).convert('RGB')
              img = img.resize((32,32))
              images.append(np.array(img))

          print(len(images))
          if len(images) > 5:
            np_images = np.array(images)
            shuffle(np_images)
            score = calculate_inception_score(np_images, 5)
            results_score[f'{directory_name}'][f'{page_directory_name}'][f'{image_generator}'] = [float(score[0]), float(score[1])]
          else:
             results_score[f'{directory_name}'][f'{page_directory_name}'][f'{image_generator}'] = [0, 0]

    # print(results_score)
    save_text_to_file(json.dumps(results_score, ensure_ascii=False), f"../{RESULTS_DIRECTORY_NAME}/inception_score_i_g.json")
    end_time = time.time()
    print("Execution time:", end_time - start_time)
  except Exception as error:
    print(f'Error running script: {error}')
