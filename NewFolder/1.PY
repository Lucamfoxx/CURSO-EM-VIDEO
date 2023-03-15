from blessed import Terminal

# Inicializa o terminal Blessed
term = Terminal()

# Define as dimensões da janela do jogo
LARGURA_JANELA = 80
ALTURA_JANELA = 24

# Cria a janela do jogo
with term.fullscreen(), term.cbreak():
    with term.location():
        print(term.clear)
        print(term.move_y(ALTURA_JANELA//2-1) + term.center("Jogo de Xadrez"))