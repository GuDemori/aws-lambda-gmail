# AWS Lambda Gmail — Envio de E-mails via Gmail API

Projeto de exemplo para disciplina de Arquitetura em Cloud:
Função Lambda AWS que envia e-mails usando a API do Gmail com autenticação OAuth2.

---

## Como funciona

- A função Lambda recebe como entrada: destinatário (`to`), assunto (`subject`) e corpo do e-mail (`body`)
- Utiliza as credenciais do Google Cloud (`credentials.json`) para autenticação OAuth2
- Envia o e-mail usando a Gmail API

---

## Passo a Passo para rodar

### 1. Crie um projeto no Google Cloud
- Ative a Gmail API
- Configure a Tela de permissão OAuth (tipo EXTERNO)
- Adicione seu e-mail como usuário de teste
- Baixe o `credentials.json`

### 2. Gere o token OAuth2 localmente

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
python get_token.py
