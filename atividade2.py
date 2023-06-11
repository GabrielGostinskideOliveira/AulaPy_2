class Time:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores

    def adiciona_jogador(self, nome, camisa):
        jogador = [nome, camisa]
        self.jogadores.append(jogador)

    def imprime_jogadores(self):
        print(f'Lista de jogadores do time {self.nome}:')
        for jogador in self.jogadores:
            nome = jogador[0]
            camisa = jogador[1]
            print(f'Nome: {nome}, Camisa: {camisa}')


# Testando a classe Time
time = Time(nome='Time A', jogadores=[['1º Jogador', 5], ['2º Jogador', 10]])

time.imp_jogadores()
# Lista de jogadores do time Time A:
# Nome: Jogador 1, Camisa: 10
# Nome: Jogador 2, Camisa: 7

time.add_jogador('3º Jogador', 11)
time.add_jogador('4º Jogador', 20)
time.imp_jogadores()
# Lista de jogadores do time Time A:
# Nome: Jogador 1, Camisa: 10
# Nome: Jogador 2, Camisa: 7
# Nome: Jogador 3, Camisa: 9
# Nome: Jogador 4, Camisa: 11