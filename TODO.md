# TODO(s)

1. MOVE ALL GOOSE STUFF TO REPO
    - all engine, models, ui to new repo goose-engine-service
    - do the same for mood-engine-service since we're on it
    - setup prism-drone-service with PrismDrone and PrismDroneLite
      - PrismDroneLite(PrismDrone)
      - Just update once and a while back and forth to keep up with data
2. Fix the data scrappers to be dynamic
   - Try without data
   - Try with data
   - Try with both
   - Able to visualize all
   - data_sources:
     - solar_data
     - earth_data with version 1 weather_data
     - market_data with investor data_set
3. Make a model for investing and toy around. ask GPT on how to make it more robost for investor_data(_set)
4. Start with trading data_set model and figure out a valid solution with investor_data_set
    - Continue doing the following: golden_goose.py REMEMBER THE CONDITIONS
      - [ ] Hold S&P 500 for x years but also day trade with single stocks of the 500 to day trade
      - [ ] Distribute the 500 stocks to x agents (prism-drones)
        - On a day, a worker does 1-5 active trades a day with 5-10 tickers
        - On a week, a worker does rotation of tickers 
        - On a month, a worker sees a total max of 30-60 tickers
        - Thus assume 12-16 agents for max, 3-12 for team(s) of workers and managers under the GoldenGoose division
      - [ ] Do simulations of all years from the data
      - [ ] From satisfactory results, then apply with prism-drones as workers
