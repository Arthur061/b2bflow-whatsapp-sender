import os
import logging
import requests
from dotenv import load_dotenv
from supabase import create_client

# Configuração de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")


def buscar_contatos():
    logging.info("Buscando contatos no Supabase...")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    response = supabase.table("contatos").select("*").limit(3).execute()
    logging.info(f"{len(response.data)} contato(s) encontrado(s).")
    return response.data


def enviar_mensagem(telefone: str, nome: str):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    headers = {
        "Content-Type": "application/json",
        "client-token": ZAPI_CLIENT_TOKEN
    }
    payload = {
        "phone": telefone,
        "message": f"Olá, {nome} tudo bem com você?"
    }

    logging.info(f"Enviando mensagem para {nome} ({telefone})...")
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        logging.info(f"Mensagem enviada com sucesso para {nome}!")
    else:
        logging.error(f"Erro ao enviar para {nome}: {response.status_code} - {response.text}")


def main():
    contatos = buscar_contatos()

    if not contatos:
        logging.warning("Nenhum contato encontrado no banco.")
        return

    for contato in contatos:
        enviar_mensagem(contato["telefone"], contato["nome"])


if __name__ == "__main__":
    main()