import alpaca_trade_api as tradeapi
from config import alpaca_key, alpaca_secret

api = tradeapi.REST(alpaca_key, alpaca_secret, api_version='v2')

# Get a list of all active assets.
active_assets = api.list_assets(status='active')

# Filter the assets down to just those on NASDAQ.
nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
print(nasdaq_assets)
