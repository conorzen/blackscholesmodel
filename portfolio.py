import os
import polars as pl
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
alpha_api = os.getenv("ALPHA_VANTAGE_API_KEY")
open_ai_key = os.getenv("OPENAI_API_KEY")


class Portfolio:
    def __init__(self):
        self.symbols = ["IBM"]
        self.time_frame = 60

    def get_stock(self, symbols, time_frame):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbols}&interval={time_frame}min&apikey={alpha_api}"
        print(f"making request: {url}")
        r = requests.get(url)
        data = r.json()
        return data

    def get_all_stocks(self):
        all_data = []
        for symbol in self.symbols:
            data = self.get_stock(symbol, self.time_frame)
            all_data.append(data)
        return all_data

    def data_extract(self, data):
        print(f"datatype {type(data)}")
        print(
            f"Data keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}"
        )  # Debug line
        print(f"First 200 chars of response: {str(data)[:200]}")
        meta_data = data["Meta Data"]
        time_series = data["Time Series (60min)"]

        latest_time = next(iter(time_series))
        latest_data = time_series[latest_time]

        return {
            "symbol": meta_data["2. Symbol"],
            "timestamp": latest_time,
            "open": float(latest_data["1. open"]),
            "high": float(latest_data["2. high"]),
            "low": float(latest_data["3. low"]),
            "close": float(latest_data["4. close"]),
            "volume": int(latest_data["5. volume"]),
            "last_refreshed": meta_data["3. Last Refreshed"],
        }

    def data_clean(self):
        all_dfs =[]
        for symbol in self.symbols:
            data = self.get_stock(symbol, self.time_frame)
            clean_data = self.data_extract(data)
            df = pl.DataFrame([clean_data])
            all_dfs.append(df)
            print(df)

        return all_dfs


    def open_ai_analysis(self, df):
        client = OpenAI(api_key=open_ai_key)

        data_str = str(df)

        response = client.chat.completions.create(
            model="gpt-4",
            messages = [
                {
                    "role": "system",
                    "content": "You are a financial analyst. Analyse stock data and provide insights."
                },
                {
                    "role": "user",
                    "content": f"Analyze this stock data and provide insights: {data_str}"
                }
            ],
            max_tokens=500
        )
        
        analysis = response.choices[0].message.content
        print("Analysis:")
        print(analysis)
        return analysis



    def run_analysis(self):
        dfs = self.data_clean()
        for df in dfs:
            self.open_ai_analysis(df)

if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.run_analysis()

