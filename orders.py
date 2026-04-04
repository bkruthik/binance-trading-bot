import logging
from .client import get_client

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        print("➡️ Inside place_order")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        print("✅ Order placed")
        logging.info(f"Response: {order}")
        return order

    except Exception as e:
        print("❌ ORDER ERROR:", str(e))
        logging.error(f"Error: {str(e)}")
        return None