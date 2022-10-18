import random 

print('Seja muito bem vindo(a) ao Guess Number!')
choice_number = input("Digite o número teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: o valor fornecido não é numérico. Favor execute novamente!")
    quit()

random_number = random.randint(0, choice_number)
n_choice = 0

while True:
    answer_user = input('Advinhe o número: ')
    
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: o valor fornecido não é numérico. Favor informe um número!")
        continue

    n_choice = n_choice + 1

    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, o numero randomico é menor que isso...")
    else:
        print("Chutou baixo, o numero randomico é maior que isso...")

print("Nº de tentativas: " + str(n_choice))