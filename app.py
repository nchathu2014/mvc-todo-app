from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
        return render_template('index.html', data = [
                {'description':'ToDo-1'},
                {'description':'ToDo-2'},
                {'description':'ToDo-3'}
        ])

if __name__ == "__main__":
    app.debug = True
    app.run()