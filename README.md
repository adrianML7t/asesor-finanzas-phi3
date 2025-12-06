# 💰 Asesor Finanzas Phi-3 (Spanish LoRA Fine-Tune)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PEFT](https://img.shields.io/badge/PEFT-LoRA-orange)
![Unsloth](https://img.shields.io/badge/Unsloth-Optimized-green)
![License](https://img.shields.io/badge/License-Apache_2.0-red)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Model-yellow)

Este proyecto implementa un **Asistente Financiero Personal en Español** basado en el modelo **Phi-3 Mini 4k Instruct** de Microsoft. 

El modelo ha sido sometido a un proceso de ajuste fino (Fine-Tuning) utilizando **QLoRA** y la librería **Unsloth** para responder preguntas sobre ahorro, inversión, hipotecas y fiscalidad (especialmente normativa española), adaptando sus respuestas al perfil de riesgo y situación personal del usuario.

🔗 **Modelo en Hugging Face:** [AdrianML7/asesor-finanzas-phi3](https://huggingface.co/AdrianML7/asesor-finanzas-phi3)

---

## 🚀 Características Principales

* **🧠 Base Model:** `unsloth/Phi-3-mini-4k-instruct-bnb-4bit` (Optimizado para bajo consumo de VRAM).
* **🗣️ Idioma:** Español nativo.
* **🎯 Contextual:** Entrenado para utilizar el campo `Input` del prompt. No da consejos genéricos; adapta la respuesta si el usuario es un "estudiante sin ingresos" o un "jubilado conservador".
* **📚 Conocimiento Específico:** Cubre temas como:
    * Inversión en Bolsa y Fondos Indexados.
    * Fiscalidad y declaración de la Renta en España.
    * Criptomonedas (con advertencias de riesgo).
    * Planificación de jubilación e hipotecas.
* **⚡ Rendimiento:** Entrenado y optimizado para inferencia rápida con cuantización de 4-bits.

---

## 🛠️ Instalación

Para ejecutar este modelo, se recomienda utilizar un entorno con GPU (Google Colab T4 o local con CUDA).
