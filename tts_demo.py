# tts_demo.py
# Author: Auwal Ahmad
# Description: Simple Text-to-Speech using Coqui TTS

from TTS.api import TTS

# Load a pre-trained English TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True)

# Synthesize and save speech to file
tts.tts_to_file(
    text="Hello Auwal, this is your first machine-generated speech!",
    file_path="output.wav"
)

