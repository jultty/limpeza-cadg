# limpeza-cadg

Dados limpos para o Certificado Profissional de Análise de Dados do Google.

| **Curso** | **Semana** | **Seção**                                        | **Conjuntos** |
|-----------|------------|--------------------------------------------------|---------------|
| 4         | 3          | Transformando dados                              | [`customer_purchase.csv`](conjuntos/C4/customer_purchase.csv) |
| 5         | 1          | Classificar dados usando SQL                     | [`movies.csv`](conjuntos/C5/movies.csv) |
| 5         | 3          | Usar instruções JOIN para agregar dados no SQL   | [`employees.csv`](conjuntos/C5/employees.csv) e [`departments.csv`](conjuntos/C5/departments.csv) |
| 6         | 2          | Introdução ao Tableau                            | [`co2.csv`](conjuntos/C6/co2.csv) |
| 6         | 2          | Trabalhar com várias fontes de dados             | [`co2.xlsx`](conjuntos/C6/S2/co2.xlsx), [`energy.csv`](conjuntos/C6/S2/energy.csv), [`gdptotal.csv`](conjuntos/C6/S2/gdptotal.csv) e [`totalpopulation.csv`](conjuntos/C6/S2/totalpopulation.csv) |

**O que muda:**
* Suporte para caracteres especiais
* Pontos e não vírgulas nas casas decimais
* Adequações nos tipos de dados
* Cabeçalhos destraduzidos para que as consultas fiquem como nos vídeos

Alguns campos são mantidos sujos quando a atividade consiste em limpá-los.

<details>
<summary>Clique para mais informações</summary>

## Índice dos conjuntos

### Curso 4, semana 3
**Seção:** Transformando dados  
**Conjunto de dados:** [`customer_purchase.csv`](conjuntos/C4/customer_purchase.csv)

Corrige o seguinte erro de importação para o BigQuery usando o esquema indicado:

```
Falha na criação da tabela: Error while reading data, error message: Could not parse 'USD 13,99' as DOUBLE for field product_price (position 6) starting at location 119 with message 'Unable to parse'. 
```

Remove a marcação de moeda "USD", que não permite a importação como um tipo *float* pelo esquema fornecido. Essa conversão de tipo seria parte da atividade, mas não deveria impossibilitar a importação do conjunto.

### Curso 5, semana 1
**Seção:** Classificar dados usando SQL  
**Conjunto de dados:** [`movies.csv`](conjuntos/C5/movies.csv)

Substitui os caracteres especiais, resolvendo um problema de codificação. O script usado para normalizar e substituir as ocorrências está disponível na pasta [scripts](/scripts).

### Curso 5, semana 3  
**Seção:** Usar instruções JOIN para agregar dados no SQL  
**Conjuntos de dados:** [`employees.csv`](conjuntos/C5/employees.csv) e [`departments.csv`](conjuntos/C5/departments.csv)

Desfaz a tradução dos cabeçalhos para que correspondam ao vídeo.

### Curso 6, semana 2
**Seção:** Introdução ao Tableau  
**Conjuntos de dados:** [`co2.csv`](conjuntos/C6/co2.csv)

Corrige e destraduz os nomes e códigos dos países, permitindo a identificação como dados geográficos pelo Tableau.

Para automatizar a correção, foi usado um arquivo CSV com cada código ISO-3166 e um script. Ambos estão disponíveis na pasta [scripts](scripts).

### Curso 6, semana 2
**Seção:** Trabalhar com várias fontes de dados  
**Conjuntos de dados:** [`co2.xlsx`](conjuntos/C6/S2/co2.xlsx), [`energy.csv`](conjuntos/C6/S2/energy.csv), [`gdptotal.csv`](conjuntos/C6/S2/gdptotal.csv) e [`totalpopulation.csv`](conjuntos/C6/S2/totalpopulation.csv)

Corrige e destraduz os nomes e códigos dos países, permitindo que o Tableau os identifique como dados geográficos. Sem isso não é possível gerar uma visualização de mapa como pedido.

Corrige os valores decimais para pontos no lugar das vírgulas e destraduz os cabeçalhos para que apareçam como nos vídeos.

## Licenças
Os dados aqui disponíveis são provenientes de conjuntos públicos de dados ou são dados demonstrativos mostrados no conteúdo da certificação.

Fontes de dados e licenças:

* [Banco Mundial](https://data.worldbank.org)
  * `co2.xlsx` e `co2.csv`: CC BY-NC 4.0
  * `totalpopulation.csv`: CC BY-4.0
  * `gdptotal.csv`: CC BY-4.0 
* [IMDb](https://www.imdb.com/interfaces/)
  * `movies.csv`: IMDb non-commercial licensing
* Dados de exemplo da certificação
  * `customer_purchase.csv`
  * `employees.csv` e `departments.csv`

</details>
