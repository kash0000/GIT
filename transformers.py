import pandas as pd
import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AdamW, get_linear_schedule_with_warmup
from torch.utils.data import DataLoader, TensorDataset, random_split
from tqdm import tqdm

# Load your dataset
data = pd.read_csv('fruits_data.csv')

# Prepare data
input_text = []  # List to store input text (column names and numerical data)
target_text = []  # List to store target commentaries

for index, row in data.iterrows():
    # Concatenate column names and numerical data into input text
    input_text.append(f"Column names: {', '.join(row.index[1:-1])}. Numerical data: {', '.join(map(str, row.values[1:-1]))}.")
    # Store commentaries as target text
    target_text.append(row['Commentary'])

# Initialize the GPT-2 model and tokenizer
model_name = "gpt2-medium"  # You can adjust the model size
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Tokenize and encode data
input_ids = []
for text in input_text:
    input_ids.append(tokenizer.encode(text, add_special_tokens=True, padding='max_length', max_length=128, truncation=True, return_tensors='pt'))

target_ids = []
for text in target_text:
    target_ids.append(tokenizer.encode(text, add_special_tokens=True, padding='max_length', max_length=128, truncation=True, return_tensors='pt'))

# Convert to PyTorch tensors
input_ids = torch.cat(input_ids, dim=0)
target_ids = torch.cat(target_ids, dim=0)

# Create DataLoader for batching
dataset = TensorDataset(input_ids, target_ids)
batch_size = 4  # Adjust as needed
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Fine-tuning
optimizer = AdamW(model.parameters(), lr=1e-4)
scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=100, num_training_steps=len(dataloader) * 10)

# Training loop (simplified)
num_epochs = 10  # Adjust as needed
model.train()
for epoch in range(num_epochs):
    for batch in tqdm(dataloader, desc=f'Epoch {epoch + 1}'):
        optimizer.zero_grad()
        input_batch, target_batch = batch
        outputs = model(input_ids=input_batch, labels=target_batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        scheduler.step()

# Inference
model.eval()
generated_commentaries = []
for input_batch in input_ids:
    output_ids = model.generate(input_batch, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
    generated_commentaries.append(tokenizer.decode(output_ids[0], skip_special_tokens=True))

# Print generated commentaries
for i, commentary in enumerate(generated_commentaries):
    print(f"Row {i + 1} Commentary: {commentary}")

# Save or use the generated commentaries as needed
