from openai import OpenAI
from ..shared.constants import *
from ..shared.credentials  import OPEN_AI_KEY
from ..shared.common import run_algorithm_in_results

client = OpenAI(api_key=OPEN_AI_KEY)

def run_summarization(data):
  # gpt-4-1106-preview, gpt-4, gpt-4 turbo, gpt-3.5-turbo
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You will be provided with a block of text, and your task is to return list of keywords (maximum 10 keywords) for provided text."},
      {"role": "user", "content": data},
    ]
  )

  # print(response)
  lines = response.choices[0].message.content.split('\n')
  result = [item.split(' ')[1] for item in lines]
  print(result)
  return result

if __name__ == '__main__':
  try:
    print('Starting script...')
    run_algorithm_in_results(run_summarization, "openapi-keywords-gpt-3")
    print('\tFinished sequence for file')
  except Exception as error:
    print(f'Error running script: ', error)
