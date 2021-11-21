from alpaca_trade_api.entity import Clock

from app.repository.alpaca.alpaca_service import AlpacaService
from app.repository.alpaca.models.MarketStatus import MarketStatus

alpaca = AlpacaService()


def __get_active_assets__():
    assets_observable = alpaca.get_active_assets()
    # TODO: Map to local object, override __str__
    assets_observable.subscribe(lambda assets: print(assets))


def __fetch_active_assets_if_open__(clock: Clock):
    market_status = MarketStatus(clock.timestamp, clock.is_open, clock.next_open, clock.next_close)
    if market_status.is_open:
        __get_active_assets__()
    else:
        print(market_status)


def main():
    # Get the market status from the alpaca clock
    clock_observable = alpaca.get_clock()
    # If this call succeeds, make use of the market status to either download active assets or pass
    clock_observable.subscribe(lambda clock: __fetch_active_assets_if_open__(clock))
