from db.run_sql import run_sql
from models.staff import Staff

def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)