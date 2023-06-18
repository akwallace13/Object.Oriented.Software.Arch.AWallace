from flask import FLASK
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#create instance
app = Flask(__name__)

#add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'

#initialize database
db = SQLAlchemy(app)

#model creation
class Items(db.model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.Integer, nullable=False)
    item = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    #create string
    def __repr__(self):
        return '<Item %r>' % self.name
    

    