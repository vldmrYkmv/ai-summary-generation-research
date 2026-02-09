from openai import OpenAI
import sys

from ..shared.constants import RESULTS_DIRECTORY_NAME_STUDY_3
from ..shared.credentials import OPEN_AI_KEY
from .__utils import run_algorithm

client = OpenAI(api_key=OPEN_AI_KEY)

def run_summarization(data, prompt):
  response = client.chat.completions.create(
    model="gpt-4.5-preview",
    messages=[
      {"role": "system", "content": prompt},
      {"role": "user", "content": data},
    ]
  )

  print(response)
  return response.choices[0].message.content

if __name__ == '__main__':
  try:
    run_algorithm(run_summarization, "gpt4", RESULTS_DIRECTORY_NAME_STUDY_3, False)
  except Exception as error:
    print(f'Error running script: {error}')
