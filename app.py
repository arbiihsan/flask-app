from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Arbi\'s Flask App',
        'status': 'running',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/api/info')
def info():
    """Application information endpoint"""
    return jsonify({
        'app': 'Arbi\'s Flask DevOps Demo',
        'version': APP_VERSION,
        'environment': ENVIRONMENT,
        'timestamp': datetime.utcnow().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
