BOOKS_DIRECTORY_NAME = './books'
RESULTS_DIRECTORY_NAME_STUDY = './results'
RESULTS_DIRECTORY_NAME_STUDY_2 = './results_2'
RESULTS_DIRECTORY_NAME_STUDY_3 = './results_3'
NUMBER_OF_RANDOM_PAGES = 5
CHARACTERS_PER_PAGE = 3000
"""The threshold of 0.5 for semantic similarity is used to filter out weak connections between words and focus on the most relevant ones.
By considering only pairs of words with a cosine similarity above 0.5, the algorithm can concentrate on capturing strong semantic relationships between words.
This helps to ensure that the score of each node in the graph accurately reflects its importance in the context of the candidate keywords.

A lower threshold might include too many weakly related words in the graph, which could lead to noise in the scoring process and affect the selection of the most relevant keywords.
Conversely, a higher threshold might exclude potentially important connections between words, resulting in a less comprehensive representation of the semantic relationships within the text.

The choice of 0.5 as the threshold represents a reasonable balance between inclusiveness and exclusiveness in the graph construction process.
It allows for the inclusion of meaningful semantic connections while filtering out less relevant word pairs that might contribute to noise in the scoring and keyword selection stages.
"""
SEMANTIC_SIMILARITY_THRESHOLD = 0.5
"""The damping factor which denotes the probability of randomly selecting one node in the graph, and the value is usually set to 0.85"""
DAMPING_FACTOR = 0.85
DAMPING_FACTOR_TF_IDF = 1.3
NUMBER_OF_KEYWORDS = 10
SKIP_EXISTED_FILES = True
SKIP_EXISTED_IMAGE_FILES = True
SELECTED_20_AUTHORS_INDEXES = [0,5,6,9,12,13,14,16,18,20,24,27,28,29,30,31,36,37,41,44]
ONLY_20_SELECTED = True
IMAGE_GENERATION_ALG_TO_CHECK = "co-occurrence-semantic"
PROMPTS_LIST = [
  "You will be provided with a block of text, and your task is to return summarization that describes provided text. Response shouldn't have more than 55 words.",
  "Choose one scene from the text and prepare summarization of it, describing main characters, scene and what is going on",
  "Summarize the following text in a clear and concise manner, preserving all key details and character actions.",
  # "Summarize the text by including the main events, character motivations, and important consequences while maintaining clarity and coherence.",
  # "Provide a summary of the following passage, focusing on the most important events and their impact on the story. Keep it accurate and well-structured, ensuring that all crucial details are retained.",
  # "Summarize the following passage with a focus on its dramatic tension, character emotions, and significant plot developments. Ensure the summary reflects the essence of the scene accurately.",
  "Summarize the following text in no more than 55 words, ensuring that all key events, characters, and motivations are clearly conveyed.",
  "Provide such summary for some scene from provided text, in the way that it can be used for AI image generation.",
]
MAX_IMAGE_GENERATE_RETRIES = 5
