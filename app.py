from flask import Flask, render_template,request,redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['CHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/todoapp'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
        __tablename__ = 'todo'
        id = db.Column(db.Integer,primary_key=True)
        description = db.Column(db.String(),nullable=False)
        completed = db.Column(db.Boolean, nullable=False,default=False)

        def __repr__(self):
                return f'<Todo ID={self.id} DESC={self.description}>'

@app.route('/')
def index():
        return render_template('index.html', data = Todo.query.all())

@app.route('/todos/create', methods=['POST'])
def create_todo():
        description = request.get_json()['description']
        todo = Todo(description = description)
        db.session.add(todo)
        db.session.commit()

        return jsonify({
                'id':todo.id,
                'description':todo.description
        })

if __name__ == "__main__":
    app.debug = True
    app.run()