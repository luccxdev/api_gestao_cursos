from marshmallow import Schema, fields, validate

class CursoSchema(Schema):
    """Schema para validação de dados de Cursos"""
    
    id = fields.Int(dump_only=True)
    nome = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=100),
        error_messages={
            'required': 'O campo nome é obrigatório',
            'invalid': 'O nome deve ser uma string'
        }
    )
    descricao = fields.Str(
        allow_none=True,
        validate=validate.Length(max=500)
    )
    carga_horaria = fields.Int(
        required=True,
        validate=validate.Range(min=1),
        error_messages={
            'required': 'A carga horária é obrigatória',
            'invalid': 'A carga horária deve ser um número inteiro'
        }
    )
    
class CursoSchemaUpdate(Schema):
    """Schema para atualização de cursos"""
    
    nome = fields.Str(validate=validate.Length(min=1, max=100))
    descricao = fields.Str(allow_none=True, validate=validate.Length(max=500))
    carga_horaria = fields.Int(validate=validate.Range(min=1))
