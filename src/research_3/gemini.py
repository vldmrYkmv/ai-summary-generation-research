import sys
from google import genai

from ..shared.constants import RESULTS_DIRECTORY_NAME_STUDY_3
from ..shared.credentials import GEMINI_API_KEY
from .__utils import run_algorithm

client = genai.Client(
  api_key=GEMINI_API_KEY
)

def run_summarization(data, prompt):
  response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[{
      "parts": [{ "text": prompt }, { "text": data }]
    }]
  )

  print(response.text)
  return response.text

if __name__ == '__main__':
  try:
    run_algorithm(run_summarization, "gemini", RESULTS_DIRECTORY_NAME_STUDY_3, False)
  except Exception as error:
    print(f'Error running script: {error}')
