# _*_ encoding=utf8 _*_
__author__ = "Volodymyr"

import os
import sys
import re
import random
import json
import time
import argparse
import networkx as nx
import nltk
from nltk.corpus import stopwords
from typing import List
import requests
from PIL import Image
from io import BytesIO

from .constants import *

def get_files_list(directory_name, is_top_list=False):
  files = os.listdir(directory_name)
  sorted_files = sorted(files)
  if ONLY_20_SELECTED and is_top_list:
    sorted_files = [sorted_files[index] for index in SELECTED_20_AUTHORS_INDEXES]
  return sorted_files

def read_file(directory_name, file_name):
  file_path = os.path.join(directory_name, file_name)
  with open(file_path, 'r', encoding='utf-8') as f:
      data = f.read()

  return data

def get_random_number(min, max):
  # Returns a random number between min and max, inclusive.
  return random.randint(min, max)

def get_random_paragraph(splitted_data_array):
  # Returns a random paragraph from the given splitsplitted_data_arrayed_data_array.
  random_number_of_paragraph = get_random_number(0, len(splitted_data_array) - 1)
  # random_number_of_paragraph = 2909
  random_paragraph = splitted_data_array[random_number_of_paragraph]
  if random_paragraph == '' or len(random_paragraph) == 0:
    return get_random_paragraph(splitted_data_array)
  return random_number_of_paragraph

def get_random_page(splitted_data_array, used_indexes=None):
  # Returns a random page from the given splitted_data_array.
  paragraph_index = get_random_paragraph(splitted_data_array)
  if used_indexes is not None:
    while paragraph_index in used_indexes:
      paragraph_index = get_random_paragraph(splitted_data_array)
  result = {}
  result["index"] = paragraph_index
  text_array = []
  text_array.append(splitted_data_array[paragraph_index])
  next_paragraph_index = paragraph_index + 1
  while len('\n'.join(text_array)) < CHARACTERS_PER_PAGE:
    if next_paragraph_index >= len(splitted_data_array):
      next_paragraph_index = 0
    text_array.append(splitted_data_array[next_paragraph_index])
    next_paragraph_index += 1
  result["text"] = '\n'.join(text_array)
  return result

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

def filter_unique_words(words):
  unique_words = set()
  filtered_words = []

  for word in words:
    if word not in unique_words:
      unique_words.add(word)
      filtered_words.append(word)

  return filtered_words

def get_candidate_words(document):
  # 1. At first replace all words with hyphens to be a single word
  modified_document= re.sub(r'\b(\w+)-(\w+)\b', r'\1\2', document)

  # 2. Cut the document into words
  words = re.split(r'\W+', modified_document)

  # 3. filtering empty strings
  filtered_list = [word.lower() for word in words if word != ""]

  # 4. Tokenize words
  pos_tags = nltk.pos_tag(filtered_list)
  # print(f"pos_tags {pos_tags}\n")

  # 5. Prepare stop words
  stop_words = set(stopwords.words("english"))

  # 6. Remove stopwords from the list of words
  no_stop_words_document = remove_stop_words(stop_words, pos_tags)
  # print(f"no_stop_words_document {no_stop_words_document}\n")

  # 7. Prepare candidate words based on PoS tags
  candidate_keywords = get_candidate_keywords(no_stop_words_document)
  # print(f"candidate_keywords {candidate_keywords}\n")

  # 8. length filtering
  length_filtered_candidate_keywords = [word for word in candidate_keywords if len(word) > 2]

  # print(f"length_filtered_candidate_keywords length {len(length_filtered_candidate_keywords)}")
  # print(f"length_filtered_candidate_keywords {length_filtered_candidate_keywords}\n")
  return length_filtered_candidate_keywords

def build_graph(candidate_keywords, sm):
  # Create a graph G
  graph = nx.Graph()

  # Add the candidate keywords as nodes to the graph
  for keyword in candidate_keywords:
    graph.add_node(keyword)

  # Add edges to the graph based on the co-occurrence and semantic relations between words
  for i, keyword1 in enumerate(candidate_keywords):
    for j, keyword2 in enumerate(candidate_keywords):
      if i != j and sm[i][j] > SEMANTIC_SIMILARITY_THRESHOLD:
        graph.add_edge(keyword1, keyword2, weight=1)

  return graph

def build_score(graph):# Calculate the score of each node in the graph
  words_score = nx.pagerank(graph)

  return words_score

def get_candidate_score(graph, words_score):
  # Calculate the score of each candidate keyword
  candidate_score = {}
  for keyword, score in words_score.items():
    candidate_score[keyword] = (1 - DAMPING_FACTOR) + DAMPING_FACTOR * sum((words_score[neighbor]) for neighbor in graph.neighbors(keyword))

  return candidate_score

def top_K(candidate_score):
  # Select the top K keywords with the highest scores
  keywords = sorted(candidate_score, key=candidate_score.get, reverse=True)[:NUMBER_OF_KEYWORDS]
  return keywords

  # result_keywords = []

  # sumValues = 0
  # for entry, score in candidate_score.items():
  #   sumValues += score

  # # Average value of a keywords from original text
  # average = (sumValues / len(candidate_score))
  # print(f"average {sumValues} {len(candidate_score)} {average}")

  # for keyword, score in candidate_score.items():
  #     if score >= (average):
  #       result_keywords.append(keyword)

  # return result_keywords

def save_text_to_file(text, file_path):
  directory = os.path.dirname(file_path)

  # Create directory if it doesn't exist
  if not os.path.exists(directory):
    os.makedirs(directory)

  # Save text to file
  with open(file_path, mode='w', encoding="utf-8") as file:
    file.write(text)

def save_image_from_url(url, file_path):
  try:
    response = requests.get(url, stream=True)
    print(response)
    if response.status_code == 200:
      with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
          if chunk:
            file.write(chunk)
      print(f"Image saved to '{file_path}'")
    else:
      print("Failed to download image")
  except Exception as e:
    print(f"An error occurred: {e}")

def save_image_from_data(image_data, file_path):
  try:
    image = Image.open(BytesIO(image_data.image.image_bytes))
    image.save(file_path)
  except Exception as e:
    print(f"An error occurred: {e}")

def checkAlorithmToContinue(alg_file):
  print(f"\talg_file {alg_file}")
  algorithm_name =alg_file.replace('.json', '').replace('alg-', '').replace('-result', '')
  print(f"algorithm_name {algorithm_name}")
  if algorithm_name != IMAGE_GENERATION_ALG_TO_CHECK:
    print("break")
    return True
  return False

def is_png_file(name):
  return ".png" in name

def is_prompt_directory(name):
  return "prompt-" in name

def is_text_results_directory(name):
  return "text_results" in name

def is_json_summary_directory(name):
  return ".json" in name

def run_algorithm_in_results(algorithm_function, algorithm_name, files_path=RESULTS_DIRECTORY_NAME_STUDY, is_top_list=False):
  start_time = time.time()
  files_list = get_files_list(files_path, is_top_list)
  print(f'Found {len(files_list)} directories in "{files_path}" directory...')
  for index, directory_name in enumerate(files_list):
    print(f'[{index + 1}/{len(files_list)}] Starting sequence for "{directory_name}" book...')
    pages_list = get_files_list(f"{files_path}/{directory_name}")
    print(f'Found {len(pages_list)} pages directories...')
    for page_index, page_directory_name in enumerate(pages_list):
      save_file_name = f"{files_path}/{directory_name}/{page_directory_name}/alg-{algorithm_name}-result.json"
      if SKIP_EXISTED_FILES and os.path.exists(save_file_name):
        print(f"Found file '{save_file_name}', Skip checking")
        continue
      else:
        print(f"File '{save_file_name}' doesn't exist or should be overwritten")
      print(f'[{page_index + 1}/{len(pages_list)}] Starting sequence for "{page_directory_name}" page...')
      page_directory_path = f"{files_path}/{directory_name}/{page_directory_name}"
      data = read_file(page_directory_path, f"{directory_name}.txt")
      time.sleep(20)
      result = algorithm_function(data)
      print(f"saving {result} to file {save_file_name}")
      save_text_to_file(json.dumps(result, ensure_ascii=False), save_file_name)
  end_time = time.time()
  print("Execution time:", end_time - start_time)

def parse_dir_args():
    parser = argparse.ArgumentParser(description="Run DALL·E image generation")
    parser.add_argument(
        "--dir",
        dest="results_dir",
        default="./results",
        help="Directory to save generated images"
    )
    return parser.parse_args()
