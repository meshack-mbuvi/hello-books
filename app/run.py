from flask import Flask, render_template

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def home():
  return render_template('designs/UI/index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	return render_template('designs/UI/index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	#After sign in, redirect user to user page
	return render_template('designs/UI/user.html')

if __name__ == '__main__':
	app.run(debug=True)