from calculos import calcular_media_ponderada

nota1 = float(input("Digite a primeira nota (Peso 2): "))
nota2 = float(input("Digite a segunda nota (Peso 3): "))
nota3 = float(input("Digite a terceira nota (Peso 5): "))

resultado = calcular_media_ponderada(nota1, nota2, nota3)

print(f"A média ponderada final é: {resultado}")