# função principal do programa
def main():
    principal = 2000.00
    taxa = 0.03
    meses = 3
    anterior = 0.0

    for i in range(1, meses + 1):
        montante = principal * pow((1 + taxa), i)
        juros = montante - principal - anterior

        anterior += juros

        print("Mês:", i, " - Montante:", montante, "- Juros:", juros)


if __name__ == "__main__":
    main()