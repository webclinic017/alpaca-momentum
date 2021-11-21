from app.repository.alpaca.alpaca_service import AlpacaService
from app.repository.alpaca.models.MarketStatus import MarketStatus
from app.usecase import fetch_active_assets

alpaca = AlpacaService()


# def print_nasdaq_assets(active_assets):
#     nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
#     print(nasdaq_assets)

def print_market_status(clock):
    # TODO: Why does this not know what the properties are despite the type hint?
    mapped = MarketStatus(clock.timestamp, clock.is_open, clock.next_open, clock.next_close)
    print(mapped)


def print_current_market_status():
    clock_observable = alpaca.get_clock()
    clock_observable.subscribe(lambda clock: print_market_status(clock))


def main():
    fetch_active_assets.main()


main()
