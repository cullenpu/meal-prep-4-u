from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

@app.route('/pantry')
def pantry():
    return render_template('pantry.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

# @app.route("/api/load", methods=['POST'])
# def get_recipes(ingredients):
#     return 0

if __name__ == '__main__':
    app.run(debug=False)
