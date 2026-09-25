# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

nums = []

for i in range(5):
    nums.append(int(input('Digite um valor: ')))

print(f'O menor elemento digitado foi {min(nums)} na posição {nums.index(min(nums))}.\nEnquanto que o maior elemento digitado foi {max(nums)} na posição {nums.index(max(nums))}.')
