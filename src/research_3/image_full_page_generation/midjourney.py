import sys
import time
import requests
import json

sys.path.append('../shared')
sys.path.append('./')
from __utils import generate_from_text
from common import save_image_from_url
from constants import RESULTS_DIRECTORY_NAME, MAX_IMAGE_GENERATE_RETRIES
from credentials import IMAGINEAPI_API_KEY

def check_progress(message_id):
  try:
    url = f"https://cl.imagineapi.dev/items/images/{message_id}"

    headers = {
      'Content-Type': 'application/json',
      'Authorization': f"Bearer {IMAGINEAPI_API_KEY}",
    }
    response = requests.request("GET", url, headers=headers)
    data_response = json.loads(response.text)
    print(data_response)

    if data_response['data']['status'] == "completed":
      return data_response['data']['upscaled_urls'][0]
    elif data_response['data']['status'] == "pending" or data_response['data']['status'] == "in-progress":
      time.sleep(10)
      return check_progress(message_id)
    elif data_response['data']['status'] == "failed":
      return 'failed'
    else:
      print(f"@check_progress error occured {response.text}")
      time.sleep(10)
      return check_progress(message_id)
  except Exception as e:
    print(f"An error occurred while generating image: {e}")
    time.sleep(10)
    return check_progress(message_id)

def generate_image(prompt, retry = 1):
  try:
    print(f"Attempt #{retry}")
    if retry >= MAX_IMAGE_GENERATE_RETRIES:
      return

    url = "http://cl.imagineapi.dev/items/images/"

    payload = json.dumps({
      "prompt": prompt
    })

    headers = {
      'Content-Type': 'application/json',
      'Authorization': f"Bearer {IMAGINEAPI_API_KEY}",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data_response = json.loads(response.text)
    print(data_response)

    if data_response['data']['id']:
      message_id = data_response['data']['id']
      time.sleep(20)
      url = check_progress(message_id)
      if url == "failed":
        return None
      print(f"response text converted image url {url}")
      return url
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
    generate_from_text(RESULTS_DIRECTORY_NAME, "midjourney", generate_image, save_image_from_url)
  except Exception as error:
    print(f'Error running script: {error}')
