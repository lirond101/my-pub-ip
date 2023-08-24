from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_pub_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR'], 200
    else:
        return request.environ['HTTP_X_FORWARDED_FOR'], 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
