import csv
from datetime import datetime, timedelta
import requests
from pathlib import Path

import config


def load_env(env_path=".env"):
    path = Path(env_path)
    if not path.exists():
        raise FileNotFoundError(f"Environment file not found: {env_path}")

    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip()

    return env


def get_env_value(key, env_path=".env"):
    env = load_env(env_path)
    value = env.get(key)
    if not value:
        raise ValueError(f"Missing value for {key} in {env_path}")
    return value


def get_alpaca_data(symbol, env_path=".env"):
    """Descarga datos de barras de Alpaca usando la configuración en config.py."""
    if not symbol:
        raise ValueError("El símbolo debe ser un valor no vacío.")

    timeframe = config.TIMEFRAME
    timeframe_map = {
        "1m": "1Min",
        "5m": "5Min",
        "15m": "15Min",
        "30m": "30Min",
        "1h": "1Hour",
        "1d": "1Day",
    }
    timeframe = timeframe_map.get(timeframe.lower(), timeframe)

    start = config.ALPACA_START_DATE
    end = config.ALPACA_END_DATE
    if "T" not in start:
        start = f"{start}T00:00:00Z"
    if "T" not in end:
        end_date = datetime.fromisoformat(config.ALPACA_END_DATE)
        end = f"{(end_date + timedelta(days=1)).date().isoformat()}T00:00:00Z"

    api_key = get_env_value("API_KEY", env_path)
    secret_key = get_env_value("SECRET_KEY", env_path)

    base_url = config.ALPACA_API_BASE_URL.rstrip("/")
    endpoint = f"{base_url}/stocks/{symbol}/bars"
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key,
    }
    params = {
        "timeframe": timeframe,
        "start": start,
        "end": end,
    }

    response = requests.get(endpoint, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def save_data_to_csv(data, symbol, output_dir="data"):
    """Guarda los datos descargados en un archivo CSV dentro de la carpeta data."""
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    if isinstance(data, dict) and "bars" in data:
        bars = data["bars"]
    elif isinstance(data, list):
        bars = data
    else:
        raise ValueError("Formato de datos inesperado para guardar en CSV.")

    if not bars:
        raise ValueError("No hay barras disponibles para guardar.")

    csv_path = path / f"{symbol}_{config.ALPACA_START_DATE}_{config.ALPACA_END_DATE}_{config.TIMEFRAME}.csv"
    fieldnames = list(bars[0].keys())

    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for bar in bars:
            writer.writerow(bar)

    return csv_path


if __name__ == "__main__":
    symbol = "ACM"
    data = get_alpaca_data(symbol)
    csv_file = save_data_to_csv(data, symbol)
    print(f"Datos de {symbol} guardados en: {csv_file}")
