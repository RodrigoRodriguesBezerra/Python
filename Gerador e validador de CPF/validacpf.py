import re


def valida_cpf(cpf):
    cpf = str(cpf)
    # Substitui tudo que não é número por espaço vazio
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]  # Elimina os dois últimos dígitos do CPF
    reverso = 10  # Contador Reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:       # Primeiro indice vai de 0 a 9
            index -= 9      # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1  # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:               # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0               # Zera o total
            novo_cpf += str(d)      # Concatena o digito gerado no novo cpf

    # Evita sequências. Ex.: 1111111, 0000000...
    sequencia = novo_cpf == str(novo_cpf[0] * len(cpf))

    if cpf == novo_cpf and not sequencia:
        return True

    return False
