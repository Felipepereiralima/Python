#Tupla são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print(f'Eu comi pra caramba, {len(lanche)} lanches!!')
print('-'*32)
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print(f'Eu comi pra caramba, {len(lanche)} lanches!!')
