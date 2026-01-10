# Schema para validação de dados

def validar_curso(dados):
    """
    Valida os dados de um curso
    Retorna (validado, erros)
    """
    erros = []
    
    # Validar nome
    if 'nome' not in dados:
        erros.append('Nome é obrigatório')
    elif not isinstance(dados['nome'], str) or len(dados['nome']) == 0:
        erros.append('Nome deve ser uma string não vazia')
    
    # Validar descricao (opcional)
    if 'descricao' in dados:
        if not isinstance(dados['descricao'], str):
            erros.append('Descrição deve ser uma string')
    
    # Validar carga_horaria
    if 'carga_horaria' not in dados:
        erros.append('Carga horária é obrigatória')
    elif not isinstance(dados['carga_horaria'], int) or dados['carga_horaria'] <= 0:
        erros.append('Carga horária deve ser um número inteiro positivo')
    
    return len(erros) == 0, erros
