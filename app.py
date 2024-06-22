import yfinance as yf
import pandas as pd
import streamlit as st

# 주요 티커 리스트 (예시)
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA","TSLA"]

def get_market_cap(ticker):
    stock = yf.Ticker(ticker)
    market_cap = stock.info['marketCap']
    return market_cap

# 데이터프레임 생성
data = {
    'Ticker': tickers,
    'MarketCap': [get_market_cap(ticker) for ticker in tickers]
}
df = pd.DataFrame(data)

# 시가총액 기준으로 데이터프레임 정렬
df = df.sort_values(by='MarketCap', ascending=False)

st.title('NASDAQ Companies Market Cap Comparison')
st.write('각 티커명의 폰트 크기는 시가총액에 비례합니다.')

for index, row in df.iterrows():
    st.markdown(
        f"<div style='font-size: {row.MarketCap / 1.9e10}px; line-height: 0.8;'>{row.Ticker}</div>",
        unsafe_allow_html=True
    )
