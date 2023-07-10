import whisper
# import pytube
# #https://github.com/openai/whisper
# video = "https://www.youtube.com/watch?v=BYkHLlKFEsM"
# data = pytube.YouTube(video)
# audio = data.streams.get_audio_only()
# audio.download()
name='实验1-1新建工程.mp4'
model = whisper.load_model("base")
text = model.transcribe(r'./static/data/'+name)
print(text['text'])