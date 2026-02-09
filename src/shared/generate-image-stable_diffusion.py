import sys
import os
import time
import requests
import json

from ..shared.constants import SKIP_EXISTED_IMAGE_FILES, MAX_IMAGE_GENERATE_RETRIES
from ..shared.credentials  import STABLE_DIFFUSION_API_KEY
from ..shared.common import save_image_from_url, get_files_list, parse_dir_args

def check_progress(url):
  print(f"check_progress {url}")
  headers = {
    'Content-Type': 'application/json'
  }
  payload = json.dumps({
    "key": STABLE_DIFFUSION_API_KEY,
  })
  response = requests.request("POST", url, headers=headers, data=payload)
  data_response = json.loads(response.text)
  print(data_response)
  if data_response['status'] == "processing":
    time.sleep(10)
    return check_progress(url)
  elif data_response['status'] == "success":
    return data_response['output'][0]
  else:
    print(f"error occured {response.text}")
    return

def generate_image(prompt, retry = 1):
  try:
    if not retry == 1:
      print(f"try #{retry}")
    if retry >= MAX_IMAGE_GENERATE_RETRIES:
      return
    
    url = "https://stablediffusionapi.com/api/v3/text2img"

    payload = json.dumps({
      "key": STABLE_DIFFUSION_API_KEY,
      "prompt": prompt,
      "negative_prompt": None,
      "width": "1024",
      "height": "1024",
      "samples": "1",
      "num_inference_steps": "20",
      "seed": None,
      "guidance_scale": 7.5,
      "safety_checker": "yes",
      "multi_lingual": "no",
      "panorama": "no",
      "self_attention": "no",
      "upscale": "no",
      "embeddings_model": None,
      "webhook": None,
      "track_id": None
    })

    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data_response = json.loads(response.text)

    if data_response['status'] == "processing":
      return check_progress(data_response['fetch_result'])
    elif data_response['status'] == "success":
      print(f"response text converted{data_response['output']}")
      return data_response['output'][0]
    else:
      print(f"error occured {response.text}")
      retry = retry + 1
      time.sleep(10)
      return generate_image(prompt, retry)
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
            # print(f"\talg_file {alg_file}")
            # Uncomment to run for specific algorithm only
            # if checkAlorithmToContinue(alg_file):
            #   continue
            image_name = alg_file.replace('.json', '-stable-diffusion.png')
            image_full_path = f"{results_dir}/{directory_name}/{page_directory_name}/{image_name}"
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
                  time.sleep(20)
                  if image_url is not None:
                    save_image_from_url(image_url, image_full_path)
                else:
                  print(f"Prompt is empty {string_prompt}")
    print('\tFinished sequence for file')
    end_time = time.time()
    print("Execution time:", end_time - start_time)
  except Exception as error:
    print(f'Error running script: ', error)
