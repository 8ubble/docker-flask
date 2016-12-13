from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='河北比众')

@app.route('/services')
def services():
    return render_template('services.html', title='河北比众')

@app.route('/rank')
def rank():
    return render_template('rank.html', title='河北比众')

@app.route('/plugins')
def plugins():
    return render_template('plugins.html', title='河北比众') 

@app.route('/apps')
def apps():
    return render_template('apps.html', title='河北比众')    

@app.route('/labs')
def labs():
    return render_template('labs.html', title='河北比众')    
    
@app.errorhandler(404)
def page_not_found():
	return render_template('404.html'), 404
	
if __name__ == '__main__':
    app.run(debug=True)