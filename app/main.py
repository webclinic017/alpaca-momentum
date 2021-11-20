import repository.alpaca_service as alpaca


def print_nasdaq_assets(active_assets):
    nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
    print(nasdaq_assets)


def main():
    observable = alpaca.get_active_assets()
    # Filter the assets down to just those on NASDAQ.
    observable.subscribe(lambda active_assets: print_nasdaq_assets(active_assets))
