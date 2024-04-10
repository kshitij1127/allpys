from flask import Flask, jsonify, request
from classifier import get_prediction
import numpy as np 

app = Flask(__name__)

@app.route("/predict-digit", methods=["POST"])
def predict_data():
  # image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image = request.files.get("digit")
  # use request function to get the file from digit key
  prediction = get_prediction(image)
  # calling the function and storing in prediction variable
  return jsonify({
    "prediction": prediction
  }), 200

if __name__ == "__main__":
  # prevents certain code from being run when imported 
  app.run(debug=True)

  # mvc architecture -> model view controller architecture
