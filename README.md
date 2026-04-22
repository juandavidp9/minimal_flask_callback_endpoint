# TikTok OAuth Callback (Flask)

Minimal Flask app to handle TikTok OAuth authorization and retrieve an access token.
This service is required to capture the authorization code via a public HTTPS callback URL.

---

## 🚀 Overview

TikTok's API requires an OAuth flow. This app provides a lightweight backend to:

* Receive the authorization code from TikTok
* Exchange it for an access token
* Enable further API calls (e.g., insights, comments)

---

## 🧩 Tech Stack

* Python (Flask)
* python-dotenv
* requests

---

## ⚙️ Environment Variables

Create a `.env` file:

```
CLIENT_KEY=your_client_key
CLIENT_SECRET=your_client_secret
REDIRECT_URI=https://your-domain.vercel.app/auth/callback/
```

---

## ▶️ Run Locally

### Create and activate virtual environment

```
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the app

```
python app.py
```
