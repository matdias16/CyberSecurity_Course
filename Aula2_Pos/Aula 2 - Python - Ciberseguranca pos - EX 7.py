# Coleções
# Dictionaries ou Map
# Conjunto de pares: chave e valor
# Não tem um índice númerico

filmes_assistidos = {
    "Parasita": 10,
    "Hellboy": 8.5,
    "Batman e Robin": 1.0
}

print(filmes_assistidos["Parasita"])
print(filmes_assistidos)
print(filmes_assistidos.keys())
print(filmes_assistidos.values())
print(filmes_assistidos.items())

for filme in filmes_assistidos:
    print(f"{filme}: {filmes_assistidos[filme]}")

print("=============================================")

filmes = {
    "Parasita": {
        "ano": 2019,
        "diretor": "Bong Joon-ho",
        "gênero": ["drama", "suspense"]
    },

    "Hellboy": {
        "ano": 2004,
        "diretor": "Guilherme Del Toro",
        "gênero": ["ação", "fantasia", "Super herói"],
        "detalhes": {
            "box office": 90000000
        }
    }
}

print(filmes["Parasita"])
print(filmes["Hellboy"]["detalhes"]["box office"])
