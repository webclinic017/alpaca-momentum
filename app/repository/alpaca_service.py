import alpaca_trade_api as tradeapi
import rx
from rx import operators as ops, Observable
from app.config.config import alpaca_key, alpaca_secret

api = tradeapi.REST(alpaca_key, alpaca_secret, api_version='v2')


def get_active_assets() -> Observable:
    """
    Returns all active assets as an Rx Observable
    """

    # Get a list of all active assets.
    active_assets = api.list_assets(status='active')
    return rx.of(active_assets)
