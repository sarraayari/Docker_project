from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify_music_genre():
    data = request.get_json()
    result = {'genre': 'Classical'} 
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
