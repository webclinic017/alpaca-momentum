import alpaca_trade_api as tradeapi
import rx
from typing import Protocol
from rx import Observable
from abc import abstractmethod
from app.config.config import alpaca_key, alpaca_secret
from app.repository.alpaca.models import MarketStatus

api = tradeapi.REST(alpaca_key, alpaca_secret, api_version='v2')

class IAlpacaService(Protocol):

    @abstractmethod
    def get_clock(self) -> Observable:
        pass

    @abstractmethod
    def get_active_assets(self) -> Observable:
        pass


class AlpacaService(IAlpacaService):

    def get_clock(self) -> Observable:
        return rx.of(api.get_clock())

    def get_active_assets(self) -> Observable:
        return rx.of(api.list_assets(status='active'))
