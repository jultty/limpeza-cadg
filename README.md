Dados limpos, codificados em UTF-8, com pontos nas casas decimais e cabeçalhos destraduzidos para que as consultas fiquem como nos vídeos.

## Curso 4, semana 3
**Seção:** Transformando dados  
**Conjunto de dados:** [`customer_purchase.csv`](customer_purchase.csv)

Ao tentar importar os dados para o BigQuery usando o esquema indicado, o seguinte erro é exibido:

```
Falha na criação da tabela: Error while reading data, error message: Could not parse 'USD 13,99' as DOUBLE for field product_price (position 6) starting at location 119 with message 'Unable to parse'. 
```

A marcação de moeda "USD" não permite a importação como um tipo *float* pelo esquema fornecido.

## Curso 5, semana 1
**Seção:** Classificar dados usando SQL  
**Conjunto de dados:** [`movies.csv`](movies.csv)

O arquivo CSV traduzido não usa uma codificação com suporte para todos os acentos, causando erros de exibição nos caracteres especiais. Você pode ver o script usado para normalizar e substituir as ocorrências na pasta [scripts](/scripts).

## Curso 5, semana 3  
**Seção:** Usar instruções JOIN para agregar dados no SQL  
**Conjuntos de dados:** [`employees.csv`](employees.csv) e [`departments.csv`](departments.csv)

Apenas desfaz a tradução dos cabeçalhos para facilitar ao acompanhar o vídeo. Note também que a coluna "id_departmento" tem um erro de digitação.

## Curso 6, semana 2
**Seção:** Introdução ao Tableau  
**Conjuntos de dados:** [`co2.csv`](co2.csv)

Os nomes dos países e alguns códigos de países foram traduzidos, impossibilitando a identificação deles como dados geográficos pelo Tableau.

Os nomes originais dos países foram substituídos usando um arquivo CSV com cada código ISO-3166. O script está disponível na pasta [scripts](/scripts).
