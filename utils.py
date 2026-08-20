from pathlib import Path
import json

def extract_route(request):
    lista = request.split()
    route = lista[1]
    return route[1:]

def read_file(filepath):
    opened_file = open(filepath, 'rb')
    return opened_file.read()

def load_data(nome):
    path = "data/" + nome
    opened_file = open(path, 'r')
    return json.load(opened_file)

def load_template(nome):
    path = "templates/" + nome
    opened_file = open(path, 'r')
    read = opened_file.read()
    return read

def add_note(titulo, detalhes):
    path = "data/notes.json"
    opened_file = open(path, 'r')
    data = json.load(opened_file)
    opened_file.close()

    data.append({"titulo": titulo, "detalhes": detalhes})

    opened_file = open(path, 'w')
    json.dump(data, opened_file)
    opened_file.close()

def build_response(body="", code=200, reason="OK", headers=""):
    if headers != "":
        headers = "\n" + headers
    return f"HTTP/1.1 {code} {reason}{headers}\n\n{body}".encode()