import torch

label_map = {
    0: 'O', 1: 'B-PER', 2: 'I-PER', 3: 'B-ORG', 4: 'I-ORG',
    5: 'B-LOC', 6: 'I-LOC', 7: 'B-MISC', 8: 'I-MISC'
}

def predict(sentence, model, tokenizer, device):
    tokens = tokenizer.tokenize(sentence)
    input_ids = tokenizer.convert_tokens_to_ids(tokens)
    input_ids = torch.tensor(input_ids).unsqueeze(0).to(device)
    attention_mask = torch.ones(input_ids.shape).to(device)
    
    with torch.no_grad():
        outputs = model(input_ids, attention_mask)
    predictions = torch.argmax(outputs, dim=2).squeeze().tolist()

    result = [(token, label_map[pred]) for token, pred in zip(tokens, predictions)]
    return result
