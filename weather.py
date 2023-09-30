import requests
import colorama
daryaftcity = input("write your city :  ")

def fstring(data):
    if 'name' in data:
        return {"city":data ['name'] , "temp":round(data ['main'] ["temp"]-273.15,2) , "windyspeed" : data["wind"]["speed"] , "degwindy " : data ["wind"]["deg"] , "clouds" : data ["clouds"]["all"]}
    else:
        return {"not find"}

def get_data(city=daryaftcity,appid='47c7d2c4c299e53afded122c13642789'):
    url_site = "https://api.openweathermap.org/data/2.5/weather"
    json = {'q' :city ,'appid' :appid ,} 
    r = requests.get(url = url_site, params = json) 
    return fstring(r.json())

def main():
    daryaft = get_data(daryaftcity)
    print(daryaft)

if __name__ == "__main__":
    main()
