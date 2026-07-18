from flask import Flask, request, redirect
import secrets

app = Flask(__name__)

clients = {
    "my_client": {
        "redirect_uri": "http://localhost:3000/callback"
    }
}


@app.route("/")
def home():
    return "OAuth server works!"


@app.route("/authorize")
def authorize():
    client_id = request.args.get("client_id")
    redirect_uri = request.args.get("redirect_uri")
    state = request.args.get("state")

    if client_id not in clients:
        return "Unknown client", 400

    if clients[client_id]["redirect_uri"] != redirect_uri:
        return "Invalid redirect URI", 400

    code = secrets.token_urlsafe(16)

    return f"""
Authorization successful!<br>
Code: {code}<br>
State: {state}
"""


if __name__ == "__main__":
    app.run(debug=True)