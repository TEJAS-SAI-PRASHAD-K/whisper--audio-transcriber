def format_timestamp(start_time, end_time=None):
    """Convert seconds to MM:SS format"""
    def seconds_to_mmss(seconds):
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes:02d}:{secs:02d}"
    
    if end_time:
        return f"{seconds_to_mmss(start_time)} - {seconds_to_mmss(end_time)}"
    else:
        return seconds_to_mmss(start_time)

def extract_transcription(segments):
    """
    Extract clean transcription from WhisperX segments
    """
    transcription_results = {
        "full_transcript": "",
        "speaker_segments": [],
        "timeline": [],
        "speakers": set()
    }
    
    for segment in segments:
        # Extract basic info
        text = segment.get('text', '').strip()
        start_time = segment.get('start', 0)
        end_time = segment.get('end', 0)
        speaker = segment.get('speaker', 'UNKNOWN')
        
        # Add to full transcript
        transcription_results["full_transcript"] += text + " "
        
        # Create speaker segment
        speaker_segment = {
            "speaker": speaker,
            "start_time": start_time,
            "end_time": end_time,
            "text": text,
            "duration": round(end_time - start_time, 2),
            "timestamp": format_timestamp(start_time, end_time)
        }
        transcription_results["speaker_segments"].append(speaker_segment)
        
        # Add to timeline
        timeline_entry = {
            "timestamp": format_timestamp(start_time, end_time),
            "speaker": speaker,
            "text": text
        }
        transcription_results["timeline"].append(timeline_entry)
        
        # Track speakers
        transcription_results["speakers"].add(speaker)
    
    # Clean up
    transcription_results["speakers"] = list(transcription_results["speakers"])
    transcription_results["full_transcript"] = transcription_results["full_transcript"].strip()
    
    return transcription_results