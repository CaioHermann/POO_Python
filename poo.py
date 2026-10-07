end = False
class estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 6:
            return "Aprovado"
        elif self.media() >= 4:
            return "Exame"

        return "Reprovado"

    def descrever(self):
        return(f"{self.nome:-<16}{self.nota1:-<8}{self.nota2:-<8}"f"{self.media():-<8.1f}{self.situacao():-<14}")
    
estudantes = []

def cadastrar():
    try:
        nome = input(f"{"Insira o nome do estudante: ":^54}")
        nota1 = float(input(f"{"Insira a Nota 1: ":^54}"))
        nota2 = float(input(f"{"Insira a Nota 2: ":^54}"))
        estudantes.append(estudante(nome, nota1, nota2))
    except ValueError:
        print(f"\nErro, valor inválido, retornando ao menu...")
        return
    print("Estudante Cadastrado")

def listar():
    if not estudantes:
        print(f"{"Nenhum Estudante Cadastrado!":^54}")
        return
    print('='*54)
    print(f"{'Nome':-<16}{'Nota 1':-<8}{'Nota 2':-<8}{'Média':-<8}{'Situação':-<14}")
    for e in estudantes:
        print(e.descrever())


while end != True:
    print(f"{"Bem vindo!":=^54}\n\n [1] - Cadastrar Estudante \n [2] - Mostrar Estudantes \n [3] - Remover Estudante (WIP) \n [4] - Sair\n")
    try:
        opcao = int(input(f"{"="*54}\n{"Insira a opção desejada: ":^54}"))
    except ValueError:
        print(f"{"Erro: Opção inválida, Reiniciando...":54}")
        continue
    if opcao == 4:
        print(f"{"Saindo...":^54}")
        end = True
        break
    elif opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    
