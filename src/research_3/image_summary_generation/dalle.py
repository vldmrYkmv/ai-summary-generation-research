from openai import OpenAI
import argparse
import sys
import time

from ...shared.constants import MAX_IMAGE_GENERATE_RETRIES
from ...shared.credentials  import OPEN_AI_KEY
from ...shared.common import save_image_from_url, parse_dir_args
from .__utils import run_algorithm

client = OpenAI(api_key=OPEN_AI_KEY)

def parse_args():
    parser = argparse.ArgumentParser(description="Run DALL·E image generation")
    parser.add_argument(
        "--dir",
        dest="results_dir",
        default="./results",
        help="Directory to save generated images"
    )
    return parser.parse_args()

def generate_image(prompt, retry = 1):
  try:
    print(f"Attempt #{retry}")
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
    if e.body['code'] == "billing_hard_limit_reached":
      raise e
    retry = retry + 1
    time.sleep(10)
    return generate_image(prompt, retry)

if __name__ == '__main__':
  try:
    args = parse_dir_args()
    run_algorithm(generate_image, "dalle", save_image_from_url, args.results_dir)
  except Exception as error:
    print(f'Error running script: {error}')
