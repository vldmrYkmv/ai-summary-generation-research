import sys
import time
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

from ...shared.constants import MAX_IMAGE_GENERATE_RETRIES
from ...shared.credentials  import GEMINI_API_KEY
from ...shared.common import save_image_from_data, parse_dir_args
from .__utils import generate_from_text

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_image(prompt, retry = 1):
  try:
    print(f"Attempt #{retry}")
    if retry >= MAX_IMAGE_GENERATE_RETRIES:
      return

    response = client.models.generate_images(
      model='imagen-3.0-generate-002',
      prompt=prompt,
      config=types.GenerateImagesConfig(
        number_of_images= 1,
      )
    )

    print(response)
    return response.generated_images
  except Exception as e:
    print(f"An error occurred while generating image: {e}")
    if e.details['error']['message'] == 'Imagen API is only accessible to billed users at this time.':
      raise ValueError("Can't proceed with unpaid account")
    retry = retry + 1
    time.sleep(10)
    return generate_image(prompt, retry)

if __name__ == '__main__':
  try:
    args = parse_dir_args()
    generate_from_text(args.results_dir, "gemini", generate_image, save_image_from_data)
  except Exception as error:
    print(f'Error running script: {error}')
