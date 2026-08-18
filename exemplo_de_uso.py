from database import Database, Note

db = Database('banco')

db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
db.add(Note(title=None, content='Lembrar de tomar água'))

notes = db.get_all()
print("pegando todas \n")

for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')

new_note = Note(2, "Aviso", 'Lembrar de tomar água')
db.update(new_note)

notes = db.get_all()
print("atualizando a 2 \n")
for note in notes:

    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')
db.delete(1)
notes = db.get_all()
print("apagando a 1 \n")
for note in notes:
    
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')
    db.delete(note.id)