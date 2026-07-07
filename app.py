from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    data = request.get_json()
    message = data["message"].lower()

    if "hello" in message:
        reply = "Hello! How can I help you today?"
    elif "price" in message:
        reply = "Our pricing starts from ₹999."
    elif "bye" in message:
        reply = "Goodbye! Have a nice day."
    else:
        reply = "I'm an AI Customer Support Bot. Ask me anything!"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
