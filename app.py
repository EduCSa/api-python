from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Livro 1',
        'autor': 'Autor 1',
    },
    {
        'id': 2,
        'título': 'Livro 2',
        'autor': 'Autor 2',
    },
    {
        'id': 3,
        'título': 'Livro 3',
        'autor': 'Autor 3',
    },
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)


@app.route('/livros',methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            print("retorno",livro)
            return jsonify(livro)
        
              
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for livro in livros:
        if livro.get('id') == id: 
            livro['título'] = livro_alterado.get('título')
            livro['autor'] = livro_alterado.get('autor')
            livro['id'] = livro_alterado.get('id')
            
            return jsonify(livro)
    return jsonify({'error': 'Livro não encontrado'}), 404
        

@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
        return jsonify(livros)       
    

app.run(port=5000, host='localhost',debug=True)   