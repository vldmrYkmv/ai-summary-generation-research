import anthropic
import sys

from ..shared.common import run_algorithm_in_results
from ..shared.constants import RESULTS_DIRECTORY_NAME_STUDY_2
from ..shared.credentials import CLAUDE_API_KEY

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def run_summarization(data):
  message = client.messages.create(
      model="claude-3-5-sonnet-20240620",
      max_tokens=1000,
      temperature=0,
      system="You will be provided with a block of text, and your task is to return summarization (1-2 sentences) that describes provided text",
      messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": data
                }
            ]
        }
      ]
  )
  print(message.content[0].text)
  return message.content[0].text

if __name__ == '__main__':
  try:
    print('Starting script...')
    run_algorithm_in_results(run_summarization, "claude3", RESULTS_DIRECTORY_NAME_STUDY_2, False)
    print('\tFinished sequence for file')
  except Exception as error:
    print(f'Error running script: ', error)
