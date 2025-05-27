import tkinter as tk
from tkinter import messagebox
from weather import get_weather
from PIL import Image, ImageTk

def draw_vertical_gradient(canvas, width, height, color1, color2):
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)

    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'
        canvas.create_line(0, i, width, i, fill=color)

def iniciar_interface():
    largura = 370
    altura = 800

    janela = tk.Tk()
    janela.title("ClimaCode")
    janela.geometry(f"{largura}x{altura}")
    janela.resizable(False, False)

    canvas = tk.Canvas(janela, width=largura, height=altura, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    draw_vertical_gradient(canvas, largura, altura, "#5BA1E1", "#1E5ECE" )

    imagem = Image.open("assets/logo.png")
    imagem = imagem.resize((131, 160))
    logo = ImageTk.PhotoImage(imagem)
    canvas.create_image(largura//2, 220, image=logo)


    bloco = tk.Frame(janela, bg="white", bd=0)
    canvas.create_window(largura//2, 500, window=bloco, width=320, height=260) 
    
    # # Imagem do globo
    # imagem = Image.open("assets/earth.png")
    # imagem = imagem.resize((150, 150))
    # globo = ImageTk.PhotoImage(imagem)
    # canvas.create_image(largura//2, 220, image=globo)

    # Entrada e botões (em cima do canvas)
    entrada_label = tk.Label(janela, text="Busque por uma cidade", font=("Arial", 12, "bold"), bg="#5BA1E1", fg="white")
    entrada_label_window = canvas.create_window(largura//2, 320, window=entrada_label)

    entrada_cidade = tk.Entry(janela, width=30, font=("Arial", 12))
    entrada_window = canvas.create_window(largura//2, 350, window=entrada_cidade)

    def buscar():
        cidade = entrada_cidade.get()
        resultado = get_weather(cidade)
        if "erro" in resultado:
            messagebox.showerror("Erro", resultado["erro"])
        else:
            clima = f"""
Temperatura: {resultado['temperatura']}°C
Umidade: {resultado['umidade']}%
Descrição: {resultado['descricao']}
Pressão: {resultado['pressao']} hPa
Vento: {resultado['vento']} m/s
"""
            messagebox.showinfo(f"Clima em {cidade}", clima)

    botao = tk.Button(janela, text="Buscar", command=buscar, bg="#3399ff", fg="white", font=("Arial", 12, "bold"))
    canvas.create_window(largura//2, 400, window=botao)

    janela.mainloop()
