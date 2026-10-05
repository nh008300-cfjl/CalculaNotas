nota1 = float(input("Digite a primeira nota (Peso 2): "))
nota2 = float(input("Digite a segunda nota (Peso 3): "))
nota3 = float(input("Digite a terceira nota (Peso 5): "))

media_ponderada = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)

print(f"A média ponderada do aluno é: {media_ponderada}")