# SocioFlu Login Bot

Este projeto é um script em Python que automatiza o login no site [sociofutebol.com.br](https://sociofutebol.com.br/), utilizando Selenium WebDriver. 

## Funcionalidades
- Acessa o site sociofutebol.com.br
- Verifica se o usuário já está logado
- Realiza logout se necessário
- Efetua login automaticamente com as credenciais fornecidas

## Pré-requisitos
- Python 3.8 ou superior
- Google Chrome instalado
- Git (opcional, para clonar o repositório)

## Instalação

1. **Clone o repositório (ou baixe os arquivos):**

```bash
git clone https://github.com/seu-usuario/socioflu-login-bot.git
cd socioflu-login-bot
```

2. **Crie e ative um ambiente virtual (recomendado):**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo (ou copie o exemplo):

```bash
cp .env.example .env
```

Edite o arquivo `.env` e coloque seu usuário e senha:

```
USERNAME=seu_usuario
PASSWORD=sua_senha
```

## Como usar

Execute o script com:

```bash
python login_bot.py
```

O script irá:
- Acessar o site
- Fazer logout se já estiver logado
- Realizar o login com as credenciais fornecidas

## Execução automática com cron

Se quiser rodar o script automaticamente em horários programados, utilize o cron do Linux:

1. Descubra o caminho do Python do seu ambiente virtual:

```bash
which python
```

2. Edite o crontab:

```bash
crontab -e
```

3. Adicione uma linha para rodar o script, por exemplo, todos os dias às 8h:

```
0 8 * * * /caminho/para/seu/venv/bin/python /caminho/para/socioflu-login-bot/login_bot.py >> /caminho/para/socioflu-login-bot/logs/script.log 2>&1
```

> Lembre-se de ajustar os caminhos conforme sua instalação.

## Observações
- Não compartilhe seu arquivo `.env` com outras pessoas.
- O script pode precisar de ajustes caso o site mude o layout ou os seletores dos campos de login.
- Para depuração, consulte o arquivo de log em `logs/script.log`.

---

Feito com ❤️ para automatizar o acesso ao Sócio Futebol (e ganhar os pontos de sócio).
