import rdiFigs
import requests as rq

# TODO: get actual key and password
# TODO: find general API URL and map special cases to different uses following https://fdc.nal.usda.gov/api-guide.html
apiKey = "DEMO_KEY"
nalAPI = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=" + apiKey + "&query=Cheddar%20Cheese"
# https://api.nal.usda.gov/fdc/v1/foods/search?query=cheddar%20cheese&dataType=Survey%20%28FNDDS%29&sortBy=dataType.keyword&sortOrder=asc
# https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1#/
res = rq.get(nalAPI) # TODO: decompose to function 1

# TODO: write dictionary mapping unit types to orders of magnitude

# TODO: build query
# TODO: build GUI to build query

# TODO: remove when ready
resJ = res.json()
print(type(res))
print(type(resJ))
print(resJ)

# TODO: build out this try-catch approximation
#       should check the status code and branch appropriately;
#       if something wrong with the server, keep trying for a certain number of times
#       if something wrong with query, return user to query build
# check if return status indicates successful retrieval
# while res.status_code != 200:
#     res = rq.get(nalAPI)  # TODO: decompose to function 1
#
#     if res.status_code == 200:
#         resJ = res.json()
# end

# TODO: decompose response into array of food items
# TODO: extract data per food item
# TODO: build RDI data, ?export to csv?
#       weight; fraction of RDI represented by food

# TODO: build RDI figures, ?make compat w df ??pandas???, ?read csv?
#       use bar_polar, possibly not the wind map that I found from SO
# build RDI figures

# TODO: display RDI figures in GUI
