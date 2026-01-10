# API de Gestão de Cursos

## Descrição

API RESTful desenvolvida com Flask para gestão de cursos. Implementa operações CRUD (Create, Read, Update, Delete) com dados armazenados em memória utilizando listas e dicionários Python.

**Tema da Atividade:** Gestão de Cursos  
**Instituição:** BFD - Bolsa Futuro Digital  
**Turma:** 07 RJ - C1 2025-2

---

## Recursos

✅ Listar todos os cursos  
✅ Criar novo curso  
✅ Obter curso por ID  
✅ Atualizar informações do curso  
✅ Deletar curso  
✅ Validação de dados obrigatórios  
✅ Respostas em formato JSON  
✅ Códigos de status HTTP apropriados  

---

## Instalação

### Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/luccxdev/api_gestao_cursos.git
cd api_gestao_cursos
```

### Passo 2: Instalar Flask

```bash
pip install flask
```

### Passo 3: Executar a API

```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

---

## Endpoints da API

### 1. Listar Todos os Cursos

**Método:** `GET`  
**Rota:** `/cursos`  
**Status:** `200 OK`

**Exemplo de Requisição:**

```bash
curl -X GET http://localhost:5000/cursos
```

**Resposta:**

```json
[
  {
    "id": 1,
    "nome": "Python Avançado",
    "descricao": "Curso de programação em Python",
    "instrutor": "João Silva"
  },
  {
    "id": 2,
    "nome": "Web Development",
    "descricao": "Desenvolvimento web com Flask",
    "instrutor": "Maria Santos"
  }
]
```

---

### 2. Criar Novo Curso

**Método:** `POST`  
**Rota:** `/cursos`  
**Status:** `201 Created`  
**Content-Type:** `application/json`

**Campos Obrigatórios:**
- `nome` (string) - Nome do curso

**Campos Opcionais:**
- `descricao` (string) - Descrição do curso
- `instrutor` (string) - Nome do instrutor

**Exemplo de Requisição:**

```bash
curl -X POST http://localhost:5000/cursos \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "JavaScript Básico",
    "descricao": "Introdução ao JavaScript",
    "instrutor": "Pedro Costa"
  }'
```

**Resposta (Sucesso):**

```json
{
  "id": 3,
  "nome": "JavaScript Básico",
  "descricao": "Introdução ao JavaScript",
  "instrutor": "Pedro Costa"
}
```

**Resposta (Erro - Campo obrigatório faltando):**

```json
{
  "erro": "Nome do curso é obrigatório"
}
```

Status: `400 Bad Request`

---

### 3. Obter Curso por ID

**Método:** `GET`  
**Rota:** `/cursos/<id>`  
**Status:** `200 OK` ou `404 Not Found`

**Parâmetro:**
- `id` (integer) - ID do curso

**Exemplo de Requisição:**

```bash
curl -X GET http://localhost:5000/cursos/1
```

**Resposta (Sucesso):**

```json
{
  "id": 1,
  "nome": "Python Avançado",
  "descricao": "Curso de programação em Python",
  "instrutor": "João Silva"
}
```

**Resposta (Erro - Curso não encontrado):**

```json
{
  "erro": "Curso não encontrado"
}
```

Status: `404 Not Found`

---

### 4. Atualizar Curso

**Método:** `PUT`  
**Rota:** `/cursos/<id>`  
**Status:** `200 OK` ou `404 Not Found`  
**Content-Type:** `application/json`

**Campos Opcionais:**
- `nome` (string) - Nome do curso
- `descricao` (string) - Descrição do curso
- `instrutor` (string) - Nome do instrutor

**Exemplo de Requisição:**

```bash
curl -X PUT http://localhost:5000/cursos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Python Avançado - Atualizado",
    "instrutor": "João Silva Junior"
  }'
```

**Resposta (Sucesso):**

```json
{
  "id": 1,
  "nome": "Python Avançado - Atualizado",
  "descricao": "Curso de programação em Python",
  "instrutor": "João Silva Junior"
}
```

---

### 5. Deletar Curso

**Método:** `DELETE`  
**Rota:** `/cursos/<id>`  
**Status:** `200 OK` ou `404 Not Found`

**Parâmetro:**
- `id` (integer) - ID do curso a ser deletado

**Exemplo de Requisição:**

```bash
curl -X DELETE http://localhost:5000/cursos/1
```

**Resposta (Sucesso):**

```json
{
  "mensagem": "Curso deletado",
  "curso": {
    "id": 1,
    "nome": "Python Avançado",
    "descricao": "Curso de programação em Python",
    "instrutor": "João Silva"
  }
}
```

**Resposta (Erro - Curso não encontrado):**

```json
{
  "erro": "Curso não encontrado"
}
```

Status: `404 Not Found`

---

## Estrutura do Projeto

```
api_gestao_cursos/
├── app.py           # Arquivo principal da API
├── README.md        # Documentação do projeto
└── .gitignore      # Arquivos a ignorar no Git
```

---

## Tecnologias Utilizadas

- **Python 3.7+** - Linguagem de programação
- **Flask** - Framework web minimalista
- **JSON** - Formato de dados
- **Git** - Controle de versão

---

## Fluxo de Desenvolvimento

Este projeto foi desenvolvido seguindo as boas práticas de controle de versão, com um commit para cada rota implementada:

1. ✅ `feat: implementa rota GET /cursos` - Listar todos os cursos
2. ✅ `feat: implementa rota POST /cursos` - Criar novo curso
3. ✅ `feat: implementa rota GET /cursos/<id>` - Obter curso por ID
4. ✅ `feat: implementa rota PUT /cursos/<id>` - Atualizar curso
5. ✅ `feat: implementa rota DELETE /cursos/<id>` - Deletar curso

---

## Exemplo Completo de Uso

```bash
# 1. Iniciar a API
python app.py

# 2. Criar um curso
curl -X POST http://localhost:5000/cursos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Python", "instrutor": "Prof. João"}'

# 3. Listar todos os cursos
curl -X GET http://localhost:5000/cursos

# 4. Obter curso específico
curl -X GET http://localhost:5000/cursos/1

# 5. Atualizar curso
curl -X PUT http://localhost:5000/cursos/1 \
  -H "Content-Type: application/json" \
  -d '{"nome": "Python Avançado"}'

# 6. Deletar curso
curl -X DELETE http://localhost:5000/cursos/1
```

---

## Notas Importantes

⚠️ **Os dados são armazenados em memória**, o que significa que todos os dados serão perdidos quando a aplicação for reiniciada.

Para uma aplicação em produção, seria recomendado usar um banco de dados como SQLite, PostgreSQL ou MongoDB.

---

## Autor

**Luccas** - Desenvolvedor

---

## Licença

Este projeto é fornecido como atividade educacional da BFD - Bolsa Futuro Digital.


## Arquitetura v2.0 - Blueprints, Schemas e OpenAPI

Esta versão refatorada implementa boas práticas de desenvolvimento de APIs:

### 1. **Blueprints (Modularização)**

A API está organizada em **blueprints** do Flask-RESTX:

```
recursos/
├── __init__.py
└── curso.py      # Blueprint dos endpoints de cursos
```

Cada blueprint é um **Namespace** que organiza endpoints relacionados.

### 2. **Schemas (Validação de Dados)**

Usamos **Marshmallow** para validação de entrada e saída:

```
schemas/
├── __init__.py
└── curso.py      # CursoSchema e CursoSchemaUpdate
```

**Validations:**
- `nome`: Obrigatório, string de 1-100 caracteres
- `descricao`: Opcional, máximo 500 caracteres
- `carga_horaria`: Obrigatório, inteiro > 0

### 3. **OpenAPI/Swagger (Documentação)**

A API implementa **OpenAPI 3.0** automáticamente:

**Acessar documentação:**
```
http://localhost:5000/docs
```

**Recurso da OpenAPI:**
- ✓ Documentação interativa em Swagger UI
- ✓ Models e schemas definidos
- ✓ Status HTTP e mensagens de erro documentados
- ✓ Testes diretos da interface

## Estrutura do Projeto

```
api_gestao_cursos/
├── app.py                  # Main application
├── db.py                   # In-memory database
├── requirements.txt        # Dependencies
├── README.md              # Documentation
├── recursos/
│   ├── __init__.py        # Blueprint package
│   └── curso.py           # Curso endpoints (GET, POST, PUT, DELETE)
└── schemas/
    ├── __init__.py        # Schema package
    └── curso.py           # CursoSchema & CursoSchemaUpdate
```

## Instalação e Execução

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar aplicativo

```bash
python app.py
```

A API estará disponível em `http://localhost:5000/api/v1`

### 3. Acessar Swagger UI

```
http://localhost:5000/docs
```

## Dependencias

- **Flask 3.0.0** - Framework web
- **Flask-RESTX 0.5.1** - REST API com OpenAPI/Swagger
- **Marshmallow 3.20.1** - Serialização e validação de dados
- **Python-dotenv 1.0.0** - Variáveis de ambiente

## Melhorias Implementadas

### vs Versão Anterior

| Aspecto | v1.0 | v2.0 |
|--------|------|------|
| Organização | Monolítica | Blueprints |
| Validação | Nenhuma | Marshmallow |
| Documentação | Manual | OpenAPI/Swagger |
| Escalabilidade | Baixa | Alta |
| Manutenção | Difícil | Fácil |
