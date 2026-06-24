Instalación

Para instalar automáticamente todas las librerías listadas en `requirements.txt` desde PowerShell:

```powershell
python -m pip install -r requirements.txt
```

Descripción del método `find_SL_TP`

El módulo `find_SL_TP.py` contiene la función `calculate_sl_tp(entry_price, stop_loss_price)`, que calcula:

- el tamaño de lote recomendado (`lot_size`)
- el precio de take profit (`take_profit_price`)
- el monto de riesgo en dinero (`risk_amount`)

La función toma como entrada:

- `entry_price`: el precio de entrada de la operación
- `stop_loss_price`: el precio de stop loss

Los porcentajes de riesgo y take profit se leen desde `config.py`:

- `ACCOUNT_SIZE`: tamaño de la cuenta
- `RISK_PERCENT`: porcentaje de la cuenta a arriesgar
- `TP_PERCENT`: porcentaje de take profit sobre el precio de entrada

Ejemplo de uso en `main.py`:

```python
from find_SL_TP import calculate_sl_tp

entry_price = 100.0
stop_loss_price = 98.0
result = calculate_sl_tp(entry_price, stop_loss_price)
```

Descripción del método `get_alpaca_data`

El módulo `get_alpaca_data.py` descarga datos de barras de Alpaca usando el endpoint configurado en `config.py` y las credenciales almacenadas en `.env`.

La función principal es:

- `get_alpaca_data(symbol, env_path=".env")`

Parámetros:

- `symbol`: símbolo del activo a descargar (por ejemplo `ACM`)
- `env_path`: ruta opcional del archivo `.env` donde se guardan `API_KEY` y `SECRET_KEY`

Los valores de fechas y timeframe se obtienen desde `config.py`:

- `ALPACA_START_DATE`: fecha de inicio de los datos
- `ALPACA_END_DATE`: fecha de fin de los datos
- `TIMEFRAME`: ventana temporal para las barras, por ejemplo `"1h"`

Ejemplo de uso:

```python
from get_alpaca_data import get_alpaca_data

result = get_alpaca_data("ACM")
print(result)
```

Asegúrate de tener en `.env` las credenciales de Alpaca:

```dotenv
API_KEY = <tu_api_key>
SECRET_KEY = <tu_secret_key>
```

Y de configurar las fechas y timeframe en `config.py` según tus necesidades.
