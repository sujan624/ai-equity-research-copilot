from data.stocks import get_stock_data
from data.news import get_company_news

def analyze_company(ticker: str):
    stock_data = get_stock_data(ticker)
    news_data = get_company_news(ticker)

    analysis = {
        **stock_data,
        "valuation_comment": _valuation_comment(stock_data),
        "news": news_data
    }

    return analysis


def _valuation_comment(data):
    price = data.get("price")
    pe = data.get("pe_ratio")

    if pe is None:
        return "No PE data available"

    if pe < 20:
        return "Potentially undervalued based on PE"
    elif pe < 35:
        return "Fair valuation range"
    else:
        return "Potentially overvalued"