# import packages
import xarray as xr
from xskillscore import rmse

def import_data(ds):
    """Importa dados em formato .nc para leitura 
    de variáveis 3D/4D

    Args:
        ds (Dataset): nome do arquivo

    Returns:
        Dataset: guarda o arquivo em uma variável
    """
    ds = xr.open_dataset(f'{ds}')
    return ds


def rename_vars(ds1, ds2):
    """A partir de data_vars.items() é possível encontrar o 
    nome das variáveis e coordenadas do arquivo. Utilizando
    essa função, os valores podem ser comparados e caso, sejam
    diferentes, o segundo arquivo recebe o nome da variável
    do primeiro arquivo. 

    Args:
        ds1 (Dataset): observation.nc
        ds2 (Dataset): forecast.nc

    Returns:
        Dataset: retorna o forecast.nc alterado, porém
        é necessária aplicá-la a variável 'forecast' 
        para sobrepor o nome da variável
    """
    if ds1.data_vars.items() == ds2.data_vars.items():
        pass
    else:
        for var1, i in ds1.data_vars.items():
            for var2, j in ds2.data_vars.items():
                ds2 = ds2.rename({f'{var2}': f'{var1}'})
    return ds2


def equal_coords(ds1, ds2):
    """Ao analisar os arquivos, observa-se que
    as coordenadas estão diferentes em casas
    decimais. Por boa prática, os valores dos
    eixos são igualados, de forma que o padrão
    vem dos dados observados.

    Args:
        ds1 (Dataset): observation.nc
        ds2 (Dataset): forecast.nc
    """
    for i in ['lat', 'lon']:
        if ds2.equals(ds1) == False:
            ds2[i] = ds1[i]


def kelvin2celsius(ds1, ds2):
    """Como os dados são de São Paulo, é muito difícil que
    chegue a ºC negativo, então por conveção os Arrays foram
    comparados com valores maiores que 273.15 K equivalente a
    0 ºC. Então, quando são encontrados esses valores, 
    a conversão é feita.

    Args:
        ds1 (Dataset): observation.nc
        ds2 (Dataset): forecast.nc
    """
    if ds1 >= 273.15 == True:
        ds1['temperatura'] = ds1['temperatura'] - 273.15
    else:
        print('Os valores do primeiro arquivo estão em °C')
    if ds2.__ge__(273.15) == True:
        ds2['temperatura'] = ds2['temperatura'] - 273.15
    else:
        print('Os valores do segundo arquivo estão em °C')


def output_rmse_6h(ds1, ds2):
    """Transforma a escala dos dados horário para cada 6 horas.
    RMSE é calculado para cada intervalo de 6 horas e também, é
    criado um novo dataset com esses dados e salvo em .nc

    Args:
        ds1 (Dataset): observation.nc
        ds2 (Dataset): forecast.nc

    Returns:
        Dataset: variável com o RMSE a cada 6 horas
    """
    ds1_6h = ds1.resample(time='6h').mean()
    ds2_6h = ds2.resample(time='6h').mean()
    rmse_6h = rmse(ds1_6h, ds2_6h, dim='time').\
        assign_coords(time=(ds1_6h['time'])).\
        rename_vars({'temperatura': 'rmse'})
    
    print('Gerando output .nc')
    rmse_6h.to_netcdf('RMSE_6hourly.nc', 'w')
    
    return rmse_6h


# processing data
observation = import_data('observation.nc')
forecast = import_data('forecast.nc')

print('observation', observation.dims)
print('forecast', forecast.dims)

forecast = rename_vars(observation, forecast)

equal_coords(observation, forecast)

kelvin2celsius(observation, forecast)

rmse_6h = output_rmse_6h(observation, forecast)
print(rmse_6h.values)
