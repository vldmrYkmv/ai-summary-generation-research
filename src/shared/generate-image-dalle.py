from openai import OpenAI
import sys
import os
import time
import json

from ..shared.constants import SKIP_EXISTED_IMAGE_FILES, MAX_IMAGE_GENERATE_RETRIES
from ..shared.credentials  import OPEN_AI_KEY
from ..shared.common import save_image_from_url, get_files_list, parse_dir_args

client = OpenAI(api_key=OPEN_AI_KEY)

def generate_image(prompt, retry = 1):
  try:
    print(f"retry {retry}")
    if retry >= MAX_IMAGE_GENERATE_RETRIES:
      return
    response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1024x1024",
      quality="standard",
      n=1,
    )

    print(response)
    image_url = response.data[0].url
    return image_url
  except Exception as e:
    print(f"An error occurred while generating image: {e}")
    retry = retry + 1
    time.sleep(10)
    return generate_image(prompt, retry)

if __name__ == '__main__':
  try:
    args = parse_dir_args()
    results_dir = args.results_dir
    start_time = time.time()
    print('Starting script...')
    # image_full_path = f"{RESULTS_DIRECTORY_NAME_STUDY_2}/H. G. Wells - The Time Machine/random-page-3/alg-claude3-result-dalle.png"
    # image_url = generate_image("This passage describes a scene where the Time Traveller, after recounting his journey through time, is questioned by his skeptical friends. He shows them the Time Machine to prove his story, but remains uncertain about his own experiences. The next day, a narrator visits the Time Traveller again, finding him preparing for another journey and insisting on the truth of his time travel claims.")
    # if image_url is not None:
    #   save_image_from_url(image_url, image_full_path)

    files_list = get_files_list(results_dir, False)
    print(f'Found {len(files_list)} directories in "{results_dir}" directory...')
    # for index, directory_name in enumerate(files_list):
    for index, directory_name in enumerate(files_list):
      print(f'[{index + 1}/{len(files_list)}] Starting sequence for "{directory_name}" book...')
      pages_list = get_files_list(f"{results_dir}/{directory_name}")
      print(f'Found {len(pages_list)} pages directories...')
      for page_index, page_directory_name in enumerate(pages_list):
        print(f"page_directory_name {page_directory_name}")
        alg_dir_name = f"{results_dir}/{directory_name}/{page_directory_name}"
        alg_files_list = get_files_list(alg_dir_name)
        for alg_index, alg_file in enumerate(alg_files_list):
          if "alg-" in alg_file and ".json" in alg_file:
            # Uncomment to run for specific algorithm only
            # if checkAlorithmToContinue(alg_file):
            #   continue
            image_name = alg_file.replace('.json', '-dalle.png')
            image_full_path = f"{results_dir}/{directory_name}/{page_directory_name}/{image_name}"
            print(image_full_path)
            if SKIP_EXISTED_IMAGE_FILES and os.path.exists(image_full_path):
              print(f"File '{image_full_path}' already exists")
            else:
              alg_full_path = f"{results_dir}/{directory_name}/{page_directory_name}/{alg_file}"
              with open(alg_full_path, 'r') as file:
                data = json.load(file)
                if isinstance(data, str):
                  string_prompt = data
                else:
                  string_prompt = ' '.join(data)
                print(f"\tprompt for '{alg_file}': `{string_prompt}`")
                if string_prompt != '':
                  image_url = generate_image(string_prompt)
                  if image_url is not None:
                    save_image_from_url(image_url, image_full_path)
                else:
                  print(f"Prompt is empty {string_prompt}")
    print('\tFinished sequence for file')
    end_time = time.time()
    print("Execution time:", end_time - start_time)
  except Exception as error:
    print(f'Error running script: ', error)
