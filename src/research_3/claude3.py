import anthropic
import sys

from ..shared.constants import RESULTS_DIRECTORY_NAME_STUDY_3
from ..shared.credentials import CLAUDE_API_KEY
from .__utils import run_algorithm

client = anthropic.Anthropic(
  api_key=CLAUDE_API_KEY
)

def run_summarization(data, prompt):
  message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system=prompt,
    messages=[
      {"role": "user", "content": [{ "type": "text", "text": data }]}
    ]
  )

  print(message.content[0].text)
  return message.content[0].text

if __name__ == '__main__':
  try:
    run_algorithm(run_summarization, "claude3", RESULTS_DIRECTORY_NAME_STUDY_3, False)
  except Exception as error:
    print(f'Error running script: {error}')
