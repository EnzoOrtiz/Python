numero = 1

while numero <= 10:
    print(f"\nTabuada do {numero}:")
    multiplicador = 0
    while multiplicador <= 10:
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        multiplicador += 1
    numero += 1
