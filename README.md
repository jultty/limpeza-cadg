Dados limpos, codificados em UTF-8, com pontos nas casas decimais e cabeçalhos destraduzidos para que as consultas fiquem como nos vídeos.

## Curso 4, semana 3
**Seção:** Transformando dados  
**Conjunto de dados:** [`customer_purchase.csv`](conjuntos/C4/customer_purchase.csv)

Ao tentar importar os dados para o BigQuery usando o esquema indicado, o seguinte erro é exibido:

```
Falha na criação da tabela: Error while reading data, error message: Could not parse 'USD 13,99' as DOUBLE for field product_price (position 6) starting at location 119 with message 'Unable to parse'. 
```

A marcação de moeda "USD" não permite a importação como um tipo *float* pelo esquema fornecido.

## Curso 5, semana 1
**Seção:** Classificar dados usando SQL  
**Conjunto de dados:** [`movies.csv`](conjuntos/C5/movies.csv)

O arquivo CSV traduzido não usa uma codificação com suporte para todos os acentos, causando erros de exibição nos caracteres especiais. Você pode ver o script usado para normalizar e substituir as ocorrências na pasta [scripts](/scripts).

## Curso 5, semana 3  
**Seção:** Usar instruções JOIN para agregar dados no SQL  
**Conjuntos de dados:** [`employees.csv`](conjuntos/C5/employees.csv) e [`departments.csv`](conjuntos/C5/departments.csv)

Apenas desfaz a tradução dos cabeçalhos para facilitar ao acompanhar o vídeo. Note também que a coluna "id_departmento" tem um erro de digitação.

## Curso 6, semana 2
**Seção:** Introdução ao Tableau  
**Conjuntos de dados:** [`co2.csv`](conjuntos/C6/co2.csv)

Os nomes dos países e alguns códigos de países foram traduzidos, impossibilitando a identificação deles como dados geográficos pelo Tableau.

Os nomes originais dos países foram substituídos usando um arquivo CSV com cada código ISO-3166. O script está disponível na pasta [scripts](scripts).

## Curso 6, semana 2
**Seção: Trabalhar com várias fontes de dados**
**Conjuntos de dados:** [`co2.xlsx`](conjuntos/C6/S2/co2.xlsx), [`energy.csv`](conjuntos/C6/S2/energy.csv), [`gdptotal.csv`](conjuntos/C6/S2/gdptotal.csv) e [`totalpopulation.csv`](conjuntos/C6/S2/totalpopulation.csv)

Os nomes dos países foram traduzidos, impossibilitando a identificação pelo Tableau como dados do tipo *spatial* (geográficos). Isso torna impossível gerar uma visualização de mapa.

Os valores decimais foram corrigidos para usarem pontos ao invés de vírgulas, para que os valores apareçam como nos vídeos.

Por fim, os cabeçalhos dos arquivos também foram alterados para corresponderem ao conteúdo do curso.

