from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')



@app.route('/')
def index():
    mylist = [1, 2, 3, 4, 5, 6]
    return render_template(template_name_or_list='index.html', mylist=mylist)

@app.route('/other')
def other():
    return render_template(template_name_or_list='other.html', some_text="Some text")

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.template_filter('alternate_case')
def repeat(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)


