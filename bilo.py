class Aluno:
    def __init__(self, matricula, nome, sexo, idade):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade


if __name__ == "__main__":
    aluno1 = Aluno("000081", "joao", "Homem", 16)
    print(aluno1.matricula,aluno1.nome,aluno1.sexo,aluno1.idade)