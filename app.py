import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import MODEL_PATH, TOKENIZER_PATH, NUM_LABELS
from models.ner_model import NERLSTMModel
from tokenization.tokenizer import load_tokenizer
from utils.utils import predict

app = FastAPI()

class TextInput(BaseModel):
    text: str

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = load_tokenizer(TOKENIZER_PATH)
vocab_size = tokenizer.vocab_size
model = NERLSTMModel(vocab_size, NUM_LABELS)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

@app.post("/predict/")
async def get_prediction(input: TextInput):
    try:
        result = predict(input.text, model, tokenizer, device)
        return {"entities": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
