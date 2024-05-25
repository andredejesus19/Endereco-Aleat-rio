import random

ruas = ["Rua das Flores", "Av. Paulista", "Rua Santa Clara", "Av. Atlântica", "Rua das Laranjeiras", "Av. Sete de Setembro", "Rua Augusta", "Av. Ipiranga", "Rua XV de Novembro", "Av. Batel", "Rua 24 de Outubro", "Av. Independência", "Rua dos Andradas", "Av. Cristóvão Colombo", "Rua João Alfredo"]
bairros = ["Jardim Primavera", "Bela Vista", "Copacabana", "Leme", "Centro", "Barra", "Consolação", "República", "Centro", "Batel", "Moinhos de Vento", "Independência", "Centro", "Floresta", "Cidade Baixa"]
cidades_estados = [("São Paulo", "SP"), ("Rio de Janeiro", "RJ"), ("Salvador", "BA"), ("Curitiba", "PR"), ("Porto Alegre", "RS")]

def gerar_cep():
    return f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"

enderecos = []
for i in range(2000):
    rua = random.choice(ruas)
    numero = random.randint(1, 2000)
    bairro = random.choice(bairros)
    cidade, estado = random.choice(cidades_estados)
    cep = gerar_cep()
    endereco = f"{rua}, {numero}, {bairro}, {cidade} - {estado}, {cep}"
    enderecos.append(endereco)

with open("enderecos.txt", "w") as f:
    for endereco in enderecos:
        f.write(endereco + "\n")
