import quantopian.optimize as opt

# Called once at the start of the simulation.
def initialize(context):
    # Reference to the AAPL security.
    #context.aapl = sid(24)
    #context.stock = symbol('IBM')
    
    #SMA50 Function scheduled to run once per day at market open
    schedule_function(SMA50, date_rules.every_day(), time_rules.market_open())	
    
    #Specified Future is first parameter
    context.future = continuous_future('GC', offset=0, roll='calendar', adjustment='mul')

#Algorithm executes whenever there is a swing in the 50 Day Moving Average 
def SMA50(context,data):
    context.active = data.current(context.future, 'contract') #Active Trading Contract
    price_history = data.history(context.future, 'price', 50, '1d') #Futures Price History
    long_mavg = price_history.mean() #50 Day Moving Average
    current_price = data.current(context.future, 'price')
    if current_price > long_mavg: #If price > 50 Day Moving Average
        if context.portfolio.positions[context.active].amount == 0: #If no current positions
            weights = {context.active:1} #100% of Portfolio weight (Buy)
            order_optimal_portfolio(opt.TargetPortfolioWeights(weights), constraints = [])
            log.info("Buying")
            print(current_price,long_mavg,context.portfolio.positions[context.active].amount)    
    elif context.portfolio.positions[context.active].amount > 0: #If there are current positions
        weights = {context.active:0} #0% of Portfolio (Sell)
        order_optimal_portfolio(opt.TargetPortfolioWeights(weights), constraints = [])
        log.info("Selling")
        print(current_price,long_mavg,context.portfolio.positions[context.active].amount)

#Benchmark function to demonstrate gains if contract were to be held from start date to end date 
def Benchmark(context,data):
    context.active = data.current(context.future, 'contract')
    weights = {context.active:1} #100% of Portfolio (Buy)
    order_optimal_portfolio(opt.TargetPortfolioWeights(weights), constraints = [])
    