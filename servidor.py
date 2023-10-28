import base64
import io
from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS
import numpy as np
from joblib import load
import os
from modelController import getClassification

# Generar el servidor (Back End)
servidorWeb = Flask(__name__)

# Enable CORS for all routes
CORS(servidorWeb, resources={r"/*": {"origins": "*"}})

# Catalogo para el modelo de 8 productos
productMatrixCatalog = {
    0: 'La Perla Codo 2',
    1: 'Codo 4 La Moderna',
    2: 'Fideo 2 La Moderna',
    3: 'Harina de Trigo La Moderna',
    4: 'Sopa de Letras La Moderna',
    5: 'Sopa Dino Figuras La Moderna',
    6: 'Sopa Munición La Moderna',
    7: 'Spaghetti La Moderna'
}

def obtainProduct(imagen):
     # Hacer resize a la imagen 256x256
    imagen_a_evaluar = imagen.resize((256, 256))
    # Obtener la clasificación
    classification = getClassification(imagen_a_evaluar)
    return int(classification)

@servidorWeb.route("/classifyImage", methods=["POST"])
def upload():
    base64_data = request.json["imagen"]
    image_data = base64.b64decode(base64_data)
    imagen = Image.open(io.BytesIO(image_data))
    
    # Saves images
    # imagen.save("imagenActual/imagenActual.jpg")

    # Obtener la clasificación
    classification = obtainProduct(imagen)

    # Obtener el nombre del producto
    product = productMatrixCatalog[classification]

    return {"message": "ok", "producto": product, "clasificacion": classification}

if __name__ == "__main__":
    servidorWeb.run(debug=False, host="0.0.0.0", port="8083")
