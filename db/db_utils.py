def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Estudantes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Curso TEXT NOT NULL,
        AnodeIngresso INTEGER
    );
    """)
    conn.commit()

def inserir_registros(conn, estudantes):
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Estudantes (Nome, Curso, AnodeIngresso)
    VALUES (?, ?, ?);
    """, estudantes)
    conn.commit()

def consultar_registros(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Estudantes")
    print(cursor.fetchall())

def atualizar(conn, tabela, atualizar, identificador, novo, nome_iden):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {tabela} SET {atualizar} = ? WHERE {identificador} = ?", (novo, nome_iden))
    conn.commit()

def deletar(conn, tabela, identificador, nome_deletar):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {tabela} WHERE {identificador} = ?", (nome_deletar,))
    conn.commit()