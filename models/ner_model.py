import torch.nn as nn

class NERLSTMModel(nn.Module):
    def __init__(self, vocab_size, num_labels):
        super(NERLSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, 128)
        self.lstm = nn.LSTM(128, 256, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(256*2, num_labels)
    
    def forward(self, input_ids, attention_mask):
        x = self.embedding(input_ids)
        x, _ = self.lstm(x)
        x = self.fc(x)
        return x