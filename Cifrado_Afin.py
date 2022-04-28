def euclides_modinverso(a, n):
    for i in range(1, n):
        if (a % n) * (i % n) % n == 1:
            return i

def encripado(texto, llave):
    return ''.join([ chr((( llave[0]*(ord(t) - ord('A')) + llave[1] ) % 27) + ord('A')) for t in texto.upper().replace(' ', '') ])

def desencriptado(texto_cifrado, llave):
    return ''.join([ chr((( euclides_modinverso(llave[0], 27)*(ord(c) - ord('A') - llave[1])) % 27) + ord('A')) for c in texto_cifrado ])

el_texto = 'ELEMENTALMIQUERIDOWATSON'
la_llave = [17, 20]
print("Aqui esta el texto encriptado")
texto_c = encripado(el_texto, la_llave)
print(texto_c)
print("Aqui esta el texto desencriptado")
texto_d = desencriptado(texto_c, la_llave)
print(texto_d)
print("Este es el texto encriptado que aparece en el ejercicio")
texto_ejercicio_encriptado = 'OKHFSNKFNWFCWJHSNCHQYWFSWF'
texto_ejercicio_desencriptado = desencriptado(texto_ejercicio_encriptado, la_llave)
print(texto_ejercicio_desencriptado)
print("El segundo texto encriptado del ejercicio")
texto_ejercicio_encriptado_2 = 'SLBCMVRBSHZBT~SRQVVMSZBVH~BVRQVLALHZBT~SRQVWQAXLZW~AQFQV'
texto_ejercicio_desencriptado_2 = desencriptado(texto_ejercicio_encriptado_2, la_llave)
print(texto_ejercicio_desencriptado_2)
    
    