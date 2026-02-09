# _*_ encoding=utf8 _*_
__author__ = "Volodymyr"

import sys
import nltk
import numpy as np
import time
from nltk.corpus import wordnet as wn

nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')
nltk.download('wordnet')

from ..shared.constants import *
from ..shared.common import get_candidate_words, build_graph, run_algorithm_in_results, build_score, get_candidate_score, top_K

def create_semantic_similarity_matrix(candidate_keywords):
  wn.langs()
  similarity_matrix = np.zeros((len(candidate_keywords), len(candidate_keywords)))
  for i, word in enumerate(candidate_keywords):
    word1_syn = wn.synsets(word)
    for j, word2 in enumerate(candidate_keywords):
      word2_syn = wn.synsets(word2)
      if (len(word1_syn) > 0 and len(word2_syn) > 0):
        res = word1_syn[0].path_similarity(word2_syn[0])
        similarity_matrix[i, j] = res
  return similarity_matrix

def run_summarization(document):
  candidate_keywords = get_candidate_words(document)
  # print(f"candidate_keywords {candidate_keywords}\n")

  similarity_matrix = create_semantic_similarity_matrix(candidate_keywords)
  # print(f"similarity_matrix {similarity_matrix}\n")

  # Build a word graph based on the co-occurrence and semantic relations between the candidate keywords
  graph = build_graph(candidate_keywords, similarity_matrix)
  # print(f"graph {graph}\n")

  words_score = build_score(graph)
  # print(f"words_score {words_score}\n")

  candidate_score = get_candidate_score(graph, words_score)
  # print(f"candidate_score {candidate_score}\n")

  keywords = top_K(candidate_score)
  print(f"keywords {keywords}\n")

  return keywords

if __name__ == '__main__':
  try:
    start_time = time.time()
    print('Starting script...')
    run_algorithm_in_results(run_summarization, "wordnet")
    print('\tFinished sequence for file')
  except Exception as error:
    print(f'Error running script: ', error)
