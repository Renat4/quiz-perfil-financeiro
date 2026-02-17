import time

titulo = "PROJETO CAOS, MEMBRO DO CLUBE OU LOBO DE WALL STREET"
print('\n' + '~'*70)
print(f'{titulo:^70}')
print('~'*70 + '\n')

total_pontos = 0
pergunta = ['1 - O salário caiu na conta agora. Qual o seu primeiro movimento?', 
            '2 - Surgiu um imprevisto caro(o celular quebrou ou o carro parou). Como está sua reserva?',
            '3 - Te convidaram para uma viagem, mas o orçamento está apertado, então você...',
            '4 - Daqui a 10 anos, onde você se vê?',
            '5 - Sexta-feira a noite, onde você está?',
            '6 - Você vê uma promoção de algo caro que você não planejava comprar agora, qual sua decisão?']

opcoes = ['''A. Compro logo algo que eu queria muito. Afinal, eu mereço e o amanhã é uma incerteza.
B. Pago todas as contas do mês. Se sobrar algo, eu vejo o que faço depois.
C. Separo primeiro o valor de investir. Eu gasto o que sobra depois de guardar.''',

'''A. Que reserva? Vou ter que parcelar tudo no cartão e torcer para o limite dar ou pedir emprestado para alguém.
B. Tenho um dinheirinho guardado, mas vai doer muito e vou ficar no aperto esse mês.
C. Tranquilo. Eu tenho uma reserva específica para emergências e isso não muda meus planos.''',

'''A. Jogo tudo pro alto e vou. A gente só vive uma vez!
B. Só vou se conseguir parcelar em mil vezes sem juros, mesmo sabendo que vou me apertar.
C. Analiso se consigo remanejar meus investimentos sem prejudicar minha meta principal.''',

'''A. Não sei nem o que vou comer amanhã. O futuro é uma ilusão.
B. Tendo uma vida estável, talvez terminando de pagar o financiamento do meu "cubículo".
C. No topo. Com a liberdade financeira batendo na porta e o sistema trabalhando por mim.''',

'''A. Curtindo a vida, afinal, só se vive uma vez né?
B. No barzinho com os amigos, dividindo a conta milimetricamente no aplicativo.
C. Em casa ou saindo, mas com o orçamento da noite já definido. Eu sei exatamente quanto posso gastar para me divertir sem quebrar o meu plano. ''',

'''A. Compro. O amanhã é uma ilusão e o prazer é agora. 
B. Eu olho, desejo e até imagino usando, mas lembro que tenho outros planos pro meu dinheiro. Saio da loja com aquela sensação de vitória... mas meio triste. 
C. Passo reto. Eu “vendo a caneta”, eu não “compro a caneta” por impulso. ''']

for i in range (len(pergunta)):
    while True:
        print(pergunta[i])
        print(opcoes[i])

        escolha = str(input('Sua escolha: ')).upper().strip()

        if escolha in 'ABC':
            if escolha == 'A':
                total_pontos += 1
            elif escolha == 'B':
                total_pontos += 3
            elif escolha == 'C':
                total_pontos += 5
            time.sleep(0.5)
            break
        print('Opção inválida! Digite apenas A, B ou C')

print('='*50)

texto = "PROCESSANDO SEU PERFIL FINANCEIRO"

for i in range(4):
    print(f'\r{(texto + "." * i):^50}', end='', flush=True)
    time.sleep(1)

print()
print('='*50)

if 6 <= total_pontos <= 12:
    print(f'PONTOS: {total_pontos} | PERFIL: \033[31mPROJETO CAOS\033[m')
    print('Você vive perigosamente. Para você, dinheiro é feito para queimar! Afinal, só se vive uma vez não é mesmo? Só cuidado com o amanhã porque ele SEMPRE chega.')
elif 13 <= total_pontos <= 22:
    print(f'PONTOS: {total_pontos} | PERFIL: \033[33mMEMBRO DO CLUBE\033[m')
    print(f'Você segue as regras, mas ainda trabalha para pagar os boletos. Falta ambição.')
else:
    print(f'PONTOS: {total_pontos} | PERFIL: \033[31mLOBO DE WALL STREET\033[m')
    print('Você joga para ganhar. A disciplina é sua estratégia e o topo é o seu lugar.')