from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index(title=None):
    return render_template('index.html', title='河北比众')
def header():
	return render_template('header.html',)

if __name__ == '__main__':
    app.run(debug=True)