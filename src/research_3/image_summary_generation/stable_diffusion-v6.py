import sys
import time
import requests
import json

from ...shared.constants import MAX_IMAGE_GENERATE_RETRIES
from ...shared.credentials  import STABLE_DIFFUSION_API_KEY
from ...shared.common import save_image_from_url, parse_dir_args
from .__utils import run_algorithm

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

def generate_image(prompt, retry = 1):
  try:
    print(f"Attempt #{retry}")
    if retry >= MAX_IMAGE_GENERATE_RETRIES:
      return
    
    url = "https://modelslab.com/api/v6/realtime/text2img"

    payload = json.dumps({
      "key": STABLE_DIFFUSION_API_KEY,
      "prompt": prompt,
      "negative_prompt": None,
      "width": "1024",
      "height": "1024",
      "samples": "1",
      # "num_inference_steps": "20",
      "seed": None,
      # "guidance_scale": 7.5,
      "safety_checker": False,
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
      error_object = json.loads(response.text)
      if "Your subscription is cancelled" in error_object['message']:
        raise ValueError("Subscription is not active")
      retry = retry + 1
      time.sleep(10)
      return generate_image(prompt, retry)
  except Exception as e:
    if str(e) == "Subscription is not active":
      raise e
    print(f"An error occurred while generating image: {e}")
    retry = retry + 1
    time.sleep(10)
    return generate_image(prompt, retry)

if __name__ == '__main__':
  try:
    args = parse_dir_args()
    run_algorithm(generate_image, "stable-diffusion-6", save_image_from_url, args.results_dir)
  except Exception as error:
    print(f'Error running script: {error}')
