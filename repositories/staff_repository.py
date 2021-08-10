from db.run_sql import run_sql
from models.staff import Staff

def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)

def add_staff_member(staff):
    sql = "INSERT INTO staff (name, start_date, department, performance_rating) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [staff.name, staff.start_date, staff.department, staff.performance_rating]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff.id = id
    return staff

def select_all_staff():
    staff_members = []
    sql = "SELECT * FROM staff"
    results = run_sql(sql)
    for row in results:
        staff = Staff(row['name'], row['start_date'], row['department'], row['performance_rating'], row['id'])
        staff_members.append(staff)

    return staff_members

def find_staff_member_name(name):
    staff_member = None

    sql = "SELECT * FROM staff WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]
    if result is not None:
        staff_member = Staff(result['name'], result['start_date'], result['department'], result['performance_rating'], result['id'])

    return staff_member


def remove_staff_member(name):
    sql = "DELETE FROM staff WHERE name = %s"
    values = [name]
    run_sql(sql, values)

def update_staff_member(staff):
    sql = "UPDATE staff SET (name, start_date, department, performance_rating) = (%s, %s, %s, %s)"
    values = [staff.name, staff.start_date, staff.department, staff.performance_rating]
    run_sql(sql, values)