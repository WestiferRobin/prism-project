import uvicorn
from fastapi import FastAPI

from configs.goose_config import TEST_TICKERS
from models.goose.engine.model import run_goose_engine

goose_api = FastAPI()

@goose_api.get("/goose/test")
async def test_golden_goose():
    try:
        run_goose_engine(tickers=TEST_TICKERS)
    except Exception as e:
        return f"{e}"
    return "GOOSE IS FINISHED!"


"""

follow the ideas from the todo and the stuff below.

1. Hold S&P 500 for x years but also day trade with single stocks of the 500 to day trade
2. Distribute the 500 stocks to x agents (prism-drones)
    - On a day, a worker does 1-5 active trades a day with 5-10 tickers
    - On a week, a worker does rotation of tickers 
    - On a month, a worker sees a total max of 30-60 tickers
    - Thus assume 12-16 agents for max, 3-12 for team(s) of workers and managers under the GoldenGoose division
3. Do simulations of all years from the data
4. From satisfactory results, then apply with prism-drones as workers

"""

def run_golden_goose():
    uvicorn.run(goose_api, host="127.0.0.1", port=8000)
