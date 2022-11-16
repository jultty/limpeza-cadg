Dados limpos, codificados em UTF-8, com pontos nas casas decimais e cabeçalhos destraduzidos para que as consultas fiquem como nos vídeos.

## Curso 4, semana 3
**Seção:** Transformando dados
**Conjunto de dados:** `customer_purchase.csv`

Ao tentar importar os dados para o BigQuery usando o esquema indicado, o seguinte erro é exibido:

```
Falha na criação da tabela: Error while reading data, error message: Could not parse 'USD 13,99' as DOUBLE for field product_price (position 6) starting at location 119 with message 'Unable to parse'. 
```

A marcação de moeda "USD" não permite a importação como um tipo *float* pelo esquema fornecido.

## Curso 5, semana 1
**Seção: Classificar dados usando SQL**
**Conjunto de dados:** `movies.csv`

O arquivo CSV traduzido não usa uma codificação com suporte para todos os acentos, causando erros de exibição nos caracteres especiais. Você pode ver o script usado para substituir as ocorrências na pasta `scripts`.
