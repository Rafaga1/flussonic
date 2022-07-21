from flask import Flask, request
from models import Pet, Base
from database import engine, Session
from flask import jsonify
from schemas import PetModelOut, PetModelIn


app = Flask("pets")


@app.before_request
def before_request():
    Base.metadata.create_all(engine)

@app.route("/petstore_api/pets/", methods=["GET", "POST"])
def pets():
    if request.method == "GET":
        session = Session()
        query = session.query(Pet).all()
        pets_list = []

        for line in query:
            pet = PetModelOut(**line.as_dict()).dict()
            pets_list.append(pet)
        return jsonify(pets_list)

    else:
        request_json = request.get_json()
        name = PetModelIn(name=request_json['name'])
        session = Session()
        new_pet = Pet(name=name.name)
        session.add(new_pet)
        session.commit()
        validate_answer = PetModelOut(id= new_pet.id, name= new_pet.name).dict()
        session.close()

        return jsonify(validate_answer)



if __name__ == '__main__':

    app.run(debug=True)

