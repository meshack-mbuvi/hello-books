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
	return render_template('designs/UI/index.html')

if __name__ == '__main__':
	app.run(debug=True)