from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Lista para guardar posições temporariamente
coordenadas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/localizacao', methods=['POST'])
def receber_localizacao():
    dados = request.get_json()

    latitude = dados.get('latitude')
    longitude = dados.get('longitude')
    accuracy = dados.get('accuracy')

    if latitude is not None and longitude is not None:
        coordenadas.append({
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": accuracy
        })
        return jsonify({"status": "sucesso"}), 200
    else:
        return jsonify({"erro": "Dados incompletos"}), 400

@app.route('/coordenadas')
def listar_coordenadas():
    return jsonify(coordenadas)


if __name__ == "__main__":
    app.run(debug=True)
