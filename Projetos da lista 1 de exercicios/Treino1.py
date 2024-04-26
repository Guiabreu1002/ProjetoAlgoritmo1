import tkinter as tk
def obter_input():
    texto_digitado = entrada.get()
    label_resultado.config(text="Texto digitado: " + texto_digitado)

# Criando a janela
janela = tk.Tk()
janela.title("Interface para Digitar")

# Criando um rótulo
label_instrucao = tk.Label(janela, text="Digite algo:")
label_instrucao.pack()

# Criando uma entrada de texto
entrada = tk.Entry(janela)
entrada.pack()

# Criando um botão para confirmar o texto digitado
botao_confirmar = tk.Button(janela, text="Confirmar", command=obter_input)
botao_confirmar.pack()

# Criando um rótulo para exibir o texto digitado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Loop principal da janela
janela.mainloop()