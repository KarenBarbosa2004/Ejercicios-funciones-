# Funcion
def celulares(Elementos):
('\n\t---Contenido de la lista---')


Elementos = ['samsung', 'lg', 'sony', 'nokia', 'apple', n'motorola', 'xiaomi', 'alcatel', 'lenovo', 'huawei']
Cadena = ",".join(Elementos)
Ordenar = sorted(Elementos)
Contador = 1
print('\n\t---Contenido de la lista----')
for i in Elementos:
    print(f'{Contador}. {i}')
    Contador += 1
print('\n\t---Cadena---\n')
print(Cadena)
print(f'n\t---Elementos organizados---\n\n{Ordenar}')