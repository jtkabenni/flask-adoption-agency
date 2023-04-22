from flask import Flask, render_template, redirect 
from models import Pet, db, connect_db
from forms import AddPetForm

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "verysecret"
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)

@app.route("/")
def homepage():
    """Show list of all pets."""
    pets = Pet.query.all()

    return render_template("base.html", pets= pets)

@app.route("/pets/add", methods = ["GET", "POST"])
def add_pet():
    """Add new pet"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        image_url = form.image_url.data if form.image_url.data else None
        age = form.age.data if form.age.data else None
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name = name, species = species, image_url = image_url, age=age, notes=notes,available = available)

        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)

@app.route("/pets/<int:pet_id>")
def display_pet(pet_id):
    """Display detail page for pet"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet_details.html", pet = pet)


@app.route("/pets/<int:pet_id>/edit", methods = ["GET", "POST"])
def update_pet(pet_id):
    """ Edit pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.image_url = form.image_url.data if form.image_url.data else None
        pet.age = form.age.data if form.age.data else None
        pet.notes = form.notes.data
        pet.available = form.available.data
       
        db.session.commit()
        return redirect(f'/pets/{pet_id}')
    else:
        return render_template("add_pet_form.html", form=form)

@app.route("/pets/<int:pet_id>/delete", methods=["POST"])
def delete_tag(pet_id):
    """Delete pet"""
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    return redirect ('/')