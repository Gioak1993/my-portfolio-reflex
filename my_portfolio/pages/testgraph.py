import reflex as rx
from my_portfolio.APIs.StockApi import FmpApi
import plotly.graph_objects as go
from my_portfolio.components.navbar import nav_bar


fmp_api = FmpApi()


def graph( stock:str, from_date:str, to_date:str):
        data = fmp_api.historical_data(stock, from_date, to_date)
        symbol = data['symbol']
        dates = [entry['date'] for entry in data['historical']]
        close_prices = close = [entry['close'] for entry in data['historical']]
        change_percent = [entry['changePercent'] for entry in data['historical']]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=close_prices, mode='lines', name='Close Price'))
        fig.update_layout(title='AAPL Close Prices', xaxis_title='Date', yaxis_title='Close Price')
        return fig


def stocks_page ():
    return rx.vstack(
        nav_bar(),
        rx.center(
        rx.plotly(data = graph('AAPL', '2024-04-01', '2024-04-11'), height="400px"),
        align='center',
        )
    )

