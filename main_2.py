import sqlite3
from db.db_utils import *

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()
cursor.execute("""DROP TABLE IF EXISTS Estudantes""")

criar_tabela(conn)

estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022),
]

inserir_registros(conn, estudantes)
conn.commit()

cursor.execute("SELECT * FROM Estudantes WHERE AnodeIngresso BETWEEN 2019 AND 2020")
print(cursor.fetchall())

atualizar(conn, "Estudantes", "AnodeIngresso", "Nome", 2017, "Pedro Mendes")
consultar_registros(conn)

deletar(conn, "Estudantes", "ID", 4)
consultar_registros(conn)

cursor.execute("SELECT * FROM Estudantes WHERE AnodeIngresso > 2019 AND Curso = 'Computação'")
print(cursor.fetchall())

atualizar(conn, "Estudantes", "AnodeIngresso", "Curso", 2016, "Computação")
consultar_registros(conn)

conn.close()