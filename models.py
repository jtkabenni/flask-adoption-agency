from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
default_img = "https://media.istockphoto.com/id/1306543850/photo/tabby-cat-and-border-collie-dog.jpg?s=612x612&w=0&k=20&c=4Wvu33FedVyMrWsVI7PO3DG34kmb7qTi6wKLtqzSvfM="

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)

    species = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=True, default = default_img)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(500), nullable = True)
    available = db.Column(db.Boolean, nullable = False, default = True)