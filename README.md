# Using artificial intelligence information technologies to generate content for virtual reality applications

> The article describes a method of image generation with Artificial Intelligence services using text abstraction retrieved using Artificial Intelligence services Dall-e, MidJourney and Stable Diffusion, that works with natural language. The implementation of the new approach gives a significant gain in image quality and consistency with analysed text. The methodology is based on using neural network API service instead of commonly used natural language algorithms to extract keywords or sentences. Proposed evaluation is applied to the generated images. An analysis of evaluation options is carried out depending on algorithm and Artificial Intelligence service, based on the tested book, length of result abstract and number of errors for each type. The evaluation results show that the new approach can provide better quality images that relate more with the text compared to natural language algorithms.

<a href="https://computingonline.net/computing/article/view/3763"><img src="https://computingonline.net/public/journals/1/pageHeaderLogoImage_en_US.gif" height=22.5></a>
<a href="https://science.lpnu.ua/mmc/all-volumes-and-issues/volume-12-number-1-2025/comparison-use-ai-services-based-general-natural"><img src="https://science.lpnu.ua/sites/default/files/journal-cover/3033/covermmc11.jpg" height=22.5></a>
<a href="https://science.lpnu.ua/mmc/all-volumes-and-issues/volume-12-number-3-2025/comparative-analysis-use-instructions-language"><img src="https://science.lpnu.ua/sites/default/files/journal-cover/3033/covermmc11.jpg" height=22.5></a>
<a href="#citation"><img src="https://img.shields.io/badge/Paper-Citation-green?style=for-the-badge&logo=Google%20Scholar" height=22.5></a>

## Description   
This project contains source code and result data on 3 researchs for thesis "Using artificial intelligence information technologies to generate content for virtual reality applications".

## Quick Links
  * [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Setup](#setup)
  * [USAGE](#usage)
      + [Pages Extraction](#pages-extraction)
      + [Research 1](#research-1)
      + [Research 2](#research-2)
      + [Research 3](#research-3)
  * Results data and analysis
      + [Research 1](research_results_analysis/stage_1/README.md)
      + [Research 2](research_results_analysis/stage_2/README.md)
      + [Research 3](research_results_analysis/stage_3/README.md)
  * [Citations](#citation)

## Getting Started
### Prerequisites
- Linux or macOS or Windows
- Python 3.12+

### Setup
- Dependencies:  
To set up the environment, please run:
```
pip install -r requirements.txt
python -m spacy download en_core_web_lg
```

## Usage

### Pages Extraction
At first extract x random pages (in this study it was 5 random pages):
```
python -m src.utils.extract-pages
```
You would get extracted pages in results folder with such structure:
```
results
├── BOOK_NAME_1
│   ├── random_page_1
│   │   └── BOOK_NAME_1.txt
│   ├── random_page_2
│   │   └── BOOK_NAME_1.txt
│   ├── random_page_3
│   │   └── BOOK_NAME_1.txt
│   ├── random_page_4
│   │   └── BOOK_NAME_1.txt
│   └── random_page_5
│       └── BOOK_NAME_1.txt
├── BOOK_NAME_2
│   ├── random_page_1
│   │   └── BOOK_NAME_2.txt
│   ├── random_page_2
│   │   └── BOOK_NAME_2.txt
│   ├── random_page_3
│   │   └── BOOK_NAME_3.txt
│   ├── random_page_4
│   │   └── BOOK_NAME_4.txt
│   └── random_page_5
│       └── BOOK_NAME_5.txt
├── BOOK_NAME_3
....
```


### Research 1
### "Research on the use of AI for Selecting Abstractions for Natural Language Image Generation Tools"
To run the command to extract keywords/abstract from retrieved random pages, i.e.:
```
python -m src.research_1.wordnet
```
As a results a file with keyword list or abstract in json file would be created inside of the directory of tested page with name i.e. **alg-wordnet-result.json**.
To run extraction of keywords/abstract for all algorithms run the file of each algorithm:
```
python -m src.research_1.co-occurrence-semantic
python -m src.research_1.openapi-keywords-gpt-3
python -m src.research_1.openapi-keywords-gpt-4
python -m src.research_1.openapi-sum-gpt-3
python -m src.research_1.openapi-sum-gpt-4
python -m src.research_1.textrank-algorithm
python -m src.research_1.tf-idf-keywords
python -m src.research_1.tf-idf-sum
python -m src.research_1.wordnet
python -m src.research_1.we-spacy
```
Then after retrieving keywords/abstracts for all algorithm to run scripts to generate images run the command for each diffusion model:
```
python -m src.shared.generate-image-dalle --dir=./results
python -m src.shared.generate-image-stable_diffusion --dir=./results
python -m src.shared.generate-image-midjourney --dir=./results
```
where **dir** is the argument for directory with results locations.

After that all data for research 1 was generated. You can find results analysis [here](research_results_analysis/stage_1/README.md)

[Article Link](https://doi.org/10.47839/ijc.23.4.3763)

### Research 2
### Comparison of the use of AI services based on general natural language for generating images for fiction

To run the command to extract abstracts from retrieved random pages, i.e.:
```
python -m src.research_2.openapi-sum-gpt-4
```
As a results a file with abstracts in json file would be created inside of the directory of tested page with name i.e. **alg-gpt-4-sum.json**.

To run extraction of abstract for all algorithms run the file of each algorithm:
```
python -m src.research_2.openapi-sum-gpt-4
python -m src.research_2.claude3
```

Then after retrieving abstracts for all algorithm to run scripts to generate images run the command for each diffusion model:
```
python -m src.shared.generate-image-dalle --dir=./results_2
python -m src.shared.generate-image-stable_diffusion --dir=./results_2
python -m src.shared.generate-image-midjourney --dir=./results_2
```
where **dir** is the argument for directory with results locations.

After that all data for research 2 was generated. You can find results analysis [here](research_results_analysis/stage_2/README.md)

[Article Link](https://doi.org/10.23939/mmc2025.01.283)

### Research 3
### Comparison of the use of AI services based on general natural language for generating images for fiction

To run the command to extract abstracts from retrieved random pages, i.e.:
```
python -m src.research_3.gpt4
```
As a results a file with abstracts in json file would be created inside of the directory of tested page with name i.e. **alg-gpt-4-sum.json**.

To run extraction of abstracts for all algorithms run the file of each algorithm:
```
python -m src.research_3.claude3
python -m src.research_3.gemini
python -m src.research_3.gpt4
```

Then after retrieving abstracts for all algorithm to run scripts to generate images run the command for each diffusion model. Research 3 contains generations using abstraction from LLM models and using full-page text.
Run commands to generate images using generated abstracts:
```
python -m src.research_3.image_summary_generation.dalle --dir=./results_3
python -m src.research_3.image_summary_generation.stable_diffusion --dir=./results_3
python -m src.research_3.image_summary_generation.midjourney --dir=./results_3
```
where **dir** is the argument for directory with results locations.
Run commands to generate images using full-page texts:
```
python -m src.research_3.image_full_page_generation.dalle --dir=./results_3
python -m src.research_3.image_full_page_generation.stable_diffusion --dir=./results_3
python -m src.research_3.image_full_page_generation.midjourney --dir=./results_3
```

After that all data for research 3 was generated. You can find results analysis [here](research_results_analysis/stage_3/README.md)

[Article Link](https://doi.org/10.23939/mmc2025.01.283)


## Citation

If you find our work useful in your research, please consider citing:
```
@inproceedings{ijc.23.4.3763,
  title     = {Research on the use of AI for selecting abstractions for natural language image generation tools},
  author    = {Yakymiv, Volodymyr and Piskozub, Yosyf},
  publisher = {Research Institute for Intelligent Computer Systems},
  pages     = 637-654,
  month     = Jan,
  year      = 2025
}
@inproceedings{mmc2025.01.283,
  title     = {Comparison of the use of {AI} services based on general natural language for generating images for fiction},
  author    = {Yakymiv, V S and Piskozub, Y Z},
  journal   = {Mathematical Modeling and Computing},
  publisher = {Lviv Polytechnic National University},
  volume    = 12,
  number    = 1,
  pages     = 283-298,
  year      = 2025
}
@inproceedings{mmc2025.03.914,
  title     = {Comparative analysis of the use of instructions for language
               models and automated metrics for assessing the quality of images
               generated by GAN models},
  author    = {Yakymiv, V S and Piskozub, Y Z and Oliiarnyk, N R},
  journal   = {Mathematical Modeling and Computing},
  publisher = {Lviv Polytechnic National University},
  volume    =  12,
  number    =  3,
  pages     =  914-935,
  year      =  2025
}
```
