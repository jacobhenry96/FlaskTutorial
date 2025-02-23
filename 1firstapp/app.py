from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/hello')
def hello():
    response = make_response('Hello World')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return "Hello World", 200

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add( number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.ketys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting} {name}'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)