from youtube_transcript_api import YouTubeTranscriptApi
import tiktoken


def transcript_video(video_id: str) -> str | None:
    """
    Gets video transription in russian or english and returns text as a string.

    Args:
        url (str): The YouTube video ID.

    Returns:
        str | None: The transripted text of a video or None if it's not available
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


def extract_video_id(url: str) -> str | None:
    """
    Extracts the video ID from a YouTube URL.

    Args:
        url (str): The YouTube video URL.

    Returns:
        str | None: The extracted video ID or None if not found.
    """
    import re

    # Regular expression for extracting the video ID from a YouTube URL
    youtube_regex = (
        r"(https?://)?(www\.)?"
        "(youtube|youtu|youtube-nocookie)\.(com|be)/"
        "(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
    )
    youtube_match = re.match(youtube_regex, str(url))
    if youtube_match:
        return youtube_match.group(6)
    else:
        return None


def reduce_transcript_to_max_tokens(transcript: str, max_tokens: int) -> str:
    """
    Reduces the transcript text to a given maximum number of tokens.

    Args:
        transcript (str): The transcript text.
        max_tokens (int): The maximum number of tokens allowed.

    Returns:
        str: The reduced transcript text.
    """

    encoding = tiktoken.get_encoding("cl100k_base")
    encoded_transcript = encoding.encode(transcript)
    num_tokens = len(encoded_transcript)

    # If tokens of transcript don't exceed max tokens returns the original transcript
    if num_tokens <= max_tokens:
        return transcript

    # Otherwise, find the point in the encoded transcript where max_tokens is reached and decode back to text
    reduced_encoded_transcript = encoded_transcript[:max_tokens]
    reduced_transcript = encoding.decode(reduced_encoded_transcript)
    return reduced_transcript
