from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'abc123'

@app.route('/')
def index():
    return render_template('index.html', message='Index')

@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'
    return render_template('index.html', message='Session data set.')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
    return render_template('index.html', message=f'Name:{name}, Other:{other}')

@app.route('/clear_session')
def clear_session():
    session.clear()
    # session.pop['name']
    return render_template('index.html', message='Session cleared.')

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie set.'))
    response.set_cookie(key='cookie_name', value='This is the cookie info')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message=f'Cookie Value:{cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message='Cookie removed.'))
    response.set_cookie(key='cookie_name', expires=0)
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'jacobhenry' and password == "abc123":
            flash('Successful Login')
            return render_template('index.html', message='')
        else:
            flash('Login Failed')
            return render_template('index.html', message='')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)