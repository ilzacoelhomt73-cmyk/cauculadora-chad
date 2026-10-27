import customtkinter as ctk
import subprocess
from PIL import Image

operador = None

tipo_de_retornagem = float
musica = True
copiar_automaticamente = False

subprocess.run(["clear"])

janela = ctk.CTk()

resultado_global = None

titulo = ctk.CTkLabel(
        janela,
        text="Cauculadora chad",
        text_color="purple",
        font=("Arial", 30)
        )

operadores = ["+", "*", "/", "-"]

primeiro_numero = ctk.StringVar()
segundo_numero = ctk.StringVar()

imagem_do_sigma = ctk.CTkImage(
        dark_image=Image.open("gigachad/sigma.jpg"),
        size=(200, 200)
        )

mostrar_imagem = ctk.CTkLabel(
        janela,
        image=imagem_do_sigma,
        text=""
        )

ctk.set_appearance_mode("Dark")

janela.title("cauculadora chad")

janela.geometry("400x700")

titulo.pack(pady=20)

p1 = ctk.CTkEntry(
        janela,
        placeholder_text="insira o primeiro numero",
        textvariable=primeiro_numero

        )

def clicar(n):
    global operador
    operador = n


mostrar_imagem.pack(pady=10)
p2 = ctk.CTkEntry(
        janela,
        placeholder_text="insira o segundo numero",
        textvariable=segundo_numero
        )

mostrar_soma = ctk.CTkLabel(
            janela,
            text="Resultado: ",
            font=("Arial", 20)
            )

def caucular(*args):
    if operador is None:
        mostrar_soma.configure(text="selecione um operador")
        mostrar_soma.pack(pady=10)
        return

    n1 = tipo_de_retornagem(primeiro_numero.get())
    n2 = tipo_de_retornagem(segundo_numero.get())

    try:
        if operador == "+":
            resultado = n1 + n2

        elif operador == "-":
            resultado = n1 - n2

        elif operador == "/":
            resultado = n1 / n2

        elif operador == "*":
            resultado = n1 * n2

    except ZeroDivisionError: 
        imagem_do_sigma_confuso = ctk.CTkImage(
                dark_image=Image.open("gigachad/confuso.jpg"),
                size=(200, 200)
                )
        
        

        mostrar_imagem_confuso = ctk.CTkLabel(
                janela,
                image=imagem_do_sigma_confuso,
                text=""
                )
        mostrar_imagem.configure(image=imagem_do_sigma_confuso)
        mostrar_soma.configure(text="IRMÃO, isso nao existe")
        mostrar_imagem.image = imagem_do_sigma
        mostrar_soma.place(relx=0.5, y=300, anchor="center")   
    else: 
        mostrar_imagem.configure(image=imagem_do_sigma)
        if copiar_automaticamente:
            janela.clipboard_clear()
            janela.clipboard_append(resultado)

            with open("resultado", "w") as arquivo:
                arquivo.write(f"{n1} {operador} {n2}: {resultado}\n")

            print(f"{n1} {operador} {n2}: {resultado}")

            mostrar_soma.configure(text=f"o Resultado é: {resultado}")
            mostrar_soma.place(relx=0.5, y=300, anchor="center")


        else:

            with open("resultado", "w") as arquivo:
                arquivo.write(f"{n1} {operador} {n2}: {resultado}\n")

            print(f"{n1} {operador} {n2}: {resultado}")

            mostrar_soma.configure(text=f"o Resultado é: {resultado}")
            mostrar_soma.place(relx=0.5, y=300, anchor="center")

for indice, operador_atual in enumerate(operadores):
    bt = ctk.CTkButton(
            janela,
            text=operador_atual,
            width=60,
            fg_color="#8B5CF6",
            command=lambda n=operador_atual: clicar(n)
            )

    bt.place(x=55 + indice * 75, y=600)





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

if musica:
    subprocess.Popen(
        ["mpv", "--loop-file=inf", "gigachad/chad.mp3"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

else:
    pass

janela.mainloop()
