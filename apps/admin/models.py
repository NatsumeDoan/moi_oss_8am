from apps import db,app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
        
with app.app_context():
    db.create_all()