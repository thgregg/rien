from flask import Flask, request, redirect
import json
from datetime import datetime
from waitress import serve

app = Flask(__name__)

def save_to_json(ip):
    log_entry = {str(datetime.now()): ip}
    with open('ip_log.json', 'a') as f:
        json.dump(log_entry, f)
        f.write('\n')

@app.route('/')
def get_client_ip():
    user_ip = request.remote_addr
    save_to_json(user_ip)
    return redirect('http://www.google.com')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
