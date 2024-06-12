import pandas as pd
import json
data = pd.read_excel("C:/sourcecode/New folder/sample.xlsx", sheet_name="Prices")
json_result = data.to_dict(orient='records')
#print(json_result)
# Transform the list of dictionaries into the desired format without using a nested dictionary
transformed_result = []
for item in json_result:
    commodity = item.pop("Commodity")
    size = item.pop("Size")
    currency = item.pop("Currency")
    unit = item.pop("Unit")
    yearly_average = item.pop("Yearly Average")
    monthly_prices = {month: item[month] for month in item}
    
    transformed_result.append({
        commodity: {
            "Unit": unit,
            "Size": size,
            "currency": currency,
            "MonthlyPrices": monthly_prices,
            #"YearlyAverage": yearly_average
   }
    })

# Print the transformed JSON result
#print(transformed_result)

print(json.dumps(transformed_result, indent=4))

# Save the transformed JSON result to a file
with open('transformed_output.json', 'w') as json_file:
    json.dump(transformed_result, json_file, indent=4)