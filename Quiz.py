""" Projeto para testar perguntas e respostas do usuário
Aprendendo a jogar no GitHub

"""
pontos = 0

print("Seja muito bem vindo ao quiz!")
answer_user = input("Quer começar? (s/n) ").lower() # Aceitar resposta minuscula ou maiuscula
print(answer_user)

if answer_user != "s":
    quit()

print("Começando...")    
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (10 pts) \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n ")

answer_1 = input("Resposta: ").lower()

if answer_1 == "a" : 
    pontos = pontos + 10
    print("Correct!")
else:
    print("Incorreto!")

print("Qual o protragonista do jogo GTA San Andreas? \n (10 pts) \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson ")
print("Valor = 10")
answer_1 = input("Resposta: ").lower()

if answer_1 == "b":
    print("Correct!")
    pontos = pontos + 10
else:
    print("Incorreto!")

print("Qual o melhor carro? Valor da questao = 10 pts \n (A) Fusca \n (B) Uno \n (C) Vtr \n (D) Ferrari ")
print("Valor = 10")
answer_1 = input("Resposta: ").lower()

if answer_1 == "c":
    print("Correct!")
    pontos = pontos + 10
else:
    print("Incorreto!")

print("Pontuação total =", pontos )





