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