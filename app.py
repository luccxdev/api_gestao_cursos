"""
API de Gestão de Cursos
Desenvolvida com Flask para gerenciar cursos de forma simples e eficiente.

Autor: Luccas
Data: Dezembro 2025
Versão: 2.0
"""

from flask import Flask, jsonify, request

# Inicializa a aplicação Flask
app = Flask(__name__)

# Lista global para armazenar cursos em memória
cursos = []


# ============================================================================
# ROTA GET - Listar todos os cursos
# ============================================================================
@app.route('/cursos', methods=['GET'])
def listar_cursos():
    """
    Lista todos os cursos cadastrados no sistema.
    
    Retorna:
        JSON: Lista com todos os cursos
        int: Código HTTP 200 (OK)
    """
    return jsonify(cursos), 200


# ============================================================================
# ROTA POST - Criar novo curso
# ============================================================================
@app.route('/cursos', methods=['POST'])
def criar_curso():
    """
    Cria um novo curso no sistema.
    
    Campos esperados (JSON):
        nome (obrigatório): Nome do curso
        descricao (opcional): Descrição detalhada do curso
        instrutor (opcional): Nome do professor/instrutor
    
    Retorna:
        JSON: Dados do curso criado
        int: Código HTTP 201 (Criado) ou 400 (Erro)
    """
    dados_requisicao = request.get_json()
    
    # Valida se o nome do curso foi fornecido
    if not dados_requisicao or 'nome' not in dados_requisicao:
        mensagem_erro = {
            "erro": "O nome do curso é obrigatório para criar um novo curso.",
            "dica": "Envie um JSON com o campo 'nome'"
        }
        return jsonify(mensagem_erro), 400
    
    # Cria um novo dicionário com os dados do curso
    novo_curso = {
        "id": len(cursos) + 1,
        "nome": dados_requisicao['nome'].strip(),
        "descricao": dados_requisicao.get('descricao', '').strip(),
        "instrutor": dados_requisicao.get('instrutor', '').strip()
    }
    
    # Adiciona o curso à lista
    cursos.append(novo_curso)
    
    resposta = {
        "mensagem": f"Curso '{novo_curso['nome']}' criado com sucesso!",
        "curso": novo_curso
    }
    
    return jsonify(resposta), 201


# ============================================================================
# ROTA GET - Obter curso por ID
# ============================================================================
@app.route('/cursos/<int:id>', methods=['GET'])
def obter_curso(id):
    """
    Busca um curso específico pelo seu ID.
    
    Parâmetro:
        id (int): ID único do curso
    
    Retorna:
        JSON: Dados do curso encontrado
        int: Código HTTP 200 (OK) ou 404 (Não encontrado)
    """
    for curso in cursos:
        if curso['id'] == id:
            return jsonify(curso), 200
    
    mensagem_erro = {
        "erro": f"Nenhum curso encontrado com ID {id}.",
        "dica": "Verifique se o ID está correto"
    }
    return jsonify(mensagem_erro), 404


# ============================================================================
# ROTA PUT - Atualizar curso
# ============================================================================
@app.route('/cursos/<int:id>', methods=['PUT'])
def atualizar_curso(id):
    """
    Atualiza os dados de um curso existente.
    
    Parâmetro:
        id (int): ID único do curso
    
    Campos que podem ser atualizados (JSON):
        nome (opcional): Novo nome do curso
        descricao (opcional): Nova descrição
        instrutor (opcional): Novo instrutor
    
    Retorna:
        JSON: Dados do curso atualizado
        int: Código HTTP 200 (OK) ou 404 (Não encontrado)
    """
    dados_atualizacao = request.get_json()
    
    # Procura o curso e o atualiza
    for curso in cursos:
        if curso['id'] == id:
            # Atualiza apenas os campos fornecidos
            if 'nome' in dados_atualizacao:
                curso['nome'] = dados_atualizacao['nome'].strip()
            if 'descricao' in dados_atualizacao:
                curso['descricao'] = dados_atualizacao['descricao'].strip()
            if 'instrutor' in dados_atualizacao:
                curso['instrutor'] = dados_atualizacao['instrutor'].strip()
            
            resposta = {
                "mensagem": f"Curso '{curso['nome']}' atualizado com sucesso!",
                "curso": curso
            }
            return jsonify(resposta), 200
    
    mensagem_erro = {
        "erro": f"Nenhum curso encontrado com ID {id}.",
        "dica": "Verifique se o ID está correto"
    }
    return jsonify(mensagem_erro), 404


# ============================================================================
# ROTA DELETE - Deletar curso
# ============================================================================
@app.route('/cursos/<int:id>', methods=['DELETE'])
def deletar_curso(id):
    """
    Remove um curso do sistema.
    
    Parâmetro:
        id (int): ID único do curso a ser removido
    
    Retorna:
        JSON: Informação sobre a deleção
        int: Código HTTP 200 (OK) ou 404 (Não encontrado)
    """
    for indice, curso in enumerate(cursos):
        if curso['id'] == id:
            curso_deletado = cursos.pop(indice)
            resposta = {
                "mensagem": f"Curso '{curso_deletado['nome']}' removido do sistema com sucesso!",
                "curso_removido": curso_deletado
            }
            return jsonify(resposta), 200
    
    mensagem_erro = {
        "erro": f"Nenhum curso encontrado com ID {id}.",
        "dica": "Verifique se o ID está correto"
    }
    return jsonify(mensagem_erro), 404


# ============================================================================
# Executa a aplicação
# ============================================================================
if __name__ == '__main__':
    # Modo debug ativado para desenvolvimento
    # Em produção, configure como False
    app.run(debug=True, port=5000)
