import http.client, os.path, json, datetime

rapidApiSecureKey = ""

def callOpenWeather(cityCode):
    headers = {
        'x-rapidapi-key': rapidApiSecureKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
    query = cityCode.replace(' ','%20').replace(',','%2C')
    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")
    conn.request("GET", "/forecast?q=" + query, headers=headers)
    res = conn.getresponse()
    data = res.read()
    return data

def cityCodeToFileName(cityCode):
    folder = 'forecasts/'
    cityPart = cityCode.replace(' ','-').replace(',','-')
    datePart = datetime.datetime.today().strftime('%Y-%m-%d') 
    return  folder + cityPart + '_' + datePart + '.json'
        
def hasForecast (cityCode):
    fname = cityCodeToFileName(cityCode)
    return os.path.isfile(fname)

def saveForecast(cityCode,forecastData):
    fname = cityCodeToFileName(cityCode)
    f = open(fname, "a")
    f.write(forecastData)
    f.close()

def loadForacast(cityCode):
    fname = cityCodeToFileName(cityCode)
    f = open(fname, "r")
    forecastData = f.read()
    f.close()
    return forecastData

def getForecast(cityCode):
    if hasForecast(cityCode):
        dataStr = loadForacast(cityCode)
    else:
        data = callOpenWeather(cityCode)
        dataStr = data.decode("utf-8")
        saveForecast(cityCode,dataStr)
    jsonForecast = json.loads(dataStr)
    return jsonForecast
