import whisperx
import os
from source.transcription.utils import extract_transcription
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv(dotenv_path="//Users/tejassaiprashad/Documents/my_workspace/whisper--audio-transcriber/.env")


# Access your token
HF_TOKEN = os.getenv("HF_TOKEN")

def whisperX_transcription(file_path):
    device = "cpu"
    audio_file = file_path
    batch_size = 4 # reduce if low on GPU mem
    compute_type = "int8" # change to "int8" if low on GPU mem (may reduce accuracy)
    
    # 1. Transcribe with original whisper (batched)
    model = whisperx.load_model("base.en", device, compute_type=compute_type)
    audio = whisperx.load_audio(audio_file)
    result = model.transcribe(audio, batch_size=batch_size)
    print("Initial transcription:", result["segments"]) # before alignment
    
    # 2. Align whisper output
    model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
    print("After alignment:", result["segments"]) # after alignment
    
    # 3. Assign speaker labels
    diarize_model = whisperx.diarize.DiarizationPipeline(use_auth_token=HF_TOKEN, device=device)
    diarize_segments = diarize_model(audio)
    result = whisperx.assign_word_speakers(diarize_segments, result)
    print("Diarization segments:", diarize_segments)
    print("Final result with speakers:", result["segments"]) # segments are now assigned speaker IDs
    
    # EXTRACT TRANSCRIPTION HERE
    transcription_data = extract_transcription(result["segments"])
    
    return transcription_data