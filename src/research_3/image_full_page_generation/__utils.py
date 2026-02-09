import os
import sys
import time

from ...shared.constants import SKIP_EXISTED_IMAGE_FILES
from ...shared.common import get_files_list, read_file

def generate_from_text(results_dir, algorithm_name, generate_image_fn, save_image_fn):
  start_time = time.time()
  print('Starting script...')
  files_list = get_files_list(results_dir, False)
  print(f'Found {len(files_list)} directories in "{results_dir}" directory...')

  for index, directory_name in enumerate(files_list):
    print(f'[{index + 1}/{len(files_list)}] Starting sequence for "{directory_name}" book...')
    pages_list = get_files_list(f"{results_dir}/{directory_name}")
    print(f'Found {len(pages_list)} pages directories...')

    for page_index, page_directory_name in enumerate(pages_list):
      print(f"Page directory: {page_directory_name}")
      text_dir_name = f"{results_dir}/{directory_name}/{page_directory_name}"
      text_files_list = get_files_list(text_dir_name)

      for text_index, text_file in enumerate(text_files_list):
        if ".txt" in text_file:
          # Uncomment to run for specific algorithm only
          # if checkAlorithmToContinue(alg_file):
          #   continue
          new_image_name = text_file.replace('.txt', f"-{algorithm_name}.png")
          if not os.path.exists(f"{results_dir}/{directory_name}/{page_directory_name}/text_results"):
            os.makedirs(f"{results_dir}/{directory_name}/{page_directory_name}/text_results")

          new_image_full_path = f"{results_dir}/{directory_name}/{page_directory_name}/text_results/{new_image_name}"

          if SKIP_EXISTED_IMAGE_FILES and os.path.exists(new_image_full_path):
            print(f"File '{new_image_full_path}' already exists")
          else:
            text_directory = f"{results_dir}/{directory_name}/{page_directory_name}"
            file_data = read_file(text_directory, text_file)

            if file_data != '':
              image_url = generate_image_fn(file_data)
              if image_url is not None:
                save_image_fn(image_url, new_image_full_path)
            else:
              print(f"Prompt is empty {file_data}")
  end_time = time.time()
  print("Execution time:", end_time - start_time)
