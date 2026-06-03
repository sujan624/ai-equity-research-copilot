import yfinance as yf

def analyze_company(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info

    data = {
        "company": info.get("longName"),
        "sector": info.get("sector"),
        "market_cap": info.get("marketCap"),
        "price": info.get("currentPrice"),
        "forward_pe": info.get("forwardPE"),
        "52_week_high": info.get("fiftyTwoWeekHigh"),
        "52_week_low": info.get("fiftyTwoWeekLow"),
    }

    return data

def main():
    ticker = "AAPL"
    result = analyze_company(ticker)

    print("\n=== EQUITY RESEARCH SNAPSHOT ===\n")
    for k, v in result.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()