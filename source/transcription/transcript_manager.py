import os
from typing import List
from .whisper_transcriber import transcribe_chunk

CHUNKS_DIR = "/Users/tejassaiprashad/Documents/my_workspace/whisper--audio-transcriber/data/chunks"
OUTPUT_DIR = "/Users/tejassaiprashad/Documents/my_workspace/whisper--audio-transcriber/data/output"


def save_transcript(transcript, filename):
    """Save transcript to output directory."""
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(transcript)
    return output_path


def transcribe_all_chunks(chunk_files,model_name="base"):
    
    full_transcript = ""
    
    for i, chunk_file in enumerate(chunk_files, 1):
        chunk_path = os.path.join(CHUNKS_DIR, chunk_file)
        chunk_transcript = transcribe_chunk(chunk_path, i, model_name)
        full_transcript += f"\n\n[Chunk {i}] : {chunk_transcript}"
    
    print(full_transcript)
    return full_transcript.strip()
