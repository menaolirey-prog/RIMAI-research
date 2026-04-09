from faster_whisper import WhisperModel
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# cargar modelo
model = WhisperModel("base")

# transcribir audio
segments, info = model.transcribe("audio_prueba.mp3")

texto = ""

for segment in segments:
    texto += segment.text + " "

print("Transcripción:")
print(texto)

# detectar muletillas
muletillas = ["eh", "este", "osea", "o sea"]

conteo = {}

for palabra in muletillas:
    conteo[palabra] = texto.lower().count(palabra)

print(conteo)

# crear pdf
documento = SimpleDocTemplate("reporte_rimai.pdf", pagesize=letter)

styles = getSampleStyleSheet()

contenido = []

contenido.append(Paragraph("Reporte RimAI", styles["Title"]))

contenido.append(Paragraph("Transcripción:", styles["Heading2"]))
contenido.append(Paragraph(texto, styles["Normal"]))

contenido.append(Paragraph("Muletillas detectadas:", styles["Heading2"]))

for palabra, cantidad in conteo.items():
    contenido.append(Paragraph(f"{palabra}: {cantidad}", styles["Normal"]))

documento.build(contenido)

print("PDF creado")