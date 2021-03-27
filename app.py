from fastapi import FastAPI
from pydantic import BaseModel
from stock_sentiment_analysis.main import test
from CONSTANTS import COUNTVECTOR, RANDOMCLASSIFIER

app = FastAPI(
    title='SentimentAnalysis'

)


class StockSentimentAnalysis(BaseModel):
    name: list


@app.post('/stocksentimentanalysis/predict')
def predict_stock_sentiment(news: StockSentimentAnalysis):
    result = test(news, COUNTVECTOR, RANDOMCLASSIFIER)
    if result == 0:
        return "Share price will go down"
    return "Share price will go up"
