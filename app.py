from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_pub_ip():
    ip_address = ''
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip_address = request.environ['REMOTE_ADDR']
    else:
        ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    return '<h1>{}</h2>'.format(ip_address), 200

if __name__ == '__main__':
    app.run(debug=True)
