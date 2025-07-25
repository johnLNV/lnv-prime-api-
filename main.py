from fastapi import FastAPI
from sympy import nextprime
import random

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "API LNV-Prime ativa. Use /gerar_primo?digitos=5"}

@app.get("/gerar_primo")
def gerar_primo(digitos: int = 5):
    numero = random.randint(10**(digitos-1), 10**digitos - 1)
    return {
        "numero_aleatorio": numero,
        "proximo_primo": nextprime(numero)
    }
