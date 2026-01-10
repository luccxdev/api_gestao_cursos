from marshmallow import Schema, fields


class CursoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    descricao = fields.Str()
    carga_horaria = fields.Int(required=True)


class CursoSchemaUpdate(Schema):
    nome = fields.Str()
    descricao = fields.Str()
    carga_horaria = fields.Int()
