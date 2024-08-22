texto = input('Digite o texto: ')
texto_criptografado = ''

for i in range(len(texto)):
    texto = texto.lower()
    if 'a' <= texto[i] <= 'e':
        texto_criptografado += '1'
    elif 'f' <= texto[i] <= 'j':
        texto_criptografado += '2'
    elif 'k' <= texto[i] <= 'o':
        texto_criptografado += '3'
    elif 'p' <= texto[i] <= 'z':
        texto_criptografado += '4'
    else:
        texto_criptografado += '5'

print(texto_criptografado)