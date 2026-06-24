from find_SL_TP import calculate_sl_tp


def main():
    entry_price = 100.0
    stop_loss_price = 98.0

    result = calculate_sl_tp(entry_price, stop_loss_price)

    print("Resultados de la operación:")
    print(f"Precio de entrada: {result['entry_price']}")
    print(f"Precio de stop loss: {result['stop_loss_price']}")
    print(f"Precio de take profit: {result['take_profit_price']}")
    print(f"Lotes recomendados: {result['lot_size']:.4f}")
    print(f"Monto de riesgo: {result['risk_amount']}")
    print(f"Porcentaje de riesgo: {result['risk_percent'] * 100}%")
    print(f"Porcentaje de TP: {result['tp_percent'] * 100}%")


if __name__ == "__main__":
    main()
