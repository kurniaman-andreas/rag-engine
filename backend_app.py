from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_openai import initialize_chatbot, chatting  

app = Flask(__name__)
CORS(app)  # izinkan akses dari Next.js (port 3000)

# Inisialisasi chatbot saat Flask dijalankan
initialize_chatbot()

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"reply": "Pesan kosong tidak dapat diproses."}), 400

    try:
        response = chatting(user_input)
        return jsonify({"reply": response})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"reply": "Maaf, terjadi kesalahan saat memproses."}), 500

if __name__ == "__main__":
    app.run(port=8080, debug=True)
