from youtube_transcript_api import YouTubeTranscriptApi

video = 'hd8bawiJRkE'

def video_transcription(input_video):
    transcript_list = YouTubeTranscriptApi.list_transcripts(input_video)
    try:
        transcript = transcript_list.find_transcript(['ru', 'en'])
        
        if transcript:
            transcript_text = transcript.fetch()
            # Combining all text pieces into a single string
            full_transcript = " ".join([item['text'] for item in transcript_text])
            return full_transcript
        else:
            return None
    except Exception as e:
        print(e)
        
print(video_transcription(video))        
        


