from flask import Flask, request
from models import Pet, Base, Breed
from database import engine, Session
from flask import jsonify
from schemas import PetModelOut, PetModelIn, BreedModelIn, BreedModelOut
from typing import Optional, List


app = Flask("pets")


@app.before_request
def before_request():
    Base.metadata.create_all(engine)

@app.route("/petstore_api/pets/", methods=["GET", "POST"])
def pets():
    """
    Создаёт и возвращает {id:int, name:str, breed_name:str}
    или
    возвращает List[{id:int, name:str, breed_name:str}]
    """
    if request.method == "GET":
        session = Session()
        query = session.query(Pet).all()
        pets_list = []

        for line in query:
            pet = PetModelOut(**line.as_dict()).dict()
            breed_id = int(session.query(Pet.breed_id).filter_by(id=pet['id']).first()[0])
            pet['breed_name'] = session.query(Breed.name).filter_by(id=breed_id).first()[0]
            pets_list.append(pet)
        return jsonify(pets_list)

    else:
        session = Session()
        request_json = request.get_json()
        breed_id =request_json['breed_id']
        new_pet = PetModelIn(name=request_json['name'], breed_id=request_json['breed_id'])
        new_pet = Pet(name=new_pet.name, breed_id=breed_id)
        session.add(new_pet)
        session.commit()
        validate_answer = PetModelOut(id=new_pet.id, name=new_pet.name).dict()
        session.close()

        return jsonify(validate_answer)


@app.route("/petstore_api/breeds/", methods=["GET", "POST"])
def breeds():
    """
    Создаёт и возвращает {id:int, name:str, breed_name:str}
    или
    возвращает List[{id:int, name:str, breed_name:str}]
    """
    if request.method == "GET":
        session = Session()
        query = session.query(Breed).all()
        breeds_list = []

        for line in query:
            breeds = BreedModelOut(**line.as_dict()).dict()
            breeds_list.append(breeds)
        return jsonify(breeds_list)

    else:
        request_json = request.get_json()
        name = BreedModelIn(name=request_json['name'])
        session = Session()
        new_breed = Breed(name=name.name)
        session.add(new_breed)
        session.commit()
        validate_answer = BreedModelOut(id=new_breed.id, name=new_breed.name).dict()
        session.close()

        return jsonify(validate_answer)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)

