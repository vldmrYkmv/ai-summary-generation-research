import sys
import os
import json
import time

sys.path.append('../')
from ..shared.constants import RESULTS_DIRECTORY_NAME_STUDY_2, SKIP_EXISTED_FILES, PROMPTS_LIST
from ..shared.common import get_files_list, read_file, save_text_to_file

def run_algorithm(algorithm_function, algorithm_name, files_path=RESULTS_DIRECTORY_NAME_STUDY_2, is_top_list=True):
  start_time = time.time()

  files_list = get_files_list(files_path, is_top_list)
  print(f'Found {len(files_list)} directories in "{files_path}" directory...')
  for index, directory_name in enumerate(files_list):
    print(f'[{index + 1}/{len(files_list)}] Starting sequence for "{directory_name}" book...')
    pages_list = get_files_list(f"{files_path}/{directory_name}")
    print(f'Found {len(pages_list)} pages directories...')
    for page_index, page_directory_name in enumerate(pages_list):
      for prompt_index, prompt_text in enumerate(PROMPTS_LIST):
        if not os.path.exists(f"{files_path}/{directory_name}/{page_directory_name}/prompt-{prompt_index + 1}"):
          os.makedirs(f"{files_path}/{directory_name}/{page_directory_name}/prompt-{prompt_index + 1}")
        save_file_name = f"{files_path}/{directory_name}/{page_directory_name}/prompt-{prompt_index + 1}/{algorithm_name}.json"
        if SKIP_EXISTED_FILES and os.path.exists(save_file_name):
          print(f"Found file '{save_file_name}', Skip checking")
          continue
        else:
          print(f"File '{save_file_name}' doesn't exist or should be overwritten")
        print(f'[{page_index + 1}/{len(pages_list)}] Starting sequence for "{page_directory_name}" page...')
        page_directory_path = f"{files_path}/{directory_name}/{page_directory_name}"
        data = read_file(page_directory_path, f"{directory_name}.txt")
        time.sleep(5)
        result = algorithm_function(data, prompt_text)
        print(f"saving {result} to file {save_file_name} {prompt_index}")
        save_text_to_file(json.dumps(result, ensure_ascii=False), save_file_name)
  end_time = time.time()
  print("Execution time:", end_time - start_time)
