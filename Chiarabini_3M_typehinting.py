import random
def descrizione(nome: str, eta : int) -> str:
    return f"{nome} ha {eta} anni."


def numero_casuale() -> int:
    return random.randint(0, 99)



def descrizione_eta_casuale(nome: str) -> str:
    eta= numero_casuale()
    return descrizione(nome, eta)


def descrizione_casuale() -> str:
    nomi=["pippo", "pluto", "paperino", "paperone" ,"minnie"]
    nome=random.choice(nomi)
    eta=numero_casuale()
    return descrizione(nome,eta)

print(descrizione("pippo",23))
print(numero_casuale())
print(descrizione_eta_casuale("pippo"))
print(descrizione_casuale())
