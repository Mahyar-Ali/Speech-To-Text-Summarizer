from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch

def build():
  processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
  model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
  return model, processor

def predict(model,processor, speech):
  input_values = processor(speech, return_tensors="pt", padding="longest").input_values  # Batch size 1
  logits = model(input_values).logits
  predicted_ids = torch.argmax(logits, dim=-1)
  transcription = processor.batch_decode(predicted_ids)
  return transcription