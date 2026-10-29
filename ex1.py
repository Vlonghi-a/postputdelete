from flask import Flask, jsonify, request
app=Flask(__name__)

id=0
filmesDB=[]

@app.route("/filmes")
def verFilmes():
    return jsonify(filmesDB)


@app.route("/filmes", methods=["POST"])
def enviarFilmes():
    global id
    dados=request.get_json()
    
    nome=dados.get("nome")
    diretor=dados.get("diretor")
    ano=dados.get("ano")
    
    filme={"id": id, "nome": nome, "diretor": diretor, "ano": ano}
    id+=1
    
    filmesDB.append(filme)
    return jsonify(filme), 201

@app.route("/filmes/<int:id>", methods=["PUT"])
def alterarFilme(id):
    dados=request.get_json()
    
    for f in filmesDB:
        if id==f["id"]:
            f['nome']=dados.get("nome")
            f['diretor']=dados.get("diretor")
            f['ano']=dados.get("ano")
            return jsonify(f), 200
    
    return jsonify({"erro": "filme não encontrado"}), 404

@app.route("/filmes/<int:id>", methods=["DELETE"])
def deletarFilme(id):
    for f in filmesDB:
        if id==f["id"]:
            filmesDB.remove(f)
            return jsonify(filmesDB), 200
        
    return jsonify({"erro": "filme não encontrado"}), 404

app.run(debug=True)
    
    