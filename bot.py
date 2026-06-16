import requests
import schedule
import time

EVOLUTION_URL = "https://evolution-api-production-9b8c0.up.railway.app"
API_KEY = "8A58085775DA-4D12-B187-18C3E350C89C"
INSTANCE_NAME = "empresaTMT"

DESTINATARIO_UNICO = "5519994418222"

def enviar_mensagem_whatsapp(destinatario, mensagem):
    """Função de envio correta para a Evolution API v2"""
    url = f"{EVOLUTION_URL}/message/sendText/{INSTANCE_NAME}"
    headers = {
        "Content-Type": "application/json",
        "apikey": API_KEY
    }

    payload = {
        "number": destinatario,
        "options": {
            "delay": 1200,
            "presence": "composing"
        },
        "textMessage": {
            "text": mensagem
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in [200, 201]:
            print(f"[OK] Mensagem enviada com sucesso para {destinatario} às {time.strftime('%H:%M:%S')}")
            return True
        else:
            print(f"[ERRO] API respondeu com status {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print(f"[ERRO] Falha ao conectar na Evolution API: {e}")
        return False

def job():
    print("\n--- Iniciando Disparo Automatizado ---")
    msg_teste = "Bom dia, mensagem teste para ver se esta tudo funcionando!"
    
    enviar_mensagem_whatsapp(DESTINATARIO_UNICO, msg_teste)

schedule.every().tuesday.at("13:50").do(job)

print("=" * 60)
print("Robô de agendamento iniciado com sucesso!")
print(f"Monitorando... Destinatário: {DESTINATARIO_UNICO}")
print("=" * 60)

while True:
    print(f"[Status] Robô ativo. Horário do Servidor: {time.strftime('%H:%M:%S')}")
    schedule.run_pending()
    time.sleep(10)
