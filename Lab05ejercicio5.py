texto = "X-DSPAM--Confidence: 0.8475"
inicio = texto.find(":")
final = len(texto)
número = texto[inicio:final]
print(inicio, final)
print(número)
print(type(número))

