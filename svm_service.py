#service svm


from flask import Flask, request, jsonify
import base64
import numpy as np
from sklearn.svm import SVC

app = Flask(__name__)

# Load your SVM model here
# model = SVC()

@app.route('/classify_svm', methods=['POST'])
def classify_music_genre_svm():
#receiving json data
    data = request.get_json()
    if 'wav_music' in data:
        wav_base64 = data['wav_music']
#encoding data in base 64
wav_data = base64.b64decode(wav_base64)

        genre = "Rock"
#returning genra of the music 
 return jsonify({'genre': genre})
    else:
        return jsonify({'error': 'Missing "wav_music" parameter'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
