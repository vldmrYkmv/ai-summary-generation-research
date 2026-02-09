# _*_ encoding=utf8 _*_
__author__ = "Volodymyr"

import sys
import nltk
import networkx as nx
import numpy as np
import time
from typing import List

nltk.download('popular')

from ..shared.constants import *
from ..shared.common import get_candidate_words, run_algorithm_in_results, get_candidate_score

def remove_stop_words(stop_words: List[str], pos_tags_words):
  return [post_tag if post_tag[0] not in stop_words else ["#",'#'] for post_tag in pos_tags_words]

def get_candidate_keywords(no_stop_words_document):
  VALID_TOKEN_TAGS = ['NN', 'JJ', 'NNS', 'NNP']
  candidate_keywords = []
  prev_value = None

  for word in no_stop_words_document:
    if word[1] in VALID_TOKEN_TAGS:
      if prev_value and prev_value[1] == 'JJ':
        prev_adjective = candidate_keywords.pop()
        candidate_keywords.append(f'{prev_adjective} {word[0]}')
      else:
        candidate_keywords.append(word[0])
    prev_value = word
  return candidate_keywords

def calculate_textrank(words, co_occurrence_matrix, damping_factor):
  """Calculates the TextRank score for each word in a given text.

  Args:
    words: A list of words in the text.
    co_occurrence_matrix: A numpy array representing the co-occurrence matrix of the words.
    damping_factor: The damping factor, which denotes the probability of randomly
      selecting one node in the graph. The usual value is 0.85.

  Returns:
    A numpy array containing the TextRank scores for each word in the text.
  """

  # Create a graph from the co-occurrence matrix.
  graph = nx.Graph()
  for i, j in zip(*np.nonzero(co_occurrence_matrix)):
    graph.add_edge(words[i], words[j], weight=co_occurrence_matrix[i, j])

  # Calculate the TextRank scores for each word.
  textrank_scores = nx.pagerank(graph, damping_factor)

  # Return the TextRank scores.
  return textrank_scores

def create_co_occurrence_matrix(words):
  """Creates a co-occurrence matrix for the given words.

  Args:
    words: A list of words.

  Returns:
    A numpy array representing the co-occurrence matrix of the words.
  """

  co_occurrence_matrix = np.zeros((len(words), len(words)))
  for i, word in enumerate(words):
    # print(f"text 1 {i} {word}")
    for j, context_word in enumerate(words):
      # print(f"text 2 {j} {context_word}")
      if i != j and word in context_word:
        # print("co_occurrence_matrix")
        co_occurrence_matrix[i, j] += 1

  return co_occurrence_matrix

def get_candidate_score(words_score, top_number):
  sorted_dict = sorted(words_score.items(), key=lambda x: x[1], reverse=True)[:top_number]
  return sorted_dict

def pos_extract_keywords(document):
  length_filtered_candidate_keywords = get_candidate_words(document)

  co_occurrence_matrix = create_co_occurrence_matrix(length_filtered_candidate_keywords)
  # print(f"co_occurrence_matrix {co_occurrence_matrix}")

  words_score = calculate_textrank(length_filtered_candidate_keywords, co_occurrence_matrix, DAMPING_FACTOR)
  # print(f"words_score {words_score}")

  candidate_score = get_candidate_score(words_score, NUMBER_OF_KEYWORDS)
  # print(f"candidate_score {candidate_score}")

  keywods = []
  for word in candidate_score:
    keywods.append(word[0])

  print(f"keywods {keywods}")
  return keywods

if __name__ == '__main__':
  try:
    start_time = time.time()
    print('Starting script...')
    run_algorithm_in_results(pos_extract_keywords, "textrank-algorithm")
    print('\tFinished sequence for file')
  except Exception as error:
    print(f'Error running script: ', error)
