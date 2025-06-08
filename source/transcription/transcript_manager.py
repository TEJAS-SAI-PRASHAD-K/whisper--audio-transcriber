import os
from typing import List
from .whisper_transcriber import transcribe_chunk

CHUNKS_DIR = "/Users/tejassaiprashad/Documents/my_workspace/whisper--audio-transcriber/data/chunks"
OUTPUT_DIR = "/Users/tejassaiprashad/Documents/my_workspace/whisper--audio-transcriber/data/output"


# def save_transcript(transcript, filename):
#     """Save transcript to output directory."""
#     output_path = os.path.join(OUTPUT_DIR, filename)

#     # Ensure output directory exists
#     os.makedirs(OUTPUT_DIR, exist_ok=True)
#     # with open(output_path, 'w', encoding='utf-8') as f:
#     #     f.write(transcript)
#     # return output_path
#     with open(transcript, 'w', encoding='utf-8') as f:
#         f.write("TRANSCRIPTION SUMMARY\n")
#         f.write("=" * 50 + "\n")
#         f.write(f"Speakers: {', '.join(transcript['speakers'])}\n")
#         f.write(f"Total segments: {len(transcript['speaker_segments'])}\n\n")
        
#         f.write("FULL TRANSCRIPT\n")
#         f.write("=" * 50 + "\n")
#         f.write(transcript['full_transcript'] + "\n\n")
        
#         f.write("SPEAKER-SEGMENTED TRANSCRIPT\n")
#         f.write("=" * 50 + "\n")
#         for segment in transcript['speaker_segments']:
#             f.write(f"[{segment['timestamp']}] {segment['speaker']}: {segment['text']}\n")

def save_transcript(transcript, filename):
    """Save transcript to output directory."""
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Correct: generate full output path using filename
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Open the file path (not the transcript dict!)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("TRANSCRIPTION SUMMARY\n")
        f.write("=" * 50 + "\n")
        f.write(f"Speakers: {', '.join(transcript['speakers'])}\n")
        f.write(f"Total segments: {len(transcript['speaker_segments'])}\n\n")

        f.write("FULL TRANSCRIPT\n")
        f.write("=" * 50 + "\n")
        f.write(transcript['full_transcript'] + "\n\n")

        f.write("SPEAKER-SEGMENTED TRANSCRIPT\n")
        f.write("=" * 50 + "\n")
        for segment in transcript['speaker_segments']:
            f.write(f"[{segment['timestamp']}] {segment['speaker']}: {segment['text']}\n")
    
    print(f"[✔] Transcript saved to: {output_path}")

def transcribe_all_chunks(chunk_files,model_name="base"):
    
    full_transcript = ""
    
    # for i, chunk_file in enumerate(chunk_files, 1):
    #     chunk_path = os.path.join(CHUNKS_DIR, chunk_file)
    #     chunk_transcript = transcribe_chunk(chunk_path, i, model_name)
    #     full_transcript += f"\n\n[Chunk {i}] : {chunk_transcript}"
    chunk_transcript = transcribe_chunk(chunk_files, model_name)
    full_transcript += f"\n\n[Chunk] : {chunk_transcript}"
    
    print(full_transcript)
    return full_transcript.strip()



import json

import json
import ast

def print_transcription(transcription_data):
    """Print formatted transcription"""
    
    # Step 1: Convert string to dict if needed
    if isinstance(transcription_data, str):
        if transcription_data.startswith("[Chunk] :"):
            transcription_data = transcription_data.replace("[Chunk] :", "", 1).strip()
        transcription_data = ast.literal_eval(transcription_data)  # ← safer than json.loads()

    # Step 2: Proceed as dictionary
    print("\n" + "=" * 60)
    print("TRANSCRIPTION RESULTS")
    print("=" * 60)
    print("DEBUG transcription_data:", transcription_data)
    print("DEBUG type:", type(transcription_data))
    print(f"Speakers detected: {', '.join(transcription_data['speakers'])}")
    print(f"Total segments: {len(transcription_data['speaker_segments'])}")
    
    print("\n" + "=" * 60)
    print("FULL TRANSCRIPT")
    print("=" * 60)
    print(transcription_data['full_transcript'])
    
    print("\n" + "=" * 60)
    print("TIMELINE TRANSCRIPT")
    print("=" * 60)
    for segment in transcription_data['speaker_segments']:
        print(f"[{segment['timestamp']}] {segment['speaker']}: {segment['text']}")


