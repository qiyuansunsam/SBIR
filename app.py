from flask import Flask, request, jsonify, render_template_string
import tensorflow as tf
import numpy as np
import os
app = Flask(__name__)
from tensorflow.keras.models import load_model
image_encoder = load_model('models/image_encoder.keras')
sketch_encoder = load_model('models/sketch_encoder.keras')
retrieval_model = load_model('models/retrieval_model.keras')

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_FORM)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        #TODO change such that it gets the sketch
        sketch = request.form["input"]
        
        sketch_emb = sketch_encoder.predict(sketch)
        predicted_img_emb = retrieval_model.predict(sketch_emb)

        #TODO retrieve using predicted embeddings
        return jsonify({
            "input": input_values.tolist(),
            "prediction": predictions.tolist()
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)