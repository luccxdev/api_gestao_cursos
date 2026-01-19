# API de Gestão de Cursos

## Descrição

API REST desenvolvida com **Flask** para gestão de cursos e professores com operações CRUD em **banco de dados SQLite** usando **Flask-SQLAlchemy**.

## Estrutura

```
.
├── app.py                  # Aplicação principal
├── db.py                   # Configuração do banco de dados
├── requirements.txt        # Dependências
├── models/                 # Modelos do banco de dados
│   ├── __init__.py
│   ├── curso.py            # Modelo de Curso
│   └── professor.py        # Modelo de Professor  
├── resource/               # Recursos da API (flask-smorest)
│   ├── __init__.py
│   ├── curso.py            # Endpoints de cursos
│   └── professor.py        # Endpoints de professores
└── schemas/                # Validação de dados com Marshmallow
    ├── __init__.py
    ├── curso.py            # Schema do curso
    └── professor.py        # Schema do professor
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

### Professores
- `GET /professores` - Listar todos os professores
- `POST /professores` - Criar novo professor
- `GET /professores/<id>` - Obter professor por ID
- `PUT /professores/<id>` - Atualizar professor
- `PATCH /professores/<id>` - Atualizar parcialmente
- `DELETE /professores/<id>` - Deletar professor

### Cursos
- `GET /` - Documentação da API
- `GET /cursos` - Listar todos os cursos
- `POST /cursos` - Criar novo curso
- `GET /cursos/<id>` - Obter curso por ID
- `PUT /cursos/<id>` - Atualizar curso
- `PATCH /cursos/<id>` - Atualizar parcialmente
- `DELETE /cursos/<id>` - Deletar curso

## Exemplo de uso

```bash
# Criar um professor
curl -X POST http://localhost:5000/professores \\
  -H "Content-Type: application/json" \\
  -d '{"nome": "Dr. João Silva", "especialidade": "Engenharia de Software"}'

# Criar curso vinculado ao professor (professor_id 1)
curl -X POST http://localhost:5000/cursos \\
  -H "Content-Type: application/json" \\
  -d '{"nome": "Python Avançado", "carga_horaria": 40, "professor_id": 1}'

# Listar todos os cursos
curl http://localhost:5000/cursos

# Listar todos os professores
curl http://localhost:5000/professores
```
