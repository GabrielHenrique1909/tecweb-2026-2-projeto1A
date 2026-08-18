import sqlite3
class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database():
    def __init__(self, nome):
        self.conn = sqlite3.connect(nome+'.db')
        command = """
        CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
                                            title TEXT,
                                            content TEXT NOT NULL );
        """
        self.conn.execute(command)
    
    def add(self, note:Note):
        command = f"INSERT INTO note (title,content) VALUES ('{note.title}','{note.content}');"
        self.conn.execute(command)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        notes = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id,title, content)
            notes.append(note)
        return notes
    
    def update(self, entry:Note):
        command = f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id}"
        self.conn.execute(command)
        self.conn.commit()
    def delete(self, note_id):
        command = f"DELETE FROM note WHERE id = {note_id}"
        self.conn.execute(command)
        self.conn.commit()
