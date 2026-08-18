from urllib.parse import unquote_plus

from utils import load_data, load_template, add_note, build_response

def index(request):
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            # AQUI É COM VOCÊ
            chave,valor = chave_valor.split('=',1)
            params[chave] = unquote_plus(valor)
            print(params)

        # Adiciona a nova anotação ao arquivo JSON
        add_note(params['titulo'], params['detalhes'])
        response = build_response(code=303, reason='See Other', headers='Location: /')
    else:
        response = build_response()

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return response + load_template('index.html').format(notes=notes).encode()