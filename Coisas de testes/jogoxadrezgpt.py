import pygame
import sys
from pygame.locals import *

# Inicialização do Pygame
pygame.init()

# Definição de variáveis para as dimensões da janela
WIDTH, HEIGHT = 800, 600
BOARD_SIZE = 8
SQUARE_SIZE = HEIGHT // BOARD_SIZE

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Tamanho da borda
BORDER = 20

# Classe para representar uma peça de xadrez
class Piece:
    def __init__(self, color, image):
        self.color = color
        self.image = image

# Classe para representar o tabuleiro de xadrez
class Board:
    def __init__(self):
        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.initialize_board()

    def initialize_board(self):
        # Peões
        for col in range(BOARD_SIZE):
            self.board[1][col] = Piece(BLACK, "peao_preto.png")
            self.board[6][col] = Piece(WHITE, "peao_branco.png")
        # Torres
        self.board[0][0] = Piece(BLACK, "torre_preto.png")
        self.board[0][7] = Piece(BLACK, "torre_preto.png")
        self.board[7][0] = Piece(WHITE, "torre_branco.png")
        self.board[7][7] = Piece(WHITE, "torre_branco.png")
        # Outras peças...

    def draw(self, screen):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if (row + col) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board[row][col]
                if piece:
                    screen.blit(pygame.image.load(piece.image), (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Função para obter a posição do mouse no tabuleiro
def get_mouse_position(mouse_pos):
    row = mouse_pos[1] // SQUARE_SIZE
    col = mouse_pos[0] // SQUARE_SIZE
    return row, col

# Função principal
def main():
    # Configuração da janela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Xadrez")

    # Tabuleiro
    board = Board()

    # Loop principal do jogo
    running = True
    while running:
        screen.fill(WHITE)
        board.draw(screen)

        # Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    row, col = get_mouse_position(mouse_pos)
                    print("Clique na posição:", row, col)

        # Atualização da tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()