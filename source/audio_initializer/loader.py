import os
from pydub import AudioSegment

def load_audio_file(file_path):
    """Load audio file using pydub."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
    
    audio_file = AudioSegment.from_file(file_path)
    return audio_file