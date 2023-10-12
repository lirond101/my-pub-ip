import logging
from flask import Flask, jsonify, request
from utils.app_logging import init_logging
from db import check_db_connection
import ifcfg

app = Flask(__name__)

logger = init_logging()
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def get_pub_ip():
    try:
        app.logger.debug(request.headers)
        logger.debug(request.headers)
        print(request.headers)
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            return jsonify({'my public ip': request.environ['REMOTE_ADDR']}), 200
        elif ',' in request.environ.get('HTTP_X_FORWARDED_FOR'):
            return jsonify({'my public ip': request.environ['HTTP_X_FORWARDED_FOR'][:request.environ['HTTP_X_FORWARDED_FOR'].index(',')-1]}), 200
        else:
            return jsonify({'my public ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200
    except Exception as ex:
        logger.exception(ex)
        return jsonify({'error': 'error fetching public ip address'}), 500


@app.route('/network', methods=['GET'])
def get_network_ip():
    try:
        return jsonify(ifcfg.interfaces()), 200
    except Exception as ex:
        logger.exception(ex)
        return jsonify({'error': 'error fetching network details because ' + str(ex)}), 500

@app.route('/healthz', methods=['GET'])
def health_check():
    return jsonify({'status': 200, 'app': 'OK', 'db': check_db_connection()}), 200

if __name__ == '__main__':
    app.run(debug=True)
