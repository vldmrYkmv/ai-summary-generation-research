import sys
import torch
import clip
import time
import os
import json
from PIL import Image

sys.path.append('../../shared')
from constants import RESULTS_DIRECTORY_NAME
from common import get_files_list, is_prompt_directory, is_text_results_directory, read_file, save_text_to_file

def get_clip_score(image_path, text):
  # Load the pre-trained CLIP model and the image
  model, preprocess = clip.load('ViT-B/32')
  image = Image.open(image_path)

  # Preprocess the image and tokenize the text
  image_input = preprocess(image).unsqueeze(0)
  text_input = clip.tokenize([text])
  
  # Move the inputs to GPU if available
  device = "cuda" if torch.cuda.is_available() else "cpu"
  image_input = image_input.to(device)
  text_input = text_input.to(device)
  model = model.to(device)
  
  # Generate embeddings for the image and text
  with torch.no_grad():
      image_features = model.encode_image(image_input)
      text_features = model.encode_text(text_input)
  
  # Normalize the features
  image_features = image_features / image_features.norm(dim=-1, keepdim=True)
  text_features = text_features / text_features.norm(dim=-1, keepdim=True)
  
  # Calculate the cosine similarity to get the CLIP score
  clip_score = torch.matmul(image_features, text_features.T).item()
  
  return round(clip_score * 10, 4)

if __name__ == '__main__':
  try:
    start_time = time.time()
    results_score = {}
    algorithms_types = ['claude3', 'gemini', 'gpt4']
    # algorithms_types = ['gpt4']
    image_generator_service = ['dalle', 'stable-diffusion-6', 'midjourney']
    # image_generator_service = ['dalle']
    images_dir_path = f"../{RESULTS_DIRECTORY_NAME}"
    print(f'Image path {images_dir_path}')
    files_list = get_files_list(images_dir_path, False)
    print(f'Found {len(files_list)} directories in "{images_dir_path}" directory...')
    for index, directory_name in enumerate(files_list):
      print(f'[{index + 1}/{len(files_list)}] Starting sequence for "{directory_name}" book...')
      if not os.path.isdir(f"{images_dir_path}/{directory_name}"):
        continue

      pages_list = get_files_list(f"{images_dir_path}/{directory_name}")
      print(f'Found {len(pages_list)} pages directories...')
      results_score[f'{directory_name}'] = {}
      for page_index, page_directory_name in enumerate(pages_list):
        page_directory_files_list = get_files_list(f"{images_dir_path}/{directory_name}/{page_directory_name}")
        print(page_directory_files_list)
        prompt_directories_list = list(filter(is_prompt_directory, page_directory_files_list))
        print(prompt_directories_list)
        results_score[f'{directory_name}'][f'{page_directory_name}'] = {}
        for prompt_directory_index, prompt_directory_name in enumerate(prompt_directories_list):
          text_summaries_directory_path = f"{images_dir_path}/{directory_name}/{page_directory_name}/{prompt_directory_name}"
          summaries_list = get_files_list(text_summaries_directory_path)
          # print(summaries_list)
          results_score[f'{directory_name}'][f'{page_directory_name}'][f'{prompt_directory_name}'] = {}
          for algorithm in algorithms_types:
            # print(algorithm)
            text_file = f"{images_dir_path}/{directory_name}/{page_directory_name}/{prompt_directory_name}/{algorithm}.json"
            # print(text_file)
            with open(text_file) as f:
              d = json.load(f)
              text = d[0]
            results_score[f'{directory_name}'][f'{page_directory_name}'][f'{prompt_directory_name}'][f'{algorithm}'] = {}
            for image_generator in image_generator_service:
              img_path = f"{images_dir_path}/{directory_name}/{page_directory_name}/{prompt_directory_name}/{algorithm}-{image_generator}.png"
              if not os.path.exists(img_path):
                print(f"should skip: {img_path}")
                continue
              print(img_path)
              start_time_clip_score = time.time()
              score = get_clip_score(img_path, text)
              results_score[f'{directory_name}'][f'{page_directory_name}'][f'{prompt_directory_name}'][f'{algorithm}'][f'{image_generator}'] = score
              end_time_clip_score = time.time()
              print(f"CLIP Score: {score}; time: {round(end_time_clip_score - start_time_clip_score, 2)}s")

        # attempt to score image created from the text
        # text_results_directories_list = list(filter(is_text_results_directory, page_directory_files_list))
        # print(text_results_directories_list)
        # for text_results_directory_index, text_results_directory_name in enumerate(text_results_directories_list):
        #   text_results_directory_path = f"{images_dir_path}/{directory_name}/{page_directory_name}/{text_results_directory_name}"
        #   summaries_list = get_files_list(text_results_directory_path)
        #   print(summaries_list)
        #   text_file = f"{images_dir_path}/{directory_name}/{page_directory_name}/{directory_name}.txt"
        #   print(text_file)
        #   text_data = read_file(f"{images_dir_path}/{directory_name}/{page_directory_name}", f"{directory_name}.txt")
        #   for image_generator in image_generator_service:
        #     img_path = f"{images_dir_path}/{directory_name}/{page_directory_name}/{text_results_directory_name}/{directory_name}-{image_generator}.png"
        #     if not os.path.exists(img_path):
        #       print(f"should skip: {img_path}")
        #       continue
        #     print(img_path)
        #     score = get_clip_score(img_path, text_data)
        #     results_score[f'{directory_name}'][f'{page_directory_name}']['text_results'][f'{image_generator}'] = score
        #     print(f"CLIP Score: {score}")
    save_text_to_file(json.dumps(results_score, ensure_ascii=False), f"../{RESULTS_DIRECTORY_NAME}/clip_score2.json")
    end_time = time.time()
    print("Execution time:", end_time - start_time)
  except Exception as error:
    print(f'Error running script: {error}')
