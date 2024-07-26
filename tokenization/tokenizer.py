from transformers import BertTokenizerFast

def load_tokenizer(tokenizer_path):
    return BertTokenizerFast.from_pretrained(tokenizer_path)
