from openai import OpenAI
import sys

from ..shared.common import run_algorithm_in_results
from ..shared.constants import RESULTS_DIRECTORY_NAME_STUDY_2
from ..shared.credentials import OPEN_AI_KEY

client = OpenAI(api_key=OPEN_AI_KEY)

def run_summarization(data):
  response = client.chat.completions.create(
    model="gpt-4o-2024-05-13",
    messages=[
      {"role": "system", "content": "You will be provided with a block of text, and your task is to return summarization (not big) that describes provided text."},
      {"role": "user", "content": data},
    ]
  )

  print(response)
  return response.choices[0].message.content

if __name__ == '__main__':
  try:
    print('Starting script "gpt-4-sum" ...')
    run_algorithm_in_results(run_summarization, "gpt-4-sum", RESULTS_DIRECTORY_NAME_STUDY_2, False)
    print('\tFinished script')
  except Exception as error:
    print(f'Error running script: ', error)
