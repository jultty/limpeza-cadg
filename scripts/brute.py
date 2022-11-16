import re
from charset_normalizer import from_bytes

dados_sujos = []
dados_limpos = []

regex = re.compile(r'[^a-zA-Z0-9!@#$%&*()/,:.\"\' \-_;]')

with open('entrada.csv', 'rb') as entrada_CSV:
    dados_sujos.append(str(from_bytes(entrada_CSV.read()).best()))

dicionario = {'č': 'ã', '√Ī': 'ñ', 'Ňü': 'ş', '√≥': 'ó', 'ć': 'ç',
              '√ď': 'Ó', '√ß': 'ç', '√ę': 'ë', '‚Äď': '–', 'ńá': 'ć',
              '√ľ': 'ü', 'ńü': 'ğ', '√Č': 'É', 'ź': 'ê', '√°': 'á',
              '‚ā™': '', '√∂': 'ö', '√į': 'ð', 'Ňě': 'Ş', '√≠': 'í',
              'í': 'í', '√•': 'å', 'á': 'á', '√®': 'è', '√©': 'é', 'ńĪ': 'ı'}

for linha in dados_sujos:
    temp = linha
    for d in dicionario:
        if temp.__contains__(d):
            temp = temp.replace(d, dicionario[d])
    dados_limpos.append(temp)

with open('saida.csv', 'w') as out:
    out.writelines(dados_limpos)

with open('saida.csv', 'r') as output:
    verificacao = set(regex.findall(output.read()))
    print(verificacao)
