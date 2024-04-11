from youtube_transcript_api import YouTubeTranscriptApi


def video_transcription(video_id:str):
    """
    Gets video transription in russian or english and returns text as a string.
            
    Args:
        url (str): The YouTube video ID.
            
    Returns:
        str: The transripted text of a video.
    """
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    try:
        transcript = transcript_list.find_transcript(["ru", "en"])

        if transcript:
            transcript_text = transcript.fetch()
            # Combining all text pieces into a single string
            full_transcript = " ".join([item["text"] for item in transcript_text])
            return full_transcript.strip()
        else:
            return None
    except Exception as e:
        print(e)


def extract_video_id(url:str):
    """
    Extracts the video ID from a YouTube URL.
            
    Args:
        url (str): The YouTube video URL.
            
    Returns:
        str: The extracted video ID or None if not found.
    """
    import re
            # Regular expression for extracting the video ID from a YouTube URL
    youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    youtube_match = re.match(youtube_regex, url)
    if youtube_match:
        return youtube_match.group(6)
    else:
        return None
    

