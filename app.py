
from flask import Flask, request, jsonify
from flask_cors import CORS
from rag import chatting  # Hanya import fungsi yang diperlukan

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_question = data.get('message', '').strip()
    
    if not user_question:
        return jsonify({"error": "Pesan tidak boleh kosong"}), 400
    
    try:
        response_text = chatting(user_question)
        return jsonify({"reply": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8080)