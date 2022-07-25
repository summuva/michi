from crypt import methods
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from requests import request

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database/tuki.db'
db= SQLAlchemy(app)
class Tuki(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    content= db.Column(db.String(200))
    done= db.Column(db.Boolean)


@app.route('/') 
def home():
    tareas= Tuki.query.all()
    return render_template ('index.html', tareas=tareas)

@app.route(('/create-task'), methods=['POST'])
def create():
    tuki= Tuki(content=request.form['content'],done=False)
    db.session.add(tuki)
    db.session.commit()
    return'saved'

if __name__ == '__main__':    
    app.run(debug=True)