# Serviço de dados meteorológicos

Este serviço tem como proposta fazer a coleta dos dados diários de cada localidade cadastrada, em paralelo com a coleta de dados de previsão do tempo. Este serviço faz uso de uma API aberta, chamada [OpenWeather](https://openweathermap.org/api), que disponibiliza dados meteorológicos de diversas localidades do mundo, tendo uma boa precisão comparada a outros serviços de código fechado.

## Dados disponíveis

Neste serviço, é possível coletar os seguintes dados:

* Temperatura atual (Celsius)
* Temperatura mínima
* Temperatura máxima
* Velocidade do vento (km/h)
* Precipitação (mm)

## Dados meteorológicos atuais

Disponibiliza uma amostra dos dados coletados de minuto a minuto (dados comumente atualizados), de acordo com a [API](https://openweathermap.org/api) utilizada para a coleta das informações meteorológicas.

**GET**: http://localhost:4000/minutely_measurement/

```json
[
  {
    "id": 312,
    "collection_time": "2019-09-16T10:11:23-03:00",
    "temperature": 298.39,
    "temperature_min": 297.15,
    "temperature_max": 299.82,
    "wind_velocity": 6.2,
    "rain_precipitation": null,
    "location": "http://localhost:4000/locations/1/",
    "url": "http://localhost:4000/minutely_measurement/312/"
  }
]
```

| Parâmetro | Descrição |
|:---------:|:---------:|
| location | Filtra dados pelo nome do local. (Ex: Gama, Ceilândia) |
| latitude | Filtra dados pela latitude do local. (Necessita do campo de longitude) |
| longitude | Filtra dados pela longitude do local. (Necessita do campo de latitude) |
| start_date | Filtra dados delimitando o período inicial para a coleta. (Necessita do campo end_date) |
| end_date | Filtra dados delimitando o período final para a coleta. (Necessita do campo start_date) |

## Previsão dos dados meteorológicos

Disponibiliza os dados diários coletados de cada localidade. Este endpoint tem uma peculiaridade de que ele só coleta dados de 3 em 3 horas, ou seja, sua coleta começa de 00:00 até sua última coleta, às 21:00, totalizando 7 medidas para cada dia.


**GET**: http://localhost:4000/forecast_measurement/

```json
[
  {
    "id": 344,
    "collection_time": "2019-09-16T21:00:00",
    "temperature": 294.37,
    "temperature_min": 294.0,
    "temperature_max": 294.37,
    "wind_velocity": 1.47,
    "rain_precipitation": null,
    "location": "http://localhost:4000/locations/1/",
    "url": "http://localhost:4000/forecast_measurement/344/"
  },
  {
     "id": 345,
     "collection_time": "2019-09-16T00:00:00",
     "temperature": 291.858,
     "temperature_min": 291.858,
     "temperature_max": 291.858,
     "wind_velocity": 2.08,
     "rain_precipitation": null,
     "location": "http://localhost:4000/locations/1/",
     "url": "http://localhost:4000/forecast_measurement/345/"
  }
]
```

| Parâmetro | Descrição |
|:---------:|:---------:|
| location | Filtra dados pelo nome do local. (Ex: Gama, Ceilândia) |
| latitude | Filtra dados pela latitude do local. (Necessita do campo de longitude) |
| longitude | Filtra dados pela longitude do local. (Necessita do campo de latitude) |
| start_date | Filtra dados delimitando o período inicial para a coleta. (Necessita do campo end_date) |
| end_date | Filtra dados delimitando o período final para a coleta. (Necessita do campo start_date) |

## Referências

> OpenWeather, **We Deliver 2 Billion Forecasts Per Day**, Disponível em: <https://openweathermap.org/api>
