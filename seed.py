from models import Pet, db 
from app import app

db.drop_all()
db.create_all()

oscar = Pet(name = "Oscar", species = "dog", age = 5, notes = "I am a very cuddly boy. ")
pumpkin = Pet(name = "Pumpkin", species = "cat", age = 14)

db.session.add_all([oscar, pumpkin])

db.session.commit()
