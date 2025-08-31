import csv

# Hardcoded stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2800, "MSFT": 330, "AMZN": 140}

def stock_portfolio():
    portfolio = {}
    total_investment = 0

    print("📊 Stock Portfolio Tracker")
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue

        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    # Calculate total investment
    for stock, qty in portfolio.items():
        total_investment += stock_prices[stock] * qty

    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}")

    print("\n💰 Total Investment Value:", total_investment)

    # Save results to CSV
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, qty in portfolio.items():
            writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
        writer.writerow(["Total", "", "", total_investment])
    print("✅ Portfolio saved to portfolio.csv")

if __name__ == "__main__":
    stock_portfolio()
