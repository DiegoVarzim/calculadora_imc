#  Cálculo de IMC - Índice de Massa Corporal

'''
Qual é a sua altura em cm:
Qual é o seu peso em kg:

'''

# MENOR QUE 18,5 - MAGREZA
# ENTRE 18,5 E 24,9 - NORMAL
# ENTRE 25,0 E 29,9 - SOBREPESO
# ENTRE 30,0 E 39,9 - OBESIDADE
# MAIOR QUE 40,0 - OBESIDADE GRAVE



altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

imc = peso / (altura/100)**2

if imc < 18.5:
    print('Magreza')
elif imc >= 18.5 and imc <= 24.9:
    print('Normal')
elif imc >= 25.0 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 30.0 and imc <= 39.9:
    print('Obesidade')
else:
    print('Obesidade Grave')


print(imc)
