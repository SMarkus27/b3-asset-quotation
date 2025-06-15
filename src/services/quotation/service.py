import requests
from decouple import config
from sqlalchemy import select

from src.core.config.extensions import db
from src.models.entities.assets_quotation import AssetsQuotation


class QuotationService:

    @classmethod
    def save(cls):

        tickers = ["ITUB3","XPML11", "SAPR11", "BBSE3", "WEGE3",
                    "EGIE3", "KNSC11","KNCR11", "BTCI11", "VISC11",
                   "XPLG11", "KDIF11", "JURO11", "IFRA11", "LVBI11",
                    "BRCR11", "PVBI11","ALZR11","GARE11","TAEE3"]
        for ticker in tickers:
            price = cls.get_asset(ticker)

            query = (
                select(AssetsQuotation).where(AssetsQuotation.ticker == ticker)
            )
            quotation = db.session.execute(query).scalar_one_or_none()

            if quotation is None:

                quotation = AssetsQuotation(
                    ticker=ticker,
                    price=price
                )
                db.session.add(quotation)
            else:
              quotation.price = price

        db.session.commit()
        return "cotação realizada com sucesso"



    @classmethod
    def get_asset(cls, ticker: str) -> dict:
        url = config("B3_URL")
        data = requests.get(f"{url}/{ticker}")
        price = data.json()["Trad"][0]["scty"]["SctyQtn"]["curPrc"]
        return price



