from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, request
from config import Config

db = SQLAlchemy()
migrate = Migrate()

import DataStruct

# http://127.0.0.1:5000/create_student?name=s1&number=1
def create_student():

    name = request.args.get('name')
    number = request.args.get('number')

    data = DataStruct.Student(name=name, number=number)

    db.session.add(data)
    db.session.commit()

    return f"""
    <h1>Hello ({number}){name}~</h1>
    """

# http://127.0.0.1:5000/create_task?id=1&name=國文&score=70
def create_task():

    id = request.args.get('id')
    name = request.args.get('name')
    score = request.args.get('score')

    data = DataStruct.TaskData(student_id=id, name=name, score=score)

    db.session.add(data)
    db.session.commit()

    return f"""
    <h1>Hello ({id}){name} => {score}</h1>
    """
def student_task(id):
    
    print(id)

    query = DataStruct.Student.query.filter_by(number=id).first()

    print(query.__dict__)
    
    content = ''

    print(query.task_data)

    for task in query.task_data:
        content += f"<p>{task.name} : {task.score} 分</p>"

    return content

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    app.add_url_rule('/create_student', 'create_student',
                     create_student, methods=['GET', 'POST'])
    app.add_url_rule('/create_task', 'create_task',
                     create_task, methods=['GET', 'POST'])
    app.add_url_rule('/student_task/<id>', 'student_task',
                     student_task, methods=['GET', 'POST'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
