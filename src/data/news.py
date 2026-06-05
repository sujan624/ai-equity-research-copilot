from pprint import pprint
import yfinance as yf


def get_company_news(ticker: str) -> list:
    raw_news = yf.Ticker(ticker).news

    normalized_news = []

    for article in raw_news[:5]:
        content = article.get("content", {})

        news_item = {
            "title": content.get("title"),
            "summary": content.get("summary"),
            "source": content.get("provider", {}).get("displayName"),
            "published": content.get("pubDate"),
            "url": content.get("canonicalUrl", {}).get("url")
        }

        normalized_news.append(news_item)

    return normalized_news

pprint(get_company_news("NVDA"))