tab1 = int(input("Digite um numero para ver uma tabuada de 1 até 5"))
tab2 = int(input("Digite outro numero entre 1 e 5 para ver outra tabuada"))
if tab2 > 5:
    tab2 = 5
    print("Você não pode informar um numero maior que 5")
if tab1 >5:
    tab1 =1
    print("Você só pode começar do 5")
if tab1 <0:
    tab1 =1
if tab2 < 0:
    tab2 =5
    print("Você só pode informar um numero em ordem crescente")
for l in range(tab1,tab2+1):
    for m in range(1,11):
        print( l, 'X', m, '=', l*m)
