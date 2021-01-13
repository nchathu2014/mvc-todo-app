from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/todoapp'

db = SQLAlchemy(app)

class Todo(db.Model):
        __tablename__ = 'todo'
        id = db.Column(db.Integer,primary_key=True)
        description = db.Column(db.String(),nullable=False)

        def __repr__(self):
                return f'<Todo ID={self.id} DESC={self.description}>'

db.create_all()       

@app.route('/')
def index():
        return render_template('index.html', data = Todo.query.all())

if __name__ == "__main__":
    app.debug = True
    app.run()