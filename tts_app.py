# tts_app.py
import gradio as gr
from TTS.api import TTS

# Load your model only once (faster startup)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

def speak(text):
    output_path = "demo_output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

# Gradio Interface
gr.Interface(
    fn=speak,
    inputs=gr.Textbox(label="Enter Text"),
    outputs=gr.Audio(type="filepath", label="Generated Voice"),
    title="🗣️ Auwal's Text-to-Speech Demo",
    description="Type any English sentence and click 'Submit' to hear the voice."
).launch()
