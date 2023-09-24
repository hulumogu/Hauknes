# Import library for fetching Elspot data
from nordpool import elspot #, elbas
from pprint import pprint


# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()


# Fetch hourly Elspot prices for Kr.sand and print the resulting dictionary
hourValues = prices_spot.hourly(areas=['Kr.sand'])['areas']['Kr.sand']['values']
#pprint(hourValues)
minPrice = 100000
maxPrice = 0
for hourValue in hourValues:
   currentPrice = hourValue['value']
   if currentPrice < minPrice:
       minPrice = currentPrice
   if currentPrice > maxPrice:
       maxPrice = currentPrice
    
   pprint('current price is ' + str(currentPrice) + ' starting at ' + str(hourValue['start'].hour)) 
  
pprint('Max price is ' + str(maxPrice)) 
pprint('Min price is ' + str(minPrice)) 

