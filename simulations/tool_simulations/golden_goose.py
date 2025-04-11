import datetime

import uvicorn
from fastapi import FastAPI

from configs.goose_config import TEST_TICKERS
from models.goose.engine.model import run_goose_engine

goose_api = FastAPI()

def test_goose_engine():
    end_date = datetime.datetime.now(datetime.UTC)
    start_date = datetime.datetime.combine(
            end_date.date().replace(year=end_date.year - 1),
            datetime.time.min,
            tzinfo=datetime.UTC
        )
    run_goose_engine(tickers=TEST_TICKERS, start_date=start_date, end_date=end_date)

@goose_api.get("/goose/test")
async def test_golden_goose():
    try:
        test_goose_engine()
    except Exception as e:
        return f"{e}"
    return "GOOSE IS FINISHED!"


"""

follow the ideas from the todo and the stuff below.

[ ] 
[ ] Hold S&P 500 for x years but also day trade with single stocks of the 500 to day trade
[ ] Distribute the 500 stocks to x agents (prism-drones)
    - On a day, a worker does 1-5 active trades a day with 5-10 tickers
    - On a week, a worker does rotation of tickers 
    - On a month, a worker sees a total max of 30-60 tickers
    - Thus assume 12-16 agents for max, 3-12 for team(s) of workers and managers under the GoldenGoose division
[ ] Do simulations of all years from the data
[ ] From satisfactory results, then apply with prism-drones as workers

"""

def run_golden_goose(is_endpoint=False):
    if is_endpoint:
        uvicorn.run(goose_api, host="127.0.0.1", port=8000)
    else:
        test_goose_engine()
