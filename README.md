# API de Gestão de Cursos

## Descrição

API REST desenvolvida com **Flask** para gestão de cursos com operações CRUD em memória.

## Estrutura

```
.
├── app.py              # Aplicação principal
├── db.py               # Banco de dados em memória
├── requirements.txt    # Dependências
├── blueprints/        # Blueprints da API
│   └── curso.py       # Endpoints de cursos
└── schemas/           # Validação de dados
    └── curso.py       # Schema do curso
```

## Instalação

```bash
pip install -r requirements.txt
```

## Executar

```bash
python app.py
```

API disponível em `http://localhost:5000`

## Endpoints

- `GET /` - Documentação da API
- `GET /cursos` - Listar todos
- `POST /cursos` - Criar novo
- `GET /cursos/<id>` - Obter por ID
- `PUT /cursos/<id>` - Atualizar
- `DELETE /cursos/<id>` - Deletar

## Exemplo de uso

```bash
# Criar curso
curl -X POST http://localhost:5000/cursos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Python", "carga_horaria": 40}'

# Listar
curl http://localhost:5000/cursos
```
