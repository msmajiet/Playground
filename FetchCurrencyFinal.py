#read json file
import json
import re
import urllib2

'''
#Example json data from website
#Test data
json_data = {u'executionTime': 77,
u'timeStamp': 1523269413,
u'licenseMessage': u'Data Retrieved From www.ExchangeRateLab.com - Under license (Not for financial/professional use)',
u'rates':
    [{u'to': u'AUD', u'rate': 1.296462},
    {u'to': u'CAD', u'rate': 1.268116},
    {u'to': u'CNY', u'rate': 6.322116},
    {u'to': u'EUR', u'rate': 0.843812},
    {u'to': u'GBP', u'rate': 0.699438},
    {u'to': u'INR', u'rate': 65.07349},
    {u'to': u'JPY', u'rate': 109.720613},
    {u'to': u'USD', u'rate': 1.0}],
u'baseCurrency': u'USD'}
'''

# Fetch the json file
def fetch_currency():
    json_data = urllib2.urlopen('http://api.exchangeratelab.com/api/current?apikey=CB158AE07B156436822E98E0DE272EBA')
    json_obj = json.load(json_data)
    return json_obj

#Validate the currency
def validate_currency(currency):
    currency_validator = r"[A-Z]{3}"
    valid_currency = re.search(currency_validator, currency)
    if (valid_currency):
        return True
    else:
        return False

#Validate the amount
def validate_amount(amt):
    amount_validator = r"\d+\.?\d*"
    valid_amount = re.search(amount_validator, amt)
    if (valid_amount):
        return True
    else:
        return False

def targetrate(target_currency):
    json_data = fetch_currency()
    rate_data = json_data["rates"]
    for item in rate_data:
        target = item["to"]
        if (target == target_currency):
            rate = item["rate"]
    return rate

# Retrieve input
print("Enter the source currency:")
source = raw_input()
print("Enter the target currency:")
target = raw_input()
print("Enter the amount to convert")
amount = raw_input()
print ("target", target)
print ("source", source)
print ("amount", amount)

t_rate= targetrate(target)
print(t_rate)
converted_amount = float(amount) * t_rate
print ("The converted amount", converted_amount)