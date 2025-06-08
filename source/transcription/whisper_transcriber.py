import os
import whisper

from source.transcription.whisperX import whisperX_transcription


def transcribe_audio_file(file_path, model_name="base"):
    """Transcribe a single audio file."""
    model = whisper.load_model(model_name)
    transcription = model.transcribe(file_path)
    return transcription


def transcribe_chunk(chunk_path, model_name="base"):
    
    # chunk_name = os.path.basename(chunk_path)
    # print(f"Transcribing chunk {chunk_number}: {chunk_name}...")
    # result = transcribe_audio_file(chunk_path, model_name)
     return whisperX_transcription(chunk_path)
    # return result["text"]

