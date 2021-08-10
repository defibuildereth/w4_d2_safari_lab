from db.run_sql import run_sql
from models.animal import Animal

def delete_all_animals():
    sql = "DELETE FROM animals"
    run_sql(sql)

def add_animal(animal):
    sql = "INSERT INTO animals (name, species, age) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.species, animal.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def select_all_animals():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for row in results:
        animal = Animal(row['name'], row['species'], row['age'], row['id'])
        animals.append(animal)

    return animals

def find_animal_name(name):
    animal = None

    sql = "SELECT * FROM animals WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]
    if result is not None:
        animal = Animal(result['name'], result['species'], result['age'], result['id'])

    return animal


def remove_animal_by_name(name):
    sql = "DELETE FROM animals WHERE name = %s"
    values = [name]
    run_sql(sql, values)

def update_animal(animal):
    sql = "UPDATE animals SET (name, species, age) = (%s, %s, %s)"
    values = [animal.name, animal.species, animal.age]
    run_sql(sql, values)