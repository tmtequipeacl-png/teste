import requests
import schedule
import time

EVOLUTION_URL = "https://evolution-api-production-9b8c0.up.railway.app"
API_KEY = "065717adde59669b240bbdd91cf1300302b3ac3b799f44cba52d674c61b6630d"
INSTANCE_NAME = "empresaTMT"

DESTINATARIOS = "5519994418222"

def enviar_mensagem_whatsapp(destinatario, mensagem):
    """Função de envio para a versão atual da Evolution API"""
    url = f"{EVOLUTION_URL}/message/sendText/{INSTANCE_NAME}"
    headers = {
        "Content-Type": "application/json",
        "apikey": API_KEY
    }

    payload = {
        "number": destinatario,
        "text": mensagem,
        "options": {
            "delay": 1200,
            "presence": "composing"
        }
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in [200, 201]:
            print(f"[OK] Mensagem enviada com sucesso para {destinatario} às {time.strftime('%H:%M:%S')}")
            return True
        else:
            print(f"[ERRO] API respondeu com status {response.status_code} para {destinatario}: {response.text}")
            return False
    except Exception as e:
        print(f"[ERRO] Falha ao conectar na Evolution API para {destinatario}: {e}")
        return False

def job():
    print("\n--- Iniciando Disparo Automatizado ---")
    msg_teste = "Bom dia, mensagem teste para ver se esta tudo funcionando!"
    
    for grupo_id in DESTINATARIOS:
        enviar_mensagem_whatsapp(grupo_id, msg_teste)

schedule.every().tuesday.at("09:45").do(job)

print("=" * 60)
print("Robô de agendamento iniciado.")
print("Monitorando o relógio... Próximo disparo: Terça-Feira as 09:25.")
print("=" * 60)

while True:
    schedule.run_pending()
    time.sleep(30)
