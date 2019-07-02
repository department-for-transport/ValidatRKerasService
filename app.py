from flask import Flask
from flask import request
from flask import jsonify
import json
import keras
import numpy
import pandas
import tensorflow as tf
import config

#load model
model = keras.models.load_model('model.h5')
graph = tf.get_default_graph()
classes = ['Cycle', 'HGV','LGV','car', 'largecar']

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
    parameters = request.json
    
    X = pandas.DataFrame.from_dict(parameters,orient='index').values
    X = tf.keras.utils.normalize(X)
    with graph.as_default():
        predictions = model.predict(X)
    predictions = numpy.argmax(predictions, axis=1)

    
    
    class_list = [classes[prediction] for prediction in predictions]


    class_json = json.dumps({ i : class_list[i] for i in range(0, len(class_list) ) })
    
    return jsonify(class_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)