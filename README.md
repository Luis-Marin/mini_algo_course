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
