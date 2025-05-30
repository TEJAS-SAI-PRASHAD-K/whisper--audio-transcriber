import os
import sys
from source.audio_initializer.loader import load_audio_file
from source.audio_initializer.analyzer import extract_bitrate
from source.audio_initializer.chunker import split_audio_into_chunks
from source.transcription.transcript_manager import transcribe_all_chunks, save_transcript


OUTPUT_ENCODING = "utf-8"
SUPPORTED_AUDIO_FORMATS = ['.wav', '.mp3', '.m4a', '.flac', '.ogg']

def is_supported_audio_file(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower() in SUPPORTED_AUDIO_FORMATS


def process_audio_file(input_path, output_filename=None, model_name="base"):
    
    if not is_supported_audio_file(input_path):
        _, ext = os.path.splitext(input_path)
        raise ValueError(f"Unsupported audio format: {ext}")
    

    audio = load_audio_file(input_path)
    bitrate = extract_bitrate(input_path)
    chunk_paths = split_audio_into_chunks(audio, input_path, bitrate or 128000)
    
    full_transcript = transcribe_all_chunks(chunk_paths,model_name="base")
    
    if not output_filename:
        filename_without_ext = os.path.splitext(os.path.basename(input_path))[0]
        output_filename = f"{filename_without_ext}_transcription.txt"
    
    save_transcript(full_transcript, output_filename)


def main():

    input_file = "/Users/tejassaiprashad/Documents/my_workspace/whisper--audio-transcriber/data/input/sample_input.wav"
    
    if os.path.exists(input_file):
        process_audio_file(input_file)
    else:
        print(f"Please place your audio file at: {input_file}")
        print("Or update the path in main() function")


if __name__ == "__main__":
    main()