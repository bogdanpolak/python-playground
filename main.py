import credentials, src.services.forecast, lists

lists.run()

src.services.forecast.rapidApiSecureKey = credentials.rapidapi_key
# cityCode = "san francisco,us"
# cityCode = "atlanta,us"
# cityCode = "denver,us"
# cityCode = "edinburgh,uk"
cityCode = "mumbai,in"
print(src.services.forecast.getForecast(cityCode))

