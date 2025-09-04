class Pessoa:
    def __init__(self, nome, idade, interesses):
        self.nome = nome
        self.idade = idade
        self.interesses = interesses
        self.inspiracoes = []
        self.conquistas = []
        self.cabelo = "curto e simples"

    def adicionar_inspiracao(self, nova_inspiracao):
        """Adiciona uma nova inspiração à lista."""
        self.inspiracoes.append(nova_inspiracao)
        print(f"Nova inspiração adicionada: '{nova_inspiracao}'.")

    def adicionar_conquista(self, nova_conquista):
        """Adiciona uma nova conquista à lista."""
        self.conquistas.append(nova_conquista)
        print(f"Nova conquista adicionada: '{nova_conquista}'.")

    def evoluir_interesses(self, novo_interesse):
        """Adiciona um novo interesse à lista."""
        self.interesses.append(novo_interesse)
        print(f"Interesse evoluído para: '{novo_interesse}'.")

    def mudar_visual(self, novo_cabelo):
        """Muda o estilo do cabelo."""
        self.cabelo = novo_cabelo
        print(f"Estilo de cabelo atualizado para: '{self.cabelo}'.")

    def __str__(self):
        """Retorna uma representação em string do objeto."""
        return (f"--- Dados Atuais de {self.nome} ---\n"
                f"Idade: {self.idade} anos\n"
                f"Interesses: {', '.join(self.interesses)}\n"
                f"Inspirações: {', '.join(self.inspiracoes)}\n"
                f"Conquistas: {', '.join(self.conquistas)}\n"
                f"Cabelo: {self.cabelo}\n"
                "\n")

class Personalidade:
    def __init__(self, tipo, energia_inicial):
        self.tipo = tipo
        self.energia = energia_inicial
    
    def interagir_com_amigos(self, com_amigos):
        """Atualiza a energia com base na interação social."""
        if com_amigos:
            self.energia = "Alta"
            print("Energia aumentada ao interagir com amigos!")
        else:
            self.energia = "Normal"
            print("Energia retornou ao estado normal.")


print("----- Início da Jornada: Infância e Adolescência -----")
arthur = Pessoa("Arthur Sena", 7,["Jogos"])
arthur.adicionar_conquista("Aprender inglês com jogos e videos")
arthur.adicionar_inspiracao("Mãe")
arthur.adicionar_inspiracao("Pai")
print("\n")
print(arthur)

print("\n----- Transformação 1: Ensino Médio para a Faculdade -----")
arthur.idade = 12
arthur.evoluir_interesses("Animação, Ciclismo, Animes")
arthur.adicionar_conquista("Começar a estudar em um curso de Ingles")
arthur.mudar_visual("Deixando crescer")
print("\n")
print(arthur)




print("\n----- Transformação 2: Ensino Médio para a Faculdade -----")
arthur.idade = 17
arthur.evoluir_interesses("Computadores, Desenhar, Escrever")
arthur.adicionar_conquista("Concluir o Ensino Médio")
arthur.adicionar_conquista("Graduar em curso de Mecatronica")
arthur.adicionar_conquista("Graduar em curso de Ingles com a maior nota da escola")
arthur.adicionar_conquista("Começar Pos-graduação de curso de Ingles")
arthur.adicionar_conquista("Entrar na facauldade")
print("\n")
print(arthur)



print("\n----- Transformação 3: A Vida Atual -----")
arthur.adicionar_inspiracao("Etika")
arthur.adicionar_inspiracao("Jerma985")
arthur.mudar_visual("Top Flat")
arthur.idade = 20
arthur.adicionar_conquista("Concluir Pos-graduação de curso de Ingles")
print("\n")



print("\n--- Objeto Final de Arthur ---")
print(arthur)
