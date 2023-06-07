from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Loading the .tflite model
interpreter = tf.lite.Interpreter(model_path='./model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load the class labels (replace with your own labels)
class_labels = ['bali', 'betawi', 'cendrawasih', 'jumputan', 'kawung', 'megamendung', 'parang', 'pekalongan', 'sekar', 'sidoluhur']

@app.route('/process-image', methods=['POST'])
def process_image():
    image_file = request.files['image']
    image = tf.image.decode_image(image_file.read(), channels=3)
    image = tf.image.resize(image, [300, 300])  # Resize to match the model's expected size
    image = image / 255.0
    image = tf.expand_dims(image, axis=0)

    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    predicted_class_index = np.argmax(output)
    predicted_class_label = class_labels[predicted_class_index]
    confidence = int(output[0][predicted_class_index] * 100)  # Convert to integer


    return jsonify({'predicted_class': predicted_class_label, 'confidence': confidence})

if __name__ == '__main__':
    app.run()
