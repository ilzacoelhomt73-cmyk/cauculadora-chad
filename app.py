import customtkinter as ctk
import subprocess
from PIL import Image



janela = ctk.CTk()

operadores = ["+", "*", "/", "-"]

primeiro_numero = ctk.StringVar()
segundo_numero = ctk.StringVar()

imagem_do_sigma = ctk.CTkImage(
        dark_image=Image.open("sigma.jpg"),
        size=(200, 200)
        )

mostrar_imagem = ctk.CTkLabel(
        janela,
        image=imagem_do_sigma,
        text=""
        )

ctk.set_appearance_mode("Dark")

janela.title("cauculadora")

janela.geometry("400x500")

p1 = ctk.CTkEntry(
        janela,
        placeholder_text="insira o primeiro numero",
        textvariable=primeiro_numero

        )

def clicar(n):
    global operador
    operador = n


mostrar_imagem.pack(pady=10)

for operador_atual in operadores:
    bt = ctk.CTkButton(
            janela,
            text=operador_atual,
            width=60,
            command=lambda n=operador_atual: clicar(n)
            )
    
    bt.pack(side="left", padx=5, pady=5)

p2 = ctk.CTkEntry(
        janela,
        placeholder_text="insira o segundo numero",
        textvariable=segundo_numero
        )

mostrar_soma = ctk.CTkLabel(
            janela,
            
            )

def caucular(*args):
    if operador == "+":
        resultado = int(primeiro_numero.get()) + int(segundo_numero.get())
        with open("resultado", "w") as arquivo:
            arquivo.write(f"Resultado: {resultado}")
    elif operador == "-":
        resultado = int(primeiro_numero.get()) - int(segundo_numero.get())
        with open("resultado", "w") as arquivo:
            arquivo.write(f"Resultado: {resultado}")

    elif operador == "/":
        resultado = int(primeiro_numero.get()) / int(segundo_numero.get())
        with open("resultado", "w") as arquivo:
            arquivo.write(f"Resultado: {resultado}")

    elif operador == "*":
        resultado = int(primeiro_numero.get()) * int(segundo_numero.get())
        with open("resultado", "w") as arquivo:
            arquivo.write(f"Resultado: {resultado}")



    mostrar_soma.configure(text=f"o Resultado é: {resultado}")
    mostrar_soma.pack(pady=(30, 0))


    

botao_somar = ctk.CTkButton(
        janela,
        text="caucular",
        fg_color="#0000FF",
        text_color="white",
        command=caucular
        )

p1.pack(pady=20)
p2.pack(pady=20)
botao_somar.pack(pady=10)



subprocess.Popen(
    ["mpv", "--loop-file=inf", "chad.mp3"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

janela.mainloop()
