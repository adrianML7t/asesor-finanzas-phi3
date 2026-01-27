import json
import random
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Configuration
NUM_EXAMPLES = 1000  # Set to 1000 for real generation
OUTPUT_FILE = "finanzas_dataset.jsonl"
MODEL_NAME = "gpt-oss:120b-cloud" # Use your most powerful model here

llm = OllamaLLM(model=MODEL_NAME, temperature=0.8)

# Topics to vary the questions
topics = [
    "ahorro personal", "inversión en bolsa", "impuestos en España", 
    "hipotecas", "jubilación", "fondos indexados", "criptomonedas", 
    "deuda y préstamos", "presupuesto familiar", "inflación", "educacion financiera"
]

# User profiles
profiles = [
    "estudiante universitario sin ingresos", "estudiante de finanzas",
    "jubilado conservador", "joven profesional con ahorros", 
    "emprendedor novato", "persona interesada en aprender educación financiera"
]

# Prompt designed to create training pairs (Instruction tuning)
template = """
Eres un generador de datos para entrenar una IA financiera.
Tu tarea es generar UN ÚNICO ejemplo de entrenamiento en formato JSON.
El ejemplo debe simular una consulta de un cliente y una respuesta experta.

Contexto del cliente: {profile}
Tema financiero: {topic}

Requisitos:
1. "instruction": La pregunta directa del usuario.
2. "input": Contexto adicional del usuario (edad, situación, riesgo). Si no aplica, déjalo vacío.
3. "output": La respuesta del asesor financiero. Debe ser empática, técnica pero clara, y siempre incluir una advertencia de riesgo si es inversión.
4. El formato debe ser JSON puro sin bloques de código ni texto adicional.

Formato esperado:
{{
    "instruction": "¿Debería invertir en Bitcoin ahora?",
    "input": "Tengo 30 años y perfil de riesgo alto.",
    "output": "Como asesor, te indico que las criptomonedas son activos volátiles..."
}}

Genera el JSON ahora:
"""

prompt = PromptTemplate(input_variables=["topic", "profile"], template=template)
chain = prompt | llm

print(f"Starting generation of {NUM_EXAMPLES} examples...")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for i in range(NUM_EXAMPLES):
        topic = random.choice(topics)
        profile = random.choice(profiles)
        
        try:
            # Invoke the LLM
            response_text = chain.invoke({"topic": topic, "profile": profile})
            
            # Basic cleanup to ensure valid JSON
            response_text = response_text.strip()
            if response_text.startswith("```json"):
                response_text = response_text.replace("```json", "").replace("```", "")
            
            # Validate that it is parseable JSON
            json_obj = json.loads(response_text)
            
            # Write to JSONL file (one line per object)
            f.write(json.dumps(json_obj, ensure_ascii=False) + "\n")
            
            print(f"[{i+1}/{NUM_EXAMPLES}] Generated topic: {topic}")
            
        except Exception as e:
            print(f"Error in example {i+1}: {e}")

print(f"\nDataset saved to {OUTPUT_FILE}")
