# Import library for fetching Elspot data
from nordpool import elspot #, elbas
from pprint import pprint


# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()


# Fetch hourly Elspot prices for Kr.sand and print the resulting dictionary
hourValues = prices_spot.hourly(areas=['Kr.sand'])['areas']['Kr.sand']['values']


# # sorted dictionary with lowest values first
# valueHourDictionary = {}
# for hourValue in hourValues:
#    currentPrice = hourValue['value']
#    currentTime=(hourValue['start'].hour) 
#    valueHourDictionary[currentPrice] = currentTime

# # sort hours
# myKeys = list(valueHourDictionary.keys())
# myKeys.sort()
# sorted_lowest_prices_first = {i: valueHourDictionary[i] for i in myKeys}

# for price, time in sorted_lowest_prices_first.items():
#    pprint('current price is ' + str(price) + ' starting at ' + str(time)) 




# #lowest and highest version
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

#lowest subsequent result
sizeHourValues = len(hourValues) 
if sizeHourValues > 2:   
    hourValue1 = hourValues[0]
    hourValue2 = hourValues[1]
    minPrice1 = hourValue1['value'] 
    minPrice2 = hourValue2['value']
    minTime1 = hourValue1['start'].hour 
    minTime2 = hourValue2['start'].hour

    pprint('current price is ' + str(minPrice1) + ' starting at ' + str(minTime1)) 
    pprint('current price is ' + str(minPrice2) + ' starting at ' + str(minTime2)) 

    for index in range(2, sizeHourValues):
        lastValue = hourValues[index-1]
        currentValue = hourValues[index]
        if minPrice1 > lastValue['value'] and minPrice2 > currentValue['value']:
            minPrice1 = lastValue['value']
            minPrice2 = currentValue['value']
            minTime1 = lastValue['start'].hour 
            minTime2 = currentValue['start'].hour 

    
        currentPrice = currentValue['value']
        currentTime=(currentValue['start'].hour) 
        pprint('current price is ' + str(currentPrice) + ' starting at ' + str(currentTime)) 
  
pprint('Min price1 is ' + str(minPrice1) + ' starting at ' + str(minTime1)) 
pprint('Min price2 is ' + str(minPrice2) + ' starting at ' + str(minTime2)) 

