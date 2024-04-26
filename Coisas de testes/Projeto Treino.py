import tkinter as tk

class JogoXadrez(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Jogo de Xadrez")
        self.geometry("1000x1000")

        self.criar_tabuleiro()

    def criar_tabuleiro(self):
        self.tabuleiro = tk.Canvas(self, width=400, height=400)
        self.tabuleiro.pack()

        # Desenha o tabuleiro de xadrez
        cor = "white"
        for linha in range(8):
            for coluna in range(8):
                x0 = coluna * 50
                y0 = linha * 50
                x1 = x0 + 50
                y1 = y0 + 50
                self.tabuleiro.create_rectangle(x0, y0, x1, y1, fill=cor)
                cor = "white" if cor == "black" else "black"
            cor = "white" if cor == "black" else "black"

        # Adiciona peças de teste (apenas como exemplo)
        self.tabuleiro.create_text(25, 25, text="♔", font=("Arial", 24))
        self.tabuleiro.create_text(75, 25, text="♕", font=("Arial", 24))
        self.tabuleiro.create_text(125, 25, text="♖", font=("Arial", 24))
        self.tabuleiro.create_text(175, 25, text="♗", font=("Arial", 24))
        self.tabuleiro.create_text(225, 25, text="♘", font=("Arial", 24))
        self.tabuleiro.create_text(275, 25, text="♙", font=("Arial", 24))

    def iniciar(self):
        self.mainloop()

if __name__ == "__main__":
    app = JogoXadrez()
    app.iniciar()