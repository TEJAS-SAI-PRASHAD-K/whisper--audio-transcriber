import math
import os
from pydub import AudioSegment
from typing import List
from .analyzer import calculate_chunk_duration

CHUNKS_DIR = "/Users/tejassaiprashad/Documents/my_workspace/whisper--audio-transcriber/data/chunks"
DEFAULT_CHUNK_SIZE_MB = 10

def split_audio_into_chunks(audio, bitrate_bps, original_file_path, chunk_size_mb=DEFAULT_CHUNK_SIZE_MB):
    """Split audio into chunks of specified size and save in a folder named after the audio file."""
    
    # Extract the audio file name without extension
    audio_filename = os.path.splitext(os.path.basename(original_file_path))[0]
    
    # Create a subfolder named after the audio file inside the chunks directory
    output_folder = os.path.join(CHUNKS_DIR, audio_filename)
    os.makedirs(output_folder, exist_ok=True)
    
    max_chunk_duration_ms = calculate_chunk_duration(bitrate_bps, chunk_size_mb)
    total_duration_ms = len(audio)
    num_chunks = math.ceil(total_duration_ms / max_chunk_duration_ms)
    
    chunk_paths = []
    print(f"Splitting into {num_chunks} chunks of ~{chunk_size_mb}MB each...")
    
    for i in range(num_chunks):
        start = int(i * max_chunk_duration_ms)
        end = int(min((i + 1) * max_chunk_duration_ms, total_duration_ms))
        chunk = audio[start:end]
        
        chunk_filename = f"chunk_{i + 1:03d}.wav"
        chunk_path = os.path.join(output_folder, chunk_filename)
        
        chunk.export(chunk_path, format="wav")
        chunk_paths.append(chunk_path)
        
        print(f"Created {chunk_filename} (from {start/1000:.2f}s to {end/1000:.2f}s)")
    
    return chunk_paths
