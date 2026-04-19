# RIMAI-research
Repositorio de pruebas de librerías para el proyecto **RIMAI (IEEE CIS UNI)**.

Este repositorio contiene experimentos orientados a validar la viabilidad técnica de distintos módulos de inteligencia artificial aplicados al análisis de comunicación oral, incluyendo procesamiento de audio, detección de muletillas, generación automática de reportes y análisis de lenguaje corporal mediante visión por computadora.

El objetivo es construir una base tecnológica que permita evaluar presentaciones considerando tanto componentes **verbales** como **no verbales**.

# 1. Faster-Whisper

## Descripción
Se probó la librería **faster-whisper** para convertir audio en texto usando inteligencia artificial.  
El objetivo fue validar la capacidad del sistema para procesar presentaciones orales en español y obtener transcripciones automáticas de manera precisa.

La tecnología Whisper utiliza modelos de deep learning entrenados para reconocimiento automático de voz (ASR).

## Flujo
audio → detección de idioma → transcripción automática

## Resultado
El modelo detectó correctamente el idioma español y generó la transcripción del audio de prueba.

Esto permite obtener el contenido textual de una presentación oral de forma automática.

## Conclusión
La herramienta funciona correctamente y puede utilizarse para analizar presentaciones orales, evaluar comunicación verbal y detectar muletillas.

## Archivos
- `test_whisper.py`
- `audio_prueba.mp3`
- `resultado.png`

## Aplicación en RimAI
Este módulo valida la capacidad del sistema para:

- procesar audio automáticamente
- convertir voz en texto
- analizar presentaciones orales
- servir como base para detección de muletillas
- apoyar la evaluación de comunicación verbal

Este resultado demuestra la viabilidad técnica del reconocimiento automático de voz como componente base del proyecto RimAI.

---

# 2. Generación automática de reporte en PDF (ReportLab + Faster-Whisper)

## Descripción
Se desarrolló un script que integra transcripción automática de audio con generación de reportes en PDF.

El sistema procesa un archivo de audio, identifica el texto hablado y calcula la frecuencia de muletillas comunes en el discurso.

Se utilizó la librería **ReportLab** para construir el reporte estructurado en formato PDF.

## Flujo
audio → transcripción → detección de muletillas → generación de reporte PDF

## Resultado
El script logró:

- procesar el audio de prueba
- generar la transcripción automática
- calcular frecuencia de muletillas
- crear un reporte estructurado en PDF

El reporte contiene el texto detectado y métricas de comunicación verbal.

## Ejemplo de muletillas analizadas
- eh
- este
- o sea
- osea

## Conclusión
La integración de **faster-whisper** con **reportlab** permite construir reportes automáticos de análisis de comunicación.

Este módulo constituye un componente clave para el sistema RimAI orientado a evaluar:

- fluidez verbal
- claridad del discurso
- patrones de lenguaje
- calidad de la comunicación oral

## Archivos
- `crear_pdf.py`
- `audio_prueba.mp3`
- `reporte_rimai.pdf`
- `evidencia_reportlab.png`

## Aplicación en RimAI
Este módulo valida la capacidad del sistema para:

- procesar audio automáticamente
- analizar el contenido del discurso
- detectar patrones de lenguaje
- generar reportes estructurados
- construir métricas de comunicación oral

Este resultado demuestra la viabilidad técnica de implementar análisis automático de presentaciones orales dentro del proyecto RimAI.

---

# 3. MediaPipe – Video / Camera Analysis

## Descripción
Se probó la librería **MediaPipe** de Google para el análisis de video en tiempo real mediante visión por computadora.

El experimento se enfocó en la detección de manos utilizando la cámara web, identificando puntos clave (*landmarks*) que representan la estructura de los dedos y la palma.

MediaPipe utiliza modelos preentrenados optimizados para aplicaciones en tiempo real, permitiendo detectar características visuales sin necesidad de entrenar modelos desde cero.

Cada mano detectada contiene 21 puntos clave que describen la posición de:

- dedos
- articulaciones
- palma
- orientación de la mano

## Flujo
video en tiempo real → detección de manos → identificación de landmarks → visualización de puntos clave

## Resultado
El sistema logró detectar correctamente ambas manos en tiempo real, identificando 21 puntos clave por mano.

Los puntos permiten analizar:

- posición de los dedos
- movimiento de la mano
- gestos básicos
- patrones de lenguaje corporal

La detección fue estable incluso con movimiento moderado frente a la cámara.

## Conclusión
MediaPipe constituye una herramienta viable para el análisis de lenguaje no verbal dentro del proyecto RimAI.

Permite capturar información sobre gestos, postura de manos y patrones de movimiento que pueden complementar el análisis de comunicación verbal.

## Archivos
- `main.py`
- `mediapipe_resultado.png`


# Tecnologías utilizadas

- Python
- Faster-Whisper
- ReportLab
- MediaPipe
- OpenCV
- Machine Learning
- Speech Recognition
- Computer Vision





