# Import library for fetching Elspot data
from nordpool import elspot #, elbas
from pprint import pprint


# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()


# Fetch hourly Elspot prices for Kr.sand and print the resulting dictionary
hourValues = prices_spot.hourly(areas=['Kr.sand'])['areas']['Kr.sand']['values']


# sorted dictionary with lowest values first
valueHourDictionary = {}
for hourValue in hourValues:
   currentPrice = hourValue['value']
   currentTime=(hourValue['start'].hour) 
   valueHourDictionary[currentPrice] = currentTime

# sort hours
myKeys = list(valueHourDictionary.keys())
myKeys.sort()
sorted_lowest_prices_first = {i: valueHourDictionary[i] for i in myKeys}

for price, time in sorted_lowest_prices_first.items():
   pprint('current price is ' + str(price) + ' starting at ' + str(time)) 




# lowest and highest version
# minPrice = 100000
# maxPrice = 0
# for hourValue in hourValues:
#    currentPrice = hourValue['value']
#    currentTime=(hourValue['start'].hour) 
#    if currentPrice < minPrice:
#        minPrice = currentPrice
#        minTime = currentTime
#    if currentPrice > maxPrice:
#        maxPrice = currentPrice
#        maxTime  = currentTime
    
#    pprint('current price is ' + str(currentPrice) + ' starting at ' + str(hourValue['start'].hour)) 
  
# pprint('Max price is ' + str(maxPrice) + ' starting at ' + str(maxTime)) 
# pprint('Min price is ' + str(minPrice) + ' starting at ' + str(minTime)) 

