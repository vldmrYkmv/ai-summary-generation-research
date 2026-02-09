# _*_ encoding=utf8 _*_
__author__ = "Volodymyr"

import sys
import spacy
import numpy as np
import time
from scipy.spatial import distance

from ..shared.constants import *
from ..shared.common import get_candidate_words, build_graph, run_algorithm_in_results, build_score, get_candidate_score, top_K

def calculate_similarity(word1: str, word2: str, nlp) -> int:
  word1_vector = nlp(word1).vector
  word2_vector = nlp(word2).vector

  # Calculate the cosine similarity between the two word vectors
  similarity = distance.cosine(word1_vector, word2_vector)

  return similarity

def create_semantic_similarity_matrix(candidate_keywords):
  # Load the SpaCy model with GloVe word vectors
  nlp = spacy.load('en_core_web_lg')
  similarity_matrix = np.zeros((len(candidate_keywords), len(candidate_keywords)))
  for i, word in enumerate(candidate_keywords):
    for j, context_word in enumerate(candidate_keywords):
      similarity = calculate_similarity(word, context_word, nlp)
      similarity_matrix[i, j] = similarity
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
  # print(f"keywords {keywords}\n")

  return keywords

if __name__ == '__main__':
  try:
    start_time = time.time()
    print('Starting script...')
    run_algorithm_in_results(run_summarization, "we-spacy")
    print('\tFinished sequence for file')
  except Exception as error:
    print(f'Error running script: ', error)
