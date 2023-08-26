import logging
from flask import Flask, jsonify, request
from flask_healthz import healthz
from utils.app_logging import init_logging

app = Flask(__name__)
init_logging()
app.register_blueprint(healthz, url_prefix="/healthz")
# Healthz(app, no_log=True)
logger = logging.getLogger()

@app.route('/', methods=['GET'])
def get_pub_ip():
    try:
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            return jsonify({'my public ip': request.environ['REMOTE_ADDR']}), 200
        else:
            return jsonify({'my public ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200
    except Exception as ex:
        logger.exception(ex)
        return jsonify({'error': 'error fetching public ip address'}), 500

def liveness():
    pass

def readiness():
    pass

app.config.update(
    HEALTHZ = {
        "live": "app.liveness",
        "ready": "app.readiness",
    }
)

if __name__ == '__main__':
    app.run(debug=True)
