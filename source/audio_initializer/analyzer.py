import subprocess
import json

def extract_bitrate(file_path):
    """Extract bitrate using ffprobe."""
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=bit_rate",
        "-of", "json",
        file_path
    ]
    
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.stderr:
        print("ffprobe error:", result.stderr)
        return None
    
    try:
        bitrate_info = json.loads(result.stdout)
        return int(bitrate_info["streams"][0]["bit_rate"])
    except (KeyError, IndexError, ValueError) as e:
        print("Error parsing bitrate info:", e)
        return None
    

def calculate_chunk_duration(bitrate_bps, target_size_mb):
    """Calculate maximum chunk duration for target file size."""
    bytes_per_ms = bitrate_bps / 8 / 1000
    max_duration_ms = (target_size_mb * 1024 * 1024) / bytes_per_ms
    return max_duration_ms