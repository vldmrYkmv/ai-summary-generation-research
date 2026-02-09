import numpy
import time
import sys
import os
from numpy import cov
from numpy import trace
from numpy import iscomplexobj
from numpy import asarray
from numpy.random import shuffle
from scipy.linalg import sqrtm
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
from keras.datasets.mnist import load_data
from skimage.transform import resize
from keras.datasets import cifar10


sys.path.append('../../shared')
from constants import RESULTS_DIRECTORY_NAME
from common import get_files_list, is_prompt_directory, save_text_to_file
 
# scale an array of images to a new size
def scale_images(images, new_shape):
	images_list = list()
	for image in images:
		# resize with nearest neighbor interpolation
		new_image = resize(image, new_shape, 0)
		# store
		images_list.append(new_image)
	return asarray(images_list)
 
# calculate frechet inception distance
def calculate_fid(model, images1, images2):
	# calculate activations
	act1 = model.predict(images1)
	act2 = model.predict(images2)
	# calculate mean and covariance statistics
	mu1, sigma1 = act1.mean(axis=0), cov(act1, rowvar=False)
	mu2, sigma2 = act2.mean(axis=0), cov(act2, rowvar=False)
	# calculate sum squared difference between means
	ssdiff = numpy.sum((mu1 - mu2)**2.0)
	# calculate sqrt of product between cov
	covmean = sqrtm(sigma1.dot(sigma2))
	# check and correct imaginary numbers from sqrt
	if iscomplexobj(covmean):
		covmean = covmean.real
	# calculate score
	fid = ssdiff + trace(sigma1 + sigma2 - 2.0 * covmean)
	return fid
 
# # prepare the inception v3 model
# model = InceptionV3(include_top=False, pooling='avg', input_shape=(299,299,3))
# # load cifar10 images
# (images1, _), (images2, _) = cifar10.load_data()
# shuffle(images1)
# images1 = images1[:10000]
# print('Loaded', images1.shape, images2.shape)
# # convert integer to floating point values
# images1 = images1.astype('float32')
# images2 = images2.astype('float32')
# # resize images
# images1 = scale_images(images1, (299,299,3))
# images2 = scale_images(images2, (299,299,3))
# print('Scaled', images1.shape, images2.shape)
# # pre-process images
# images1 = preprocess_input(images1)
# images2 = preprocess_input(images2)
# # calculate fid
# fid = calculate_fid(model, images1, images2)
# print('FID: %.3f' % fid)
def calculate_fid_score():
  print('FID: %.3f' % fid)

if __name__ == '__main__':
  try:
    start_time = time.time()
    results_score = {}
    images_dir_path = RESULTS_DIRECTORY_NAME
    print(f'Image path {images_dir_path}')
    files_list = get_files_list(images_dir_path, False)
    print(f'Found {len(files_list)} directories in "{images_dir_path}" directory...')
    for index, directory_name in enumerate([files_list[0]]):
      print(f'[{index + 1}/{len(files_list)}] Starting sequence for "{directory_name}" book...')
      if not os.path.isdir(f"{images_dir_path}/{directory_name}"):
        continue

      pages_list = get_files_list(f"{images_dir_path}/{directory_name}")
      print(f'Found {len(pages_list)} pages directories...')
      images = list()
      for page_index, page_directory_name in enumerate([pages_list[0]]):
        print(f"Page directory: {page_directory_name}")
        text_dir_name = f"{images_dir_path}/{directory_name}/{page_directory_name}"
        text_files_list = get_files_list(text_dir_name)
        print(text_files_list)

        prompt_directories_list = list(filter(is_prompt_directory, text_files_list))
        print(prompt_directories_list)
        results_score[f'{directory_name}'][f'{page_directory_name}'] = {}

        # image_data_list = get_files_list(f"{images_dir_path}/{directory_name}/{page_directory_name}")
        # for file_index, data_file_name in enumerate([image_data_list[0], image_data_list[1]]):
        #     print(f'data_file_name {data_file_name}')
        #     if ".png" in data_file_name:
        #         images.append(f"{images_dir_path}/{directory_name}/{page_directory_name}/{data_file_name}")
        print(images)
    calculate_fid_score(images)
    print('\tFinished sequence for file')
    end_time = time.time()
    print("Execution time:", end_time - start_time)
  except Exception as error:
    print(f'Error running script: ', error)