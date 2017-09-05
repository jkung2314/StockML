# Called once at the start of the simulation.
def initialize(context):
    # Reference to the AAPL security.
    context.stock = symbol(‘AAPL’)

    #SMA50 Function scheduled to run once per day at market open
    schedule_function(SMA50, date_rules.every_day(), time_rules.market_open())

#Algorithm executes whenever there is a swing in the 50 Day Moving Average 
def SMA50(context,data):
    price_history = data.history(context.stock, 'price', 50, '1d')
    long_mavg = price_history.mean() #50 Day Moving Average
    current_price = data.current(sid(24), 'price')
    if current_price > long_mavg: #If price > 50 Day Moving Average
        if context.portfolio.positions_value == 0: #If no current positions
        	order_target_percent(context.stock, 1.0) #100% of Portfolio weight (Buy)
       		log.info("Buying")
    		print(current_price,long_mavg)            
    elif context.portfolio.positions_value > 0: #If there are current positions
    	order_target_percent(context.stock, 0) #0% of Portfolio (Sell)
    	log.info("Selling")
        print(current_price,long_mavg)

#Benchmark function to demonstrate gains if stock was to be held from start date to end date
def Benchmark(context,data):
    order_target_percent(context.stock, 1.0)