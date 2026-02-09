# _*_ encoding=utf8 _*_
__author__ = "Volodymyr"
# Based on https://github.com/akashp1712/nlp-akash/blob/master/text-summarization/TF_IDF_Summarization.py and
# https://github.com/mayank408/TFIDF/blob/master/TFIDF.ipynb, https://www.freecodecamp.org/news/how-to-process-textual-data-using-tf-idf-in-python-cd2bbc0a94a3/
# seems to be not valid

import math
from ..shared.constants import *
from ..shared.common import get_candidate_words, run_algorithm_in_results

def create_frequency_matrix(candidate_words):
  frequency_matrix = {}

  for word in candidate_words:
    word = word.lower()

    if word in frequency_matrix:
      frequency_matrix[word] += 1
    else:
      frequency_matrix[word] = 1

  return frequency_matrix

def create_tf_matrix(freq_matrix):
  tf_matrix = {}
  count_words = len(freq_matrix.items())

  for word, count in freq_matrix.items():
    tf_matrix[word] = count / count_words

  return tf_matrix

def create_idf_matrix(freq_matrix):
  total_documents = len(freq_matrix.items())
  idf_matrix = {}

  for word in freq_matrix.keys():
    idf_matrix[word] = math.log10(total_documents / float(freq_matrix[word]))

  return idf_matrix

def create_tf_idf_matrix(tf_matrix, idf_matrix):
  tf_idf_matrix = {}

  for (word1, value1), (word2, value2) in zip(tf_matrix.items(),
                                              idf_matrix.items()):  # here, keys are the same in both the table
    tf_idf_matrix[word1] = float(value1 * value2)

  return tf_idf_matrix

def score_keywords(tf_idf_matrix) -> dict:
  wordsValue = {}

  for word, score in tf_idf_matrix.items():
    if word not in wordsValue:
      wordsValue[word] = 0
    wordsValue[word] += score

  total_words = len(tf_idf_matrix.items())
  for word, word_score in tf_idf_matrix.items():
    wordsValue[word] = word_score / total_words

  return wordsValue

def find_average_score(keywordsValues) -> int:
  """
  Find the average score from the sentence value dictionary
  :rtype: int
  """
  sumValues = 0
  for entry in keywordsValues:
    sumValues += keywordsValues[entry]

  # Average value of a keywords from original text
  average = (sumValues / len(keywordsValues))

  return average

def extract_keywords(keywords_values, threshold):
  result_keywords = []

  for keyword, score in keywords_values.items():
    if score >= (threshold):
      result_keywords.append(keyword)

  return result_keywords


def run_summarization(document):
  candidate_keywords = get_candidate_words(document)
  # print(f"candidate_keywords {candidate_keywords}")

  # Create the Frequency matrix of the words in document.
  freq_matrix = create_frequency_matrix(candidate_keywords)
  # print(f"freq_matrix {freq_matrix}\n")

  # Calculate TermFrequency and generate a matrix
  tf_matrix = create_tf_matrix(freq_matrix)
  # print(f"tf_matrix {tf_matrix}\n")

  # Calculate IDF and generate a matrix
  idf_matrix = create_idf_matrix(freq_matrix)
  # print(f"idf_matrix {idf_matrix}\n")

  # Calculate TF-IDF and generate a matrix
  tf_idf_matrix = create_tf_idf_matrix(tf_matrix, idf_matrix)
  # print(f"tf_idf_matrix {tf_idf_matrix}\n")

  # Important Algorithm: score the sentences
  keywords_scores = score_keywords(tf_idf_matrix)
  # print(f"keywords_scores {keywords_scores}\n")

  # Find the threshold
  threshold = find_average_score(keywords_scores)
  # print(f"threshold {threshold}")

  # Important Algorithm: Generate the summary
  result = extract_keywords(keywords_scores, DAMPING_FACTOR_TF_IDF * threshold)
  print(f"keywords {result}")
  return result

if __name__ == '__main__':
  try:
    print('Starting script...')
    run_algorithm_in_results(run_summarization, "tf-idf-keywords")
    print('\tFinished sequence for file')
  except Exception as error:
    print(f'Error running script: ', error)
