import logging
from flask import Flask, jsonify, request
from utils.app_logging import init_logging

def create_app() -> Flask:
    init_logging()
    app = Flask(__name__)

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

    @app.route('/healthz', methods=['GET'])
    def health_check():
        return jsonify({'status': 200, 'title': 'OK'}), 200
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
