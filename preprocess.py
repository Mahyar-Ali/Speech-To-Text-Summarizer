from pydub import AudioSegment
import soundfile as sf
import os

def _map(batch):
     speech, _ = sf.read(batch)
     return speech

def preprocess(args):
  if (args.input_format == 'wav'):
    sample = AudioSegment.from_mp3("/content/nmse_sample_noisy_0_0.wav")
  else:
    sample = AudioSegment.from_wav("/content/nmse_sample_noisy_0_0.wav")
  os.makedirs('temp_flac_format')
  sample.export("temp_flac_format/test.flac",format = "flac")
  speech = _map('test.flac')
  return speech