import pdb
from models.staff import Staff
import repositories.staff_repository as staff_repository

staff_repository.delete_all()

new_staff_member = Staff("Zookeepy McGhee", "01/01/2002", "Penguins", 3)
new_staff_member1 = Staff("Catriona loves penguinas", "23/07/2021", "Tigers", 4)

staff_repository.add_staff_member(new_staff_member)
staff_repository.add_staff_member(new_staff_member1)

staff_repository.remove_staff_member("Zookeepy McGhee")

new_staff_member1.update_rating(2)
staff_repository.update_staff_member(new_staff_member1)

pdb.set_trace()