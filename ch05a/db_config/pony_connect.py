from pony.orm import Database

db = Database(
    "postgres",
    host="localhost",
    port="5432",
    user="postgres",
    password="secret",
    database="fcms",
)
