from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask deployed with Ansible, NGINX, and GitHub Actions!"
