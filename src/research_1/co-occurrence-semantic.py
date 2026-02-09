# _*_ encoding=utf8 _*_
__author__ = "Volodymyr"

import sys
import networkx as nx
import spacy
import time
from scipy.spatial import distance

from ..shared.constants import *
from ..shared.common import get_candidate_words, run_algorithm_in_results

def build_word_graph(words, window_size):
  # Create a graph to represent word co-occurrence
  graph = nx.Graph()

  # Add words as nodes to the graph
  for word in words:
    graph.add_node(word)

  # Count co-occurrence frequencies within a window
  for i, word in enumerate(words):
    window_start = max(0, i - window_size)
    window_end = min(i + window_size + 1, len(words))
    window_words = words[window_start:window_end]

    for context_word in window_words:
      if word != context_word:
        # Check if edge already exists
        if not graph.has_edge(word, context_word):
          # Add edge with co-occurrence frequency as weight
          graph.add_edge(word, context_word, weight=1)
        else:
          # Update edge weight
          current_weight = graph[word][context_word]['weight']
          graph[word][context_word]['weight'] = current_weight + 1

  return graph

def calculate_semantic_similarity(word1, word2):
  # Use a word embedding model to calculate semantic similarity
  # Replace with your preferred word embedding model
  word1_vector = embedding_model(word1).vector
  word2_vector = embedding_model(word2).vector

  # Calculate cosine similarity between word vectors
  similarity = distance.cosine(word1_vector, word2_vector)
  # print(f"word1 {word1} word2 {word2} sim: {similarity}")

  return similarity

def score_word_cooccurrence(graph, word):
  # Calculate the score of a word based on its co-occurrence relationships
  word_score = 0
  for neighbor in graph.neighbors(word):
    edge_weight = graph[word][neighbor]['weight']
    word_score += edge_weight

  return word_score

def score_words(graph, words):
  # Calculate the scores for all words in the graph
  word_scores = {}
  for word in words:
    word_scores[word] = score_word_cooccurrence(graph, word)

  return word_scores

def combine_scores(score_cooccurrence, score_semantic, lambda_value):
  # Combine the scores using the given lambda value
  combined_scores = {}
  for word, co_occurrence_score in score_cooccurrence.items():
    semantic_score = score_semantic[word]
    combined_score = lambda_value * co_occurrence_score + (1 - lambda_value) * semantic_score
    combined_scores[word] = combined_score

  return combined_scores

def keyword_extraction(words, window_size, lambda_value, top_number):
  # Construct the word co-occurrence graph
  graph = build_word_graph(words, window_size)
  print("build word graph - finished")

  # Calculate scores based on word co-occurrence
  score_cooccurrence = score_words(graph, words)
  print("score words - finished")

  # Calculate scores based on semantic similarity
  score_semantic = {}
  words_length = len(words)
  i = 0
  j = 0
  for word1 in words:
    for word2 in words:
      print(f"[{i}-{j}/{words_length}] calculating semantic similarity")
      if word1 != word2:
        similarity = calculate_semantic_similarity(word1, word2)
        if word1 not in score_semantic:
          score_semantic[word1] = 0
        score_semantic[word1] += similarity
      j = j + 1
    i = i + 1
    j = 0
  print("calculate semantic similarity - finished")

  # Combine the two scores
  combined_scores = combine_scores(score_cooccurrence, score_semantic, lambda_value)
  print("combine scores - finished")

  # Identify top-ranked nodes as keywords based on combined scores
  keywords = sorted(combined_scores, key=combined_scores.get, reverse=True)[:top_number]

  return keywords

def run_summarization(document):
  candidate_keywords = get_candidate_words(document)
  print(f"candidate_keywords {candidate_keywords}\n")

  window_size = 2
  lambda_value = 0.5

  keywords = keyword_extraction(candidate_keywords, window_size, lambda_value, NUMBER_OF_KEYWORDS)
  print("Keywords:", keywords)

  return keywords

if __name__ == '__main__':
  try:
    start_time = time.time()
    embedding_model = spacy.load('en_core_web_lg')
    print('Starting script...')
    run_algorithm_in_results(run_summarization, "co-occurrence-semantic")
    print('\tFinished sequence for file')
  except Exception as error:
    print(f'Error running script: ', error)
