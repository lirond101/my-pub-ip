import logging
from flask import Flask, jsonify, request
from utils.app_logging import init_logging
from db import check_db_connection, get_ip_data, create_ip_data
import ifcfg
import datetime

app = Flask(__name__)

logger = init_logging()
# logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def get_pub_ip():
    try:
        # app.logger.debug(request.headers)
        # logger.debug(request.headers)
        # logger.debug(get_ip_data().ips_as_map())
        # logger.debug(type(get_ip_data().ips_as_map()))
        # print(request.headers)
        ip_address = ""
        if request.environ.get('HTTP_X_FORWARDED_FOR'):
            if ',' in request.environ.get('HTTP_X_FORWARDED_FOR'):
                result = request.environ['HTTP_X_FORWARDED_FOR'][:request.environ['HTTP_X_FORWARDED_FOR'].index(',')-1]
            ip_address = request.environ['HTTP_X_FORWARDED_FOR']
        else:
            ip_address = request.environ['REMOTE_ADDR']
        
        create_ip_data(datetime.datetime.now(), ip_address)
        return jsonify({'my public ip': ip_address}), 200 
    except Exception as ex:
        logger.exception(ex)
        return jsonify({'error': 'error fetching public ip address'}), 500

@app.route('/history', methods=['GET'])
def get_history():
    try:
        return jsonify(get_ip_data()), 200
    except Exception as ex:
        logger.exception(ex)
        return jsonify({'error': 'error fetching ips history because ' + str(ex)}), 500

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
