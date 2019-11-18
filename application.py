from flask import Flask , render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
application = Flask(__name__)

# Database initial config
application.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(application)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return 



@application.route("/")
def index():
    # pending to change to jsonify 
    return render_template("index.html")
if __name__ == "__main__":
    application.debug = True
    application.run(host="0.0.0.0", port=5000, debug= True)