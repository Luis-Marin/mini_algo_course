from config import ACCOUNT_SIZE, RISK_PERCENT, TP_PERCENT


def calculate_sl_tp(entry_price, stop_loss_price):
    """Calcula lotes y valor de take profit según la configuración.

    Args:
        entry_price (float): Precio de entrada.
        stop_loss_price (float): Precio de stop loss.

    Returns:
        dict: Valores calculados para la operación.
    """
    if entry_price == stop_loss_price:
        raise ValueError("El precio de entrada y el precio de stop loss no pueden ser iguales.")

    # Riesgo en dinero según el porcentaje de la cuenta
    risk_amount = ACCOUNT_SIZE * RISK_PERCENT
    # Diferencia de precio entre entrada y stop loss
    risk_per_unit = abs(entry_price - stop_loss_price)
    # Tamaño de lote aproximado
    lot_size = risk_amount / risk_per_unit
    # Precio de take profit basado en porcentaje de TP
    take_profit_price = entry_price + entry_price * TP_PERCENT

    return {
        "entry_price": entry_price,
        "stop_loss_price": stop_loss_price,
        "take_profit_price": take_profit_price,
        "lot_size": lot_size,
        "risk_amount": risk_amount,
        "risk_percent": RISK_PERCENT,
        "tp_percent": TP_PERCENT,
    }
