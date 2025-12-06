import json
import random
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Configuración
NUM_EJEMPLOS = 1000  # Cambia esto a 1000 para la generación real
OUTPUT_FILE = "finanzas_dataset.jsonl"
MODEL_NAME = "gpt-oss:120b-cloud" # Usa tu modelo más potente aquí

llm = OllamaLLM(model=MODEL_NAME, temperature=0.8)

# Temas para variar las preguntas
temas = [
    "ahorro personal", "inversión en bolsa", "impuestos en España", 
    "hipotecas", "jubilación", "fondos indexados", "criptomonedas", 
    "deuda y préstamos", "presupuesto familiar", "inflación", "educacion financiera"
]

perfiles = [
    "estudiante universitario sin ingresos", "estudiante de finanzas",
    "jubilado conservador", "joven profesional con ahorros", 
    "emprendedor novato", "epersona interesada en aprender educación financiera"
]

# Prompt diseñado para crear pares de entrenamiento (Instruction tuning)
template = """
Eres un generador de datos para entrenar una IA financiera.
Tu tarea es generar UN ÚNICO ejemplo de entrenamiento en formato JSON.
El ejemplo debe simular una consulta de un cliente y una respuesta experta.

Contexto del cliente: {perfil}
Tema financiero: {tema}

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

prompt = PromptTemplate(input_variables=["tema", "perfil"], template=template)
chain = prompt | llm

print(f"🚀 Iniciando generación de {NUM_EJEMPLOS} ejemplos...")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for i in range(NUM_EJEMPLOS):
        tema = random.choice(temas)
        perfil = random.choice(perfiles)
        
        try:
            # Invocar al LLM
            response_text = chain.invoke({"tema": tema, "perfil": perfil})
            
            # Limpieza básica para asegurar que sea JSON válido
            response_text = response_text.strip()
            if response_text.startswith("```json"):
                response_text = response_text.replace("```json", "").replace("```", "")
            
            # Validar que es JSON parseable
            json_obj = json.loads(response_text)
            
            # Escribir en el archivo JSONL (una línea por objeto)
            f.write(json.dumps(json_obj, ensure_ascii=False) + "\n")
            
            print(f"[{i+1}/{NUM_EJEMPLOS}] Generado sobre: {tema}")
            
        except Exception as e:
            print(f"⚠️ Error en ejemplo {i+1}: {e}")

print(f"\n✅ Dataset guardado en {OUTPUT_FILE}")