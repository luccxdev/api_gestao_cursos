# schemas/curso.py
from marshmallow import Schema, fields


class CursoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    carga_horaria = fields.Int(required=True)


class CursoUpdateSchema(Schema):
    nome = fields.Str()
    carga_horaria = fields.Int()
