'''
    Example code from the Hugging Face model hub
    https://huggingface.co/docs/transformers/en/model_doc/whisper
    
'''

from datasets import load_dataset
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Select an audio file and read it:
ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
audio_sample = ds[0]["audio"]
waveform = audio_sample["array"]
sampling_rate = audio_sample["sampling_rate"]

# Load the Whisper model in Hugging Face format:
processor = WhisperProcessor.from_pretrained("openai/whisper-tiny.en")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")

# Use the model and processor to transcribe the audio:
input_features = processor(
    waveform, sampling_rate=sampling_rate, return_tensors="pt"
).input_features

# Generate token ids
predicted_ids = model.generate(input_features)

# Decode token ids to text
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

transcription[0]