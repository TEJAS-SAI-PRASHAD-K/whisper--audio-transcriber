import ffmpeg

def extract_bitrate(file_path):
    probe = ffmpeg.probe(file_path)
    audio_stream = next(stream for stream in probe['streams'] if stream['codec_type'] == 'audio')
    return int(audio_stream['bit_rate'])

    

def calculate_chunk_duration(bitrate_bps, target_size_mb):
    """Calculate maximum chunk duration for target file size."""
    bytes_per_ms = bitrate_bps / 8 / 1000
    max_duration_ms = (target_size_mb * 1024 * 1024) / bytes_per_ms
    return max_duration_ms