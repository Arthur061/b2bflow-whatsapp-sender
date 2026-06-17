# b2bflow-whatsapp-sender

Lê contatos cadastrados no Supabase e envia mensagens personalizadas via Z-API.

---

## Pré-requisitos

- Python 3.11+
- Conta no [Supabase](https://supabase.com) (gratuito)
- Conta na [Z-API](https://z-api.io) (gratuito)

---

## Setup da tabela no Supabase

Crie uma tabela chamada `contatos` com as seguintes colunas:

| Coluna    | Tipo |
|-----------|------|
| id        | int8 |
| nome      | text |
| telefone  | text |

Insira até 3 contatos com o telefone no formato internacional: `5511999999999`

---

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```env
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_anon_key_here
ZAPI_INSTANCE_ID=your_zapi_instance_id_here
ZAPI_TOKEN=your_zapi_token_here
ZAPI_CLIENT_TOKEN=your_zapi_client_token_here
```

---

## Como rodar

```bash
# 1. Clone o repositório
git clone https://github.com/Arthur061/b2bflow-whatsapp-sender.git
cd b2bflow-whatsapp-sender

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate     # Linux/Mac

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o .env com suas credenciais

# 5. Execute
python main.py
```

---

## Exemplo de saída

```
2026-06-17 11:10:25 [INFO] Buscando contatos no Supabase...
2026-06-17 11:10:27 [INFO] 3 contato(s) encontrado(s).
2026-06-17 11:10:27 [INFO] Enviando mensagem para Arthur (5561999999999)...
2026-06-17 11:10:27 [INFO] Mensagem enviada com sucesso para Arthur!
```