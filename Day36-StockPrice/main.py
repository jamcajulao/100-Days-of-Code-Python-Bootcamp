# STOCK NEWS
"""Sends 3 latest news about the specified company
when there is significant change in their stock price"""

import requests

# |-------------------- SETUP --------------------|

# input your specified company name and ticker symbol
STOCK_TICKER = ""
COMPANY_NAME = ""

# STOCK API - register for a free account on https://www.alphavantage.co to get your API key
AV_API_KEY = ""
# NEWS API - register for a free account on https://newsapi.org to get your API key
NEWS_API_KEY = ""
# TELEGRAM BOT - create a free bot on telegram using @BotFather to get Token and chatID
TG_BOT_TOKEN = ""
TG_BOT_CHATID = ""

# |-------------------- PARAMETERS --------------------|
AV_URL = "https://www.alphavantage.co/query"
AV_PARAMETERS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_TICKER,
    "apikey": AV_API_KEY,
    "outputsize": "compact",
}
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_PARAMETERS = {
    "q": COMPANY_NAME,
    "searchIn": "title,description",
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": NEWS_API_KEY,
    }

# |-------------------- CHECK CHANGE IN STOCK --------------------|
av_response = requests.get(AV_URL, AV_PARAMETERS)
av_response.raise_for_status()

close_ytd = float(list(av_response.json()["Time Series (Daily)"].items())[0][1]["4. close"])
close_previous = float(list(av_response.json()["Time Series (Daily)"].items())[1][1]["4. close"])
change_percent = round((close_ytd - close_previous) / close_previous * 100, 2)

if change_percent > 5 or change_percent < -5:
    if change_percent > 0:
        emoji = "🔺"
    else:
        emoji = "🔻"

    # |-------------------- GET LATEST NEWS --------------------|
    response_news = requests.get(NEWS_URL, NEWS_PARAMETERS)
    response_news.raise_for_status()
    news = response_news.json()["articles"]

    for num in range(0, 3):
        headline = news[num]["title"]
        brief = news[num]["description"]
        url = news[num]["url"]

        # |-------------------- SEND MESSAGE --------------------|
        message = f"{STOCK_TICKER}: {emoji} {change_percent}%\n\nHeadline: {headline}\n\nBrief: {brief}\n\nLink: {url}"
        tg_url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id={TG_BOT_CHATID}&text={message}"
        requests.get(tg_url).json()
