from services.analyzer import analyze_company

def main():
    ticker = "NVDA"
    result = analyze_company(ticker)

    print("\n=== AI EQUITY RESEARCH SNAPSHOT ===\n")

    for k, v in result.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()