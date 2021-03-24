import credentials, src.services.forecast, lists

lists.run()

src.services.forecast.rapidApiSecureKey = credentials.rapidapi_key

cityCodes = ["atlanta,us", "denver,us", "edinburgh,uk", "warsaw,pl", "mumbai,in"]

for cityCode in cityCodes:
    forecast = src.services.forecast.getForecast(cityCode)
    entry = forecast["list"][0]
    dateTime = entry["dt_txt"]
    temperature = round(entry["main"]["temp"]-273.15,2)
    fealsLike = round(entry["main"]["feels_like"]-273.15,2)
    windSpeed = str(round(entry["wind"]["speed"],2))+"m/s"
    clouds = str(entry["clouds"]["all"])+"%"
    weatherDesc = entry["weather"][0]["description"]
    clouds = str(entry["clouds"]["all"])+"%"
    print(cityCode, dateTime, temperature, fealsLike, windSpeed, clouds, weatherDesc, sep="\t")

# print(src.services.forecast.getForecast("atlanta,us")["list"][0])
