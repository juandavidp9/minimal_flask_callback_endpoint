from flask import Flask, request
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)

CLIENT_KEY = os.getenv("CLIENT_KEY")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

@app.route("/auth/callback/")
def callback():
    print("FULL URL:", request.url)
    print("ARGS:", request.args)

    code = request.args.get("code")
    error = request.args.get("error")

    if error:
        return f"OAuth error: {error}", 400

    if not code:
        return "Missing authorization code", 400

    return f"Code received: {code}"

@app.route("/")
def home():
    return "TikTok OAuth demo is running"

if __name__ == "__main__":
    app.run(port=5000, debug=True)