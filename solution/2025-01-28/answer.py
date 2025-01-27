import os
import pandas as pd
import numpy as np


def read_csv_data(filename):
    # Check if the file exists
    if not os.path.isfile(filename):
        return None

    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename, index_col=0)

    return df


def calculate_return(df):
    annaul_return = {}

    for col in df:
        annaul_return[col] = (df[col].iloc[-1] - df[col].iloc[0]) / df[col].iloc[0]

    total_return = sum(annaul_return.values()) / len(annaul_return)

    # 일별 수익률 계산
    return_trend = df.pct_change()

    # 변동성 계산
    daily_volatility = return_trend.std()
    annaul_volatility = daily_volatility * np.sqrt(252)

    return_trend = return_trend.mean(axis="columns")

    return annaul_return, total_return, return_trend, annaul_volatility


def main():
    df = read_csv_data("data/file/stock_prices.csv")
    if df is not None:
        annual_return, total_return, return_trend, annaul_volatility = calculate_return(
            df
        )

        # 결과 출력
        print("\n종목별 연 수익률:")
        for col, return_value in annual_return.items():
            print(f"{col}: {return_value:.2%}")

        print(f"\n전체 수익률 평균: {total_return:.2%}")

        print("\nReturn Trend:")
        print(return_trend.head())

        print(f"\nannual_volatility: \n{annaul_volatility}")


if __name__ == "__main__":
    main()
