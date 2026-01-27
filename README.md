# 💰 Asesor Finanzas Phi-3 (Spanish LoRA Fine-Tune)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PEFT](https://img.shields.io/badge/PEFT-LoRA-orange)
![Unsloth](https://img.shields.io/badge/Unsloth-Optimized-green)
![License](https://img.shields.io/badge/License-Apache_2.0-red)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Model-yellow)

This project implements a **Personal Financial Assistant in Spanish** based on Microsoft's **Phi-3 Mini 4k Instruct** model.

The model has undergone a fine-tuning process using **QLoRA** and the Unsloth library to answer questions regarding savings, investing, mortgages, and taxation (specifically Spanish regulations), adapting its responses to the user's risk profile and personal situation.

🔗 **Model avaliable on Hugging Face:** [AdrianML7/asesor-finanzas-phi3](https://huggingface.co/AdrianML7/asesor-finanzas-phi3)

---

## 🚀 Key Features

* **🧠 Base Model:** `unsloth/Phi-3-mini-4k-instruct-bnb-4bit` (Optimized for low VRAM usage).
* **🗣️ Language:** Native Spanish.
* **🎯 Contextual:** Trained to utilize the `Input` field of the prompt. It does not provide generic advice; it adapts the response depending on whether the user is a "student with no income" or a "conservative retiree."
* **📚 Specific Knowledge:** Covers topics such as:
    * Stock Market and Index Fund investing.
    * Taxation and Income Tax filing in Spain.
    * Cryptocurrencies (with risk warnings).
    * Retirement planning and mortgages.
* **⚡ Performance:** Trained and optimized for fast inference with 4-bit quantization.

---

## 🛠️ Running the model

To run this model, using a GPU environment (Google Colab T4 or local with CUDA) is recommended.
