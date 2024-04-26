
soma = 0
soma2 = 0
somadosidosos = 0
somadosmaisnovos = 0

for dale in range(10):
    idadedif = int(input("Digite sua idade"))
    if idadedif >= 40 and idadedif < 50:
        soma += idadedif
        if idadedif >= 40 and idadedif < 50:
            somadosidosos += 1
    if idadedif >= 18 and idadedif < 40:
        soma2 += idadedif
        if idadedif >= 18 and idadedif < 40:
            somadosmaisnovos += 1
if soma >= 1:
    soma = soma / somadosidosos
    print(f"a média de idosos é de {soma}")
else:
    print("não tem pessoas com a idade entre 40 e 50")
if soma2 >= 1:
    soma2 = soma2 / somadosmaisnovos
    print(f"a media de novos e de {soma2}")
else:
    print("não tem pessoas com a idade entre 18 e 40")
