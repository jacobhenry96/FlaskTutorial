from flask import Flask, render_template, session

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'abc123'

@app.route('/')
def index():
    return render_template('index.html', message='Index')

@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'
    render_template('index.html', message='Session data set.')







if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)