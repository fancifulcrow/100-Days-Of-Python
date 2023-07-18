import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

stock_api_parameters = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK,
    "apikey" : stock_api_key,
}

news_api_parameters = {
    "apikey" : news_api_key,
    "q" : COMPANY_NAME,
    "from" : datetime.now() - timedelta(days=1),
    "to" : datetime.now(),
    "sortBy" : "relevancy",
}

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_api_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

stock_response.close()

yesterday = datetime.strftime(datetime.now() - timedelta(days=1), "%Y-%m-%d")
day_before_yesterday = datetime.strftime(datetime.now() - timedelta(days=2), "%Y-%m-%d")


if yesterday in stock_data and day_before_yesterday in stock_data:
    yesterday_close = float(stock_data[yesterday]["4. close"])
    day_before_yesterday_close = float(stock_data[day_before_yesterday]["4. close"])

    stock_price_increase = ((yesterday_close - day_before_yesterday_close) / 100) * day_before_yesterday_close

    # print(stock_price_increase)

    if abs(stock_price_increase) > 5:
        ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
        # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
        #HINT 1: Think about using the Python Slice Operator
        news_response = requests.get(url=NEWS_ENDPOINT, params=news_api_parameters)
        news_response.raise_for_status()
        news_data = news_response.json()["articles"][:3]

        news_response.close()

        # print(news_data)

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        # Send a separate message with each article's title and description to your phone number. 
        #HINT 1: Consider using a List Comprehension.
        
        message = ""

        if stock_price_increase > 0:
            message += f"Subject: TSLA 🔺{round(abs(stock_price_increase), 2)}% \n\n "
        else:
            message += f"Subject: TSLA 🔻{round(abs(stock_price_increase), 2)}% \n\n "

        for article in news_data:
            message += f"Headline:{article['title']}\nBrief:{article['description']}\n"

        # print(message)

        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=message
            )




#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

