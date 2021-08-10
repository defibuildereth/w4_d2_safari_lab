from db.run_sql import run_sql
from models.animal import Animal
import repositories.staff_repository as staff_repository

def delete_all_animals():
    sql = "DELETE FROM animals"
    run_sql(sql)

def add_animal(animal):
    sql = "INSERT INTO animals (name, species, age, staff) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.species, animal.age, animal.staff]
    results = run_sql(sql, values)
    print(results)
    id = results[0]
    animal.id = id
    return animal

def select_all_animals():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for row in results:
        staff = staff_repository.find_staff_member_name(row['staff'])
        animal = Animal(row['name'], row['species'], row['age'], staff, row['id'])
        animals.append(animal)

    return animals

def find_animal_name(name):
    animal = None

    sql = "SELECT * FROM animals WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]
    if result is not None:
        animal = Animal(result['name'], result['species'], result['age'], result['staff'], result['id'])

    return animal


def remove_animal_by_name(name):
    sql = "DELETE FROM animals WHERE name = %s"
    values = [name]
    run_sql(sql, values)

def update_animal(animal):
    sql = "UPDATE animals SET (name, species, age) = (%s, %s, %s)"
    values = [animal.name, animal.species, animal.age]
    run_sql(sql, values)