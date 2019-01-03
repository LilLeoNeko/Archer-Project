from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home') 
def home(name = None):
	return render_template('homePage.html', name = name)

@app.route('/login')
def login():
	return render_template('loginPage.html')

@app.route('/about')
def about():
	return render_template('aboutPage.html')

if __name__ == '__main__':
	app.run(debug = True)