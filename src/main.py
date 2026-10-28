import numpy as np

#gerando bits aleatórios

rng = np.random.default_rng(42)

bits = rng.integers(0, 2, size=10)


#mapeamento antipodal

simbolos = 1 - 2 * bits

#gerar ruído gaussiano

sigma = 0.4
ruido = rng.normal(0, sigma, size=simbolos.shape)

recebido = simbolos + ruido

print(" Bits gerados:", bits)
print(" Símbolos mapeados:", simbolos)
print(" Ruído gaussiano:", ruido)
print(" Sinal recebido:", recebido)

bits_decodificados = (recebido < 0).astype(int)

print(" Bits decodificados:", bits_decodificados)

erros = 0

for i in range(len(bits)):
    if bits[i] != bits_decodificados[i]:
        erros += 1

print(" Número de erros:", erros)
ber = erros / len(bits)
print(" Taxa de erro de bit (BER):", ber)