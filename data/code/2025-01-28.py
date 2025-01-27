import pandas as pd
import numpy as np

np.random.seed(42)

# 날짜 생성
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

# 5개 주식의 일별 수익률 생성
stocks = ["삼성전자", "SK하이닉스", "네이버", "카카오", "LG에너지솔루션"]
daily_returns = pd.DataFrame(
    np.random.normal(0.0001, 0.02, (len(dates), len(stocks))),
    columns=stocks,
    index=dates,
)

# 초기 가격 설정
initial_prices = {
    "삼성전자": 60000,
    "SK하이닉스": 120000,
    "네이버": 200000,
    "카카오": 50000,
    "LG에너지솔루션": 450000,
}

# 수익률을 가격으로 변환
prices = pd.DataFrame(index=dates, columns=stocks)
for stock in stocks:
    prices[stock] = initial_prices[stock] * (1 + daily_returns[stock]).cumprod()

# 포트폴리오 보유 수량
holdings = {
    "삼성전자": 100,
    "SK하이닉스": 50,
    "네이버": 30,
    "카카오": 200,
    "LG에너지솔루션": 10,
}

# CSV 파일로 저장
prices.to_csv("data/file/stock_prices.csv")
