# External Imports
import alpaca_trade_api as alpaca
from ratelimit import limits, sleep_and_retry
from dataclasses import dataclass

# Internal Imports
from config import alpaca_key, alpaca_secret, alpaca_url

# Limit API Calls to 200 per minute
calls = 200
rate_limit = 60


@sleep_and_retry
@limits(calls=calls, period=rate_limit)
def check_limit():
    # Empty function to throttle calls to API
    return None


def get_alpaca_assets():
    api = alpaca.REST(alpaca_key, alpaca_secret, alpaca_url)

    # Get a list of all active assets.
    active_assets = api.list_assets(status='active')

    # Filter the assets down to just those on NASDAQ.
    applicable_assets = [a for a in active_assets if a.shortable is True and a.fractionable is True]
    return applicable_assets


@dataclass
class assetMapping:
    """Class for mapping asset names and symbols from Alpaca."""
    name: str
    symbol: str

    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def store_symbol(self, name, symbol) -> dict:
        return {self.name:self.symbol}

for asset in get_alpaca_assets():
    assetMapping.store_symbol(asset)



