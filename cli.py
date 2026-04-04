import argparse
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logging

setup_logging()

print("BOT STARTED")  # DEBUG

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_side(args.side)
    validate_order_type(args.type)

    if args.type == "LIMIT" and not args.price:
        raise ValueError("Price required for LIMIT order")

    print("\nOrder Summary")
    print(vars(args))

    print("Sending order...")

    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    if response:
        print("\nSUCCESS")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
    else:
        print("\nFAILED")

except Exception as e:
    print("ERROR:", str(e))
