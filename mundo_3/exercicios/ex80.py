# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

nums = []

for i in range(5):
    num = int(input('Digite um valor: '))

    if i == 0 or num > nums[-1]: # Se for o primeiro valor digitado OU o valor digitado for maior que o valor na última posição da lista
        nums.append(num)
        print(f'O valor {num} foi adicioando ao final da lista.')
    else:
        pos = 0 # Faz um loop para todas as posições do array
        while pos < len(nums):
            if num <= nums[pos]: # Se o valor digitado for menor ou igual ao valor na posição analisada
                nums.insert(pos, num) # Insere o valor digitado nessa posição
                print(f'O valor {num} foi digitado na posição {pos} da lista.')
                break
            pos += 1

print(f'Os valores digitados em ordem foram: {nums}')