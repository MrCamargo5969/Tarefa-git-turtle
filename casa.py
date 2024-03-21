import turtle
import random
# Codigo principal
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor("#8B8FE4")
def main():
    turtle.title("Casa do João")
    t = turtle.Turtle()
    t.shape("circle")
    t.speed(0)
    draw_gradient(t)
    lua(t)
    estrela2(t)
    corpo(t)
    chameine(t)
    teto(t)
    porta(t)
    macaneta(t)
    janela(t)
    chao(t)
    caminho(t)
    avre(t)
    tronco(t)
    
    t.hideturtle()
    turtle.done()

# Desenhar o quadrilatero corpo da casa
def corpo(t):
    t.penup()
    t.home()
    t.pendown()
    t.color("black")
    t.fillcolor("#D0D300")
    t.begin_fill()
    t.forward(200)  # Linha inferior
    t.left(90)
    t.forward(150)  # Lateral esquerda
    t.left(90)
    t.forward(200)  # Linha superior
    t.left(90)
    t.forward(150)  # Linha inferior
    t.end_fill()

# Desenha o triangulo que faz o telhado da casa
def teto(t):
    t.fillcolor("#B60C00")
    t.begin_fill()
    t.penup()
    t.goto(0, 150)
    t.pendown()
    t.left(120)
    t.forward(115.4)
    t.right(60)
    t.forward(115.4)
    t.right(150)
    t.forward(200)
    t.end_fill()

# desenhar porta
def porta(t):
    t.fillcolor("#8E774E")
    t.begin_fill()
    t.penup()
    t.goto(25, 0)
    t.pendown()
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.end_fill()

# Desenhar uma janela
def janela(t):
    t.fillcolor("#878700")
    t.begin_fill()
    t.penup()
    t.goto(100, 50)
    t.pendown()
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.end_fill()
    t.penup()
    t.goto(100, 87.5)
    t.pendown()
    t.left(90)
    t.forward(75)
    t.penup()
    t.goto(137.5, 125)
    t.pendown()
    t.right(90)
    t.forward(75)
    
def chao(t):
    t.fillcolor("#1a472a")
    t.begin_fill()
    t.penup()
    t.goto(-250, 0)
    t.pendown()
    t.left(90)
    t.forward(500)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(250)
    t.end_fill()

def caminho(t):
    t.fillcolor("#915E00")
    t.begin_fill()
    t.penup()
    t.goto(25, 0)
    t.pendown()
    t.left(135)
    t.forward(371)
    t.left(135)
    t.forward(130)
    t.left(55)
    t.forward(320)
    t.left(125)
    t.forward(50)
    t.end_fill()

def avre(t):
# Arvores de baixo:
    t.fillcolor("#1f3217")
    t.begin_fill()
    t.penup()
    t.goto(225, -100)
    t.pendown()
    t.circle(125)
    t.end_fill()
    t.fillcolor("#355427")
    t.begin_fill()
    t.penup()
    t.goto(200, -125)
    t.pendown()
    t.circle(125)
    t.end_fill()
    t.fillcolor("#4a7537")
    t.begin_fill()
    t.penup()
    t.goto(175, -160)
    t.pendown()
    t.circle(125)
    t.end_fill()

def tronco(t):
    t.fillcolor("#724C27")
    t.begin_fill()
    t.penup()
    t.goto(-160, 100)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.end_fill()

    t.begin_fill()
    t.penup()
    t.goto(-185, 80)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.end_fill()

    t.begin_fill()
    t.penup()
    t.goto(-210, 60)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.end_fill()

# Arvores de cima:
    t.fillcolor("#1f3217")
    t.begin_fill()
    t.penup()
    t.goto(-175, 160)
    t.pendown()
    t.circle(125)
    t.end_fill()
    t.fillcolor("#355427")
    t.begin_fill()
    t.penup()
    t.goto(-200, 140)
    t.pendown()
    t.circle(125)
    t.end_fill()
    t.fillcolor("#4a7537")
    t.begin_fill()
    t.penup()
    t.goto(-225, 120)
    t.pendown()
    t.circle(125)
    t.end_fill()

def chameine(t):
    t.fillcolor("#F38B3D")
    t.begin_fill()
    t.penup()
    t.goto(155, 150)
    t.pendown()
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(70)
    t.penup()
    t.goto(155, 150)
    t.pendown()
    t.end_fill()

def draw_gradient(t):
    colors = ["violet", "#A72781", "#A64199", "#A157B0", "#9B6BC4", "#937DD5", "#8C8FE4"]  # Cores do degradê
    steps = 50  # Número de passos para o degradê
    width, height = screen.window_width(), screen.window_height()

    for i in range(steps):
        y = -height / 2 + (i / steps) * height  # Calcula a posição Y
        color = colors[int((i / steps) * len(colors))]  # Seleciona a cor do degradê
        t.penup()
        t.goto(-width / 2, y)  # Move a tartaruga para a posição inicial
        t.pendown()
        t.color(color)  # Define a cor
        t.begin_fill()  # Inicia o preenchimento
        t.setheading(0)  # Define a direção para a direita
        t.forward(width)  # Desenha uma linha para a direita
        t.right(90)  # Vira a tartaruga para desenhar a altura do retângulo
        t.forward(10)  # Desenha a altura do retângulo
        t.right(90)  # Vira a tartaruga novamente para desenhar a base do retângulo
        t.forward(width)  # Desenha a base do retângulo
        t.end_fill()  # Termina o preenchimento

def lua(t):
    t.color("#B3B5E2")
    t.fillcolor("#B3B5E2")
    t.begin_fill()
    t.penup()
    t.goto(-225, 240)
    t.pendown()
    t.circle(30)
    t.end_fill()

def estrela(t, tamanho):
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)

# Desenha as estrelas
def estrela2(t):
    for _ in range(50):  # Você pode ajustar o número de estrelas conforme desejar
        x = random.randint(-250, 250)  # Posição aleatória no eixo x
        y = random.randint(0, 250)  # Posição aleatória no eixo y
        tamanho = random.randint(1, 4)  # Tamanho aleatório da estrela
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("#B3B5E2")  # Define a cor da estrela
        estrela(t, tamanho)

def macaneta(t):
    t.penup()
    t.goto(65, 50)
    t.pendown()
    t.fillcolor("#2D1D1D")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

main()