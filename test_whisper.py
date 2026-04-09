from faster_whisper import WhisperModel

# cargar modelo de inteligencia artificial
model = WhisperModel("base")

# procesar audio
segments, info = model.transcribe("audio_prueba.mp3")

print("Idioma detectado:", info.language)

print("\nTexto transcrito:\n")

for segment in segments:
    print(segment.text)
    
