# Cálculo de RMSE para dados de Temperatura do Ar
<div style="text-align: justify">
A métrica <i>Root Mean Squared Error</i> (RMSE) é utilizada para analisar a acurácia de um modelo preditivo. Partindo da importância dessa medida,
este projeto tem o objetivo de calcular o RMSE a partir de dados observados e previstos da temperatura do ar para o estado de São Paulo. Serviu de
objeto de estudo para aplicações do Python.

## Requisitos
Para utilizar o projeto, é necessária a instalação de alguns pacotes no <i>environment</i> utilizado.

Os pacotes dispostos abaixo são voltados para a manipulação de dados <b>n-dimensionais</b>. Essas bibliotecas incorporam muitas funções do NumPy e Pandas, porém com a capacidade de operar em dados com pontos de grade. O <i>xskillscore</i> oferece módulos que determinam várias métricas preditivas.

```bash
user@dektop:~$ pip install xarray
user@dektop:~$ pip install xskillscore
```

<p style="font-weight:bold">Descrição dos arquivos</p>


Dados de Previsão


| Propriedade                        | Descrição   |
| :--------------------------------- |:------------|
| Arquivo                            | forecast.nc |
| Número de tempos                   | 72          |
| Data de referência                 | 2018/04/14  |
| Frequência do tempo                | Horária     |
| Nome da variável de temperatura    | t2m         |
| Unidade da variável de temperatura | Kelvin      |


Dados Observados

| Propriedade                        | Descrição      |
| :--------------------------------- |:---------------|
| Arquivo                            | observation.nc |
| Número de tempos                   | 72             |
| Data de referência                 | 2018/04/14     |
| Frequência do tempo                | Horária        |
| Nome da variável de temperatura    | temperatura    |
| Unidade da variável de temperatura | Grau Celsius   |

</p>

Os arquivos de dados observados e previsão precisam estar no mesmo diretório que o código.

## Funcionalidade

Como o projeto tem o intuito de aprendizado, dois códigos podem ser encontrados no repositório. O `main.py` está documentado e dividido por funções, já o `main.ipynb` é um <i>Jupyter notebook</i> com o código mais limpo.

O código está dividido por blocos que:
- Importam os pacotes que serão utilizados
- Importam e efetuam a leitura de arquivos no formato `.nc`
- Os arquivos de entrada possuem valores de coordenadas diferentes. Para efeito de padronização de <i>datasets</i>, suas coordenadas são uniformizadas
- Como a variável de `previsão.nc` está em Kelvin, efetua-se a transformação para °C
- Muda a frequência horária dos arquivos para intervalos de 6 horas e calcula o RMSE para cada intervalo e ponto de grade, escrevendo um <i>output</i> de `RMSE_6hourly.nc` com a métrica calculada.

<p style="text-align: center">
    <img src="https://media-exp1.licdn.com/dms/image/C5612AQF8JAeUs7CwCQ/article-inline_image-shrink_1000_1488/0/1543435697122?e=1649289600&v=beta&t=AEoZzW08votOCHB5v12lFAroXSdcBXfcyiCfY3hNfxE" alt="RMSE"/> 
</p>

O projeto ainda está em desenvolvimento e as próximas atualizações serão:
- Criação de campos espaciais de cada intervalo com os valores de RMSE para o estado de São Paulo
- Plot da série temporal contendo temperatura do ar observada, prevista e o RMSE para a capital

## Execução

Utilize <b>Python 3.X</b>:
```bash
user@dektop:~$ python3 main.py
```
O código retornará:
- As dimensões dos arquivos de entrada
- Se as variáveis já estão em °C
- Criação do arquivo de saída `.nc`
- Informações gerais do <i>output</i>

## Referências

[xarray](https://xarray.pydata.org/en/stable/) \
[xskillscore](https://xskillscore.readthedocs.io/en/stable/) \
[Challenge criado pela Climatempo](https://github.com/climatempo/challenge-accepted-python/blob/master/README.md)
___