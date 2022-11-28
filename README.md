Dados limpos, codificados em UTF-8, com pontos nas casas decimais e cabeçalhos destraduzidos para que as consultas fiquem como nos vídeos.

## Curso 4, semana 3
**Seção:** Transformando dados  
**Conjunto de dados:** [`customer_purchase.csv`](conjuntos/C4/customer_purchase.csv)

Corrige o seguinte erro de importação para o BigQuery usando o esquema indicado:

```
Falha na criação da tabela: Error while reading data, error message: Could not parse 'USD 13,99' as DOUBLE for field product_price (position 6) starting at location 119 with message 'Unable to parse'. 
```

Remove a marcação de moeda "USD", que não permite a importação como um tipo *float* pelo esquema fornecido. Essa conversão de tipo seria parte da atividade, mas não deveria impossibilitar a importação do conjunto.

## Curso 5, semana 1
**Seção:** Classificar dados usando SQL  
**Conjunto de dados:** [`movies.csv`](conjuntos/C5/movies.csv)

Os caracteres especiais foram substituídos e o arquivo foi codificado como UTF-8, resolvendo erros de exibição nos acentos. Você pode ver o script usado para normalizar e substituir as ocorrências na pasta [scripts](/scripts).

## Curso 5, semana 3  
**Seção:** Usar instruções JOIN para agregar dados no SQL  
**Conjuntos de dados:** [`employees.csv`](conjuntos/C5/employees.csv) e [`departments.csv`](conjuntos/C5/departments.csv)

Apenas desfaz a tradução dos cabeçalhos para que corresponda ao vídeo.

## Curso 6, semana 2
**Seção:** Introdução ao Tableau  
**Conjuntos de dados:** [`co2.csv`](conjuntos/C6/co2.csv)

Os nomes dos países e os códigos de países foram destraduzidos e corrigidos, permitindo a identificação como dados geográficos pelo Tableau.

Para automatizar a correção, foi usado um arquivo CSV com cada código ISO-3166 e um script. Ambos estão disponíveis na pasta [scripts](scripts).

## Curso 6, semana 2
**Seção:** Trabalhar com várias fontes de dados  
**Conjuntos de dados:** [`co2.xlsx`](conjuntos/C6/S2/co2.xlsx), [`energy.csv`](conjuntos/C6/S2/energy.csv), [`gdptotal.csv`](conjuntos/C6/S2/gdptotal.csv) e [`totalpopulation.csv`](conjuntos/C6/S2/totalpopulation.csv)

Os nomes dos países foram destraduzidos, permitindo que o Tableau os identifique como dados geográficos. Sem isso não é possível gerar uma visualização de mapa.

Os valores decimais foram corrigidos para usarem pontos ao invés de vírgulas e os cabeçalhos destraduzidos para que os valores apareçam como nos vídeos.

