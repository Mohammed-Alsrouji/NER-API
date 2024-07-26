import os

MODEL_PATH = os.getenv('MODEL_PATH', 'models/model_v3/ner_model.pt')
TOKENIZER_PATH = os.getenv('TOKENIZER_PATH', 'models/model_v3')
NUM_LABELS = int(os.getenv('NUM_LABELS', 9))
