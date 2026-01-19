# schemas/professor.py
from marshmallow import Schema, fields


class ProfessorSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    especialidade = fields.Str(required=True)


class ProfessorUpdateSchema(Schema):
    nome = fields.Str()
    especialidade = fields.Str()
