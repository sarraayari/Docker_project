#service vgg19


from flask import Flask, request, jsonify
import base64
import numpy as np
from keras.applications.vgg19 import VGG19, preprocess_input, decode_predictions
from keras.preprocessing import image

app = Flask(__name__)




@app.route('/classify_vgg19', methods=['POST'])
def classify_music_genre_vgg19():
#receiving data in json format
    data = request.get_json()
    if 'wav_music' in data:
        wav_base64 = data['wav_music']
#encoding data
        wav_data = base64.b64decode(wav_base64)
# Convert the WAV data to a format suitable for VGG19
        img = preprocess_input(wav_data)
        img = image.load_img(img, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        # Use your VGG19 model to classify the genre
        predictions = model.predict(img)
        predicted_labels = decode_predictions(predictions, top=1)[0][0][1]
#returning genra       
 return jsonify({'genre': predicted_labels})
    else:
        return jsonify({'error': 'Missing "wav_music" parameter'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
