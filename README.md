# 🐶 Best Friend Backend

API desenvolvida em Django para consumir dados de uma API externa de raças de cachorros, normalizar as informações e armazená-las em banco de dados SQL.

A aplicação realiza sincronização automática dos dados, disponibilizando uma API própria para consulta das raças cadastradas.

## ⚙️ Decisões Técnicas

### 🌐 Consumo da API externa com Requests

A biblioteca requests foi utilizada para realizar as conexões com a API externa devido à sua simplicidade e legibilidade.

Isso permitiu implementar facilmente:

- 🔄 paginação;
- 📡 múltiplas requisições;
- 🔑 autenticação via headers;
- ⚠️ tratamento de erros.

### 🗄️ Uso do PostgreSQL/Supabase

O projeto utiliza PostgreSQL hospedado no Supabase.

A escolha foi feita por:

- 🚀 boa performance;
- 🔒 confiabilidade;
- ☁️ hospedagem gratuita;
- 🧩 integração simples com Django.

### 🆔 Uso de UUID

Foi utilizado UUID como identificador principal dos registros para:

- 🔒 evitar IDs previsíveis;
- 🌐 melhorar compatibilidade com APIs públicas;
- 📦 facilitar futuras integrações.

## ☁️ Deploy

O deploy da aplicação foi realizado utilizando:

- Render
- Supabase

## 📋 Requisitos

- ✅ Python instalado.
- ✅ pip instalado.
- ✅ PostgreSQL/Supabase configurado.
- ✅ Chave da API de cachorros.

## 🚀 Como Rodar Localmente

### 1️⃣ Clone o repositorio:

```bash
git clone https://github.com/kakeiko/Best-Friend-Back.git
cd Best-Friend-Back
```

### 2️⃣ Crie um ambiente virtual:
#### Windows
```bash
python -m venv .venv
```

Ative o ambiente:
```bash
.venv\Scripts\activate
```

### 3️⃣ Instale as dependencias:
```bash
pip install -r requirements.txt
```
### 4️⃣ Crie um arquivo .env na raiz do projeto:
```env
API_LINK_INFO=
API_KEY=

SECRET_KEY=

DEBUG=True
```

Exemplo de `API_LINK_INFO`:
```env
API_LINK_INFO=https://api.thedogapi.com/v1/breeds
```
#### 📌 Como gerar uma SECRET_KEY

Execute o comando abaixo no terminal:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Exemplo de saída:
```
django-insecure-4r9@2f#8m2...
```

#### 📌 Adicione no arquivo .env
```.env
SECRET_KEY=sua_secret_key
```

### 5️⃣ Execute as migrations:
```bash
python manage.py migrate
```
### 6️⃣ Rode o servidor:
```bash
python manage.py runserver
```
### 7️⃣ Acesse a API:
```
http://127.0.0.1:8000/
```
## 📡 Endpoint
### Buscar todas as raças
```html
GET /breed/
```