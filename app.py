from flask import Flask, jsonify, request
import json

app = Flask(__name__)
devs = [
    {'nome':'Bruno',
     'habilidades':['C', 'Java']},
    {'nome':'Lairon',
     'habilidades':['Python', 'Flask', 'PHP', 'HTML5', 'CSS']},
    {'nome':'Luna',
     'habilidades':['CSS', 'HTML5', 'Bootstrap', 'JavaScript']}
]

@app.route("/dev/<int:id>", methods=["GET", "PUT"])
def dev(id):
    if request.method == "GET":
        registro = devs[id]
        return jsonify(registro)
    elif request.method == "PUT":
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)