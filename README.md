---
base_model: unsloth/Phi-3-mini-4k-instruct-bnb-4bit
language:
- es
library_name: peft
tags:
- finance
- finanzas
- español
- unsloth
- loRA
- alpaca
license: apache-2.0
datasets:
- finanzas_dataset
---

# Asesor Finanzas Phi-3 (LoRA Fine-Tune) 💰📈

Este modelo es un ajuste fino (fine-tune) de **Phi-3 Mini 4k Instruct** diseñado para actuar como un **asesor financiero personal en español**. 

Ha sido entrenado para responder dudas sobre ahorro, inversión, hipotecas, impuestos (normativa española) y planificación financiera, adaptando sus respuestas al perfil específico del usuario (edad, ingresos, tolerancia al riesgo).

## 🚀 Características Principales

- **Especialización:** Finanzas personales, inversión (bolsa, cripto, fondos indexados), fiscalidad española y ahorro.
- **Contextual:** Utiliza el campo `Input` para adaptar el consejo al perfil del usuario (ej: estudiante sin ingresos vs. jubilado conservador).
- **Eficiencia:** Entrenado usando QLoRA (4-bit) con [Unsloth](https://github.com/unslothai/unsloth), lo que lo hace muy rápido y ligero para inferencia.

## 💻 Cómo usar el modelo

### Instalación de dependencias

```bash
pip install unsloth torch transformers accelerate
