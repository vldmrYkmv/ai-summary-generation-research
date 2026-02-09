# _*_ encoding=utf8 _*_
__author__ = "Volodymyr"

import os
import sys
import random

from ..shared.constants import *
from ..shared.common import *

if __name__ == '__main__':
  try:
    print('Starting script...')
    files_list = get_files_list(BOOKS_DIRECTORY_NAME)
    print(f'Found {len(files_list)} files...')

    if not os.path.exists(RESULTS_DIRECTORY_NAME_STUDY):
      os.makedirs(RESULTS_DIRECTORY_NAME_STUDY)

    for index, file_name in enumerate(files_list):
      print(f'[{index + 1}/{len(files_list)}] Starting sequence for "{file_name}" file...')
      data = read_file(BOOKS_DIRECTORY_NAME, file_name)
      splitted_data_array = data.split('\n\n')

      print(f'\tRead file "{file_name}" length {len(data)} splitted {len(splitted_data_array)}')

      book_directory = file_name.replace('.txt', '')

      used_indexes = []
      if len(splitted_data_array) > 1:
        for i in range(NUMBER_OF_RANDOM_PAGES):
          index = i + 1
          print(f'[{index}/{NUMBER_OF_RANDOM_PAGES}] Getting random page')
          random_page_result = get_random_page(splitted_data_array, used_indexes)
          used_indexes.append(random_page_result["index"])

          save_file_name = f"{RESULTS_DIRECTORY_NAME_STUDY}/{book_directory}/random-page-{i+1}/{file_name}"

          if SKIP_EXISTED_FILES and os.path.exists(save_file_name):
            print(f"Found file '{save_file_name}', Skip checking")
            continue
          else:
            print(f"Saving file {save_file_name}")
            save_text_to_file(random_page_result["text"], save_file_name)
      else:
        raise Exception('\tCouldn\'t split text into paragraphs')

      print('\tFinished sequence for file')
  except Exception as error:
    print(f'Error running script: ', error)
