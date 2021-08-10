import pdb
from models.staff import Staff
import repositories.staff_repository as staff_repository

staff_repository.delete_all()

new_staff_member = Staff("Zookeepy McGhee", "01/01/2002", "Penguins", 3)

staff_repository.add_staff_member(new_staff_member)

pdb.set_trace()