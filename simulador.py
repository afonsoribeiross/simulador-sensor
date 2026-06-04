import time
import random
from supabase import create_client

SUPABASE_URL = "https://kyzuskuyluiyuvwgwngo.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt5enVza3V5bHVpeXV2d2d3bmdvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA1MTg4OTcsImV4cCI6MjA5NjA5NDg5N30.vWH6-pbpBLZRd3XrF49h41vOTnHa1Nd1EtgVvM9110o"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

MAQUINA_ID = 3
temperatura_atual = 50.0

print("Simulador iniciado. Enviando leituras a cada 10 segundos...")
print("Pressione Ctrl+C para parar.")

while True:
    temperatura_atual += random.uniform(1, 3)
    
    status = "normal"
    if temperatura_atual >= 70:
        status = "alerta"
    if temperatura_atual >= 85:
        status = "falha"
    
    supabase.table("leituras").insert({
        "maquina_id": MAQUINA_ID,
        "temperatura": round(temperatura_atual, 1),
        "status": status
    }).execute()
    
    print(f"Leitura enviada: {round(temperatura_atual, 1)}°C — {status}")
    
    time.sleep(10)