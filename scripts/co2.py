import re
import csv

dados_limpos = []

regex_verificacao = re.compile(r'[^a-zA-Z0-9,\"\' \-]')

with open('entrada.csv', 'r') as entrada_CSV:
    dados_sujos = entrada_CSV.readlines()

with open('countries_iso-alpha3.csv', 'r') as iso_alpha3:
    reader = csv.reader(iso_alpha3)
    dicionario = {rows[0]: rows[1] for rows in reader}

for linha in dados_sujos:
    temp = linha
    linha_split = temp.split(',')
    for d in dicionario:
        if temp.__contains__(d):
            temp = temp.replace(linha_split[1], dicionario[d])
    dados_limpos.append(temp)

with open('saida.csv', 'w') as out:
    out.writelines(dados_limpos)

with open('saida.csv', 'r') as output:
    verificacao = set(regex_verificacao.findall(output.read()))

print(verificacao)
