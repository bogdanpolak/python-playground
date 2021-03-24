import http.client, os.path
from datetime import datetime
import credentials

expenses = [10.30, 24.60, 10, 15, 56.69]
total = sum(expenses)

def callOpenWeather(cityCode):
    headers = {
        'x-rapidapi-key': credentials.rapidapi_key,
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
    datePart = datetime.today().strftime('%Y-%m-%d') 
    return  folder + cityPart + '_' + datePart + '.json'
        
def hasForecast (cityCode):
    fname = cityCodeToFileName(cityCode)
    return os.path.isfile(fname)

def saveForecast(cityCode,data):
    fname = cityCodeToFileName(cityCode)
    f = open(fname, "a")
    f.write(data)
    f.close()

cityCode = "san francisco,us"
data = callOpenWeather(cityCode)
dataStr = data.decode("utf-8")
saveForecast(cityCode,dataStr)
