import sys
import os
import json
import time

from ...shared.constants import RESULTS_DIRECTORY_NAME_STUDY_3, SKIP_EXISTED_IMAGE_FILES
from ...shared.common import get_files_list, is_prompt_directory, is_json_summary_directory

def run_algorithm(algorithm_function, algorithm_name, save_image_fn, files_path=RESULTS_DIRECTORY_NAME_STUDY_3):
  start_time = time.time()
  book_file_list = get_files_list(files_path, False)
  print(f'Found {len(book_file_list)} book directories in "{files_path}" directory')
  # for index, directory_name in enumerate(files_list):
  for book_directory_index, book_directory_name in enumerate(book_file_list):
    print(f'[{book_directory_index + 1}/{len(book_file_list)}] Starting sequence for "{book_directory_name}" book...')
    book_pages_list = get_files_list(f"{files_path}/{book_directory_name}")
    print(f'Found {len(book_pages_list)} pages directories...')
    for page_index, page_directory_name in enumerate(book_pages_list):
      page_directory_path = f"{files_path}/{book_directory_name}/{page_directory_name}"
      page_directory_files_list = get_files_list(page_directory_path)
      print(page_directory_files_list)
      prompt_directories_list = list(filter(is_prompt_directory, page_directory_files_list))
      print(prompt_directories_list)
      for prompt_directory_index, prompt_directory_name in enumerate(prompt_directories_list):
        text_summaries_directory_path = f"{files_path}/{book_directory_name}/{page_directory_name}/{prompt_directory_name}"
        summaries_list = get_files_list(text_summaries_directory_path)
        prompt_files_list = list(filter(is_json_summary_directory, summaries_list))
        print(prompt_files_list)
        for summary_algorithm_index, summary_algorithm_name in enumerate(prompt_files_list):
          # Uncomment to run for specific algorithm only
          # if checkAlorithmToContinue(alg_file):
          #   continue
          image_name = summary_algorithm_name.replace('.json', f"-{algorithm_name}.png")
          image_full_path = f"{text_summaries_directory_path}/{image_name}"
          print(image_full_path)
          if SKIP_EXISTED_IMAGE_FILES and os.path.exists(image_full_path):
            print(f"File '{image_full_path}' already exists")
          else:
            summary_full_path = f"{text_summaries_directory_path}/{summary_algorithm_name}"
            with open(summary_full_path, 'r') as file:
              data = json.load(file)
              if isinstance(data, str):
                string_prompt = data
              else:
                string_prompt = ' '.join(data)
              print(f"\tprompt for '{summary_algorithm_name}': `{string_prompt}`")
              if string_prompt != '':
                image_url = algorithm_function(string_prompt)
                if image_url is not None:
                  save_image_fn(image_url, image_full_path)
              else:
                print(f"Prompt is empty {string_prompt}")
  end_time = time.time()
  print("Execution time:", end_time - start_time)