RIMAI-research  
Repositorio de pruebas de librerías para el proyecto RIMAI (IEEE CIS UNI).

1. Faster-Whisper

Descripción:  
Se probó la librería faster-whisper para convertir audio en texto usando inteligencia artificial.

Resultado:  
El modelo detectó correctamente el idioma español y generó la transcripción del audio de prueba.

Conclusión:  
La herramienta funciona correctamente y puede utilizarse para analizar presentaciones orales, evaluar comunicación verbal y detectar muletillas.

Archivos:

test_whisper.py  
audio_prueba.mp3  
resultado.png


2. Generación automática de reporte en PDF (ReportLab + Faster-Whisper)

Descripción:  
Se desarrolló un script que integra transcripción automática de audio con generación de reportes en PDF. El sistema procesa un archivo de audio, identifica el texto hablado y calcula la frecuencia de muletillas comunes en el discurso.

El flujo implementado fue:

audio → transcripción → detección de muletillas → generación de reporte PDF

Resultado:  
El script logró procesar el audio de prueba, generar la transcripción automática y crear un reporte en formato PDF con el contenido del discurso y el conteo de muletillas detectadas.

Ejemplo de muletillas analizadas:

- eh
- este
- o sea
- osea

Conclusión:  
La integración de faster-whisper con reportlab permite construir reportes automáticos de análisis de comunicación, lo cual constituye un componente clave para el sistema RimAI orientado a evaluar fluidez verbal, claridad del discurso y patrones de lenguaje.

Archivos:

crear_pdf.py  
audio_prueba.mp3  
reporte_rimai.pdf  
 
evidencia reportlab.png


Aplicación en RimAI:

Este módulo valida la capacidad del sistema para:

- procesar audio automáticamente
- analizar el contenido del discurso
- detectar patrones de lenguaje
- generar reportes estructurados
- construir métricas de comunicación oral

Este resultado demuestra la viabilidad técnica de implementar análisis automático de presentaciones orales dentro del proyecto RimAI.
