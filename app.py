from flask import Flask, render_template, request
import random

app = Flask(__name__)

COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'white', 'orange']

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        guess = request.form.get('color')
        actual = random.choice(COLORS)
        if guess == actual:
            message = f"Correct! It was {actual}."
        else:
            message = f"Wrong! It was {actual}."
    return render_template('index.html', colors=COLORS, message=message)

if __name__ == "__main__":
    app.run(debug=True)
