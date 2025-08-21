#algoritmo mercearia da jack
total = 0
vlr = 0

#opcoes de produtos 
print('1 -> Coca-Cola 2L')
print('2 -> Sal lebre')
print('3 -> Arroz Tio João 1Kg')
print('4 -> Feijão Urbano 1Kg')

while id != 0:
    id = int(input('Digite o id do produto. (0 para sair) '))
    if id == 1:
        qntd = int(input('Digite a quantidade: '))
        vlr = qntd * 10.99
        total = total + vlr
    elif id == 2:
        qntd = int(input('Digite a quantidade: '))
        vlr = qntd * 5.99
        total = total + vlr
    elif id == 3:
        qntd = int(input('Digite a quantiade: '))
        vlr = qntd * 7.5
        total = total + vlr
    elif id == 4:
        qntd = int(input('Digite a quantidade: '))
        vlr = qntd * 8.9
        total = total + vlr
    elif id < 0 or id > 4:
        print('Código invalido')

#opcoes de pagamento
print('Total a pagar R$', total)
print("Digite o código da forma de pagamento")
print("1 -> Crédito")
print("2 -> Débito")
print("3 -> pix")
print("4 -> Espécie")
pagamento = int(input(':'))

if pagamento == 1:
    resposta = int(input('Crédito selecionado, deseja parcelar? (1 para sim / 0 para não): '))
    if resposta == 1:
        print('Parcelas de 2x R$', total/2)
        print('Parcelas de 3x R$', total/3)
        resposta2 = int(input('Escolha (2 ou 3):'))
        while resposta2 != 2 and resposta2 != 3:
            print('Código invalido, digite novamente')
            resposta2 = int(input('Escolha (2 ou 3):'))
            if resposta2 == 2:
                print('Parcela de 2x escolhida, 2 parcelas de R$', total / 2)
            elif resposta2 == 3:
                print('Parcela de 3x escolhida, 3 parcelas de R$', total / 3)
    elif resposta == 0:
        print('Total a pagar R$', total)
if pagamento == 2:
    print('Débito selecionado, Total a pagar R$', total)
if pagamento == 3:
    print('Pix selecionado, Total a pagar R$', total)
    print('Chave pix: 00.000.000/0000-00')
if pagamento == 4:
    print("Espécie selecionado, Total a pagar R$", total)
print('Obrigado pela compra!')
# Fim do algoritmo