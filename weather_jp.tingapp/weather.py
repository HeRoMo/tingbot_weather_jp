# coding: utf-8
import requests

class Forecast:
    '''Container class of forecast data
    '''
    pass

# 
# @param
def fetch_forecast(city):
    ''' Fetch weather forecast from Livedoor weather hack API
    
        @param city [String] city code
        @return [dict] forecast data
    '''
    params = { 'city': city }
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    res = requests.get(url, params=params).json()
    
    forecast = Forecast()
    forecasts = res['forecasts']
    forecast.today = forecasts[0]
    forecast.today.update({'temperature': temperature(forecasts[0])})
    forecast.tomorrow = forecasts[1]
    forecast.tomorrow.update({'temperature': temperature(forecasts[1])})
    forecast.location = res['location']
    forecast.copyright = { 'provider': res['copyright']['provider'][0]['name'], 'title': res['copyright']['image']['title']}
    return forecast

def temperature(forecast):
    ''' parse temperature attribute of forecast data.
        
        @param forecast [dict] forecast data.
        @return [dict] min and max temperature by celsius
    '''
    t_min = '-'
    t_max = '-'
    if forecast['temperature']['min'] != None:
        t_min = forecast['temperature']['min']['celsius']
    if forecast['temperature']['max'] != None:
        t_max = forecast['temperature']['max']['celsius']
    return { 'min': t_min, 'max': t_max }
    
def weather_fonts(url):
    '''build weather icon list
        
        @param url [string] URL of weather image
        @return [lit] list of weather fonts
    '''
    sunny      = {'font': u'\uf101', 'color':(255, 165, 0)}
    sun        = {'font': u'\uf113', 'color':(255, 165, 0)}
    base_cloud = {'font': u'\uf105', 'color':(180,180,180)}
    cloudy     = {'font': u'\uf106', 'color':(180,180,180)}
    rain       = {'font': u'\uf107', 'color':(100,149,237)}
    windyrain  = {'font': u'\uf10e', 'color':(100,149,237)}
    sleet      = {'font': u'\uf10c', 'color':(100,149,237)}
    snow       = {'font': u'\uf102', 'color':(133, 216, 247)}
    snowy      = {'font': u'\uf10b', 'color':(133, 216, 247)}
    windysnow  = {'font': u'\uf103', 'color':(133, 216, 247)}
    windy      = {'font': u'\uf115', 'color':(139,137,137)}
    windyraincloud = {'font': u'\uf111', 'color':(139,137,137)}
    windysnowcloud = {'font': u'\uf109', 'color':(139,137,137)}
    rain_storm = {'font': u'\uf018', 'color':(0,0,255)}
    snow_storm = {'font': u'\uf064', 'color':(0,0,255)}
    file = url.split('/')[-1].split('.')[-2]
    code = { '1': [[sun]], # 晴
             '2': [[sunny,cloudy]], # 晴れ時々曇り
             '3': [[base_cloud, sunny, rain]], # 晴れ時々雨
             '4': [[base_cloud, sunny, snow]], # 晴れ時々雪
             '5': [[sun],[cloudy]], # 晴れのち曇り
             '6': [[sun],[base_cloud, rain]], # 晴れのち雨
             '7': [[sun],[base_cloud, snowy]], # 晴れのち雪
             '8': [[cloudy]], # 曇り
             '9': [[sunny,cloudy]], # 曇り時々晴れ
             '10': [[base_cloud, rain]], # 曇り時々雨
             '11': [[base_cloud, snow]], #曇り時々雪
             '12': [[cloudy], [sun]], # 曇りのち晴れ
             '13': [[cloudy], [base_cloud, rain]], # 曇りのち雨
             '14': [[cloudy], [base_cloud, snowy]], # 曇りのち雪
             '15': [[rain]], # 雨
             '16': [[base_cloud, rain, sunny]], # 雨時々晴れ
             '17': [[base_cloud, rain]], # 雨時々止む(曇り)
             '18': [[base_cloud, sleet]], # 雨時々雪
             '19': [[base_cloud, rain],[sun]], # 雨のち晴れ
             '20': [[base_cloud, rain],[cloudy]], # 雨のち曇り
             '21': [[base_cloud, rain],[base_cloud, snowy]], # 雨のち雪
             '22': [[windyraincloud, windyrain]], # 雨で暴風を伴う
             '23': [[base_cloud, snowy]], # 雪
             '24': [[base_cloud, snow, sunny]], # 雪時々晴れ
             '25': [[base_cloud, windysnow]], # 雪時々止む(曇り)
             '26': [[base_cloud, sleet]], # 雪時々雨
             '27': [[base_cloud, snowy],[sun]], # 雪のち晴れ
             '28': [[base_cloud, snowy],[cloudy]], # 雪のち曇り
             '29': [[base_cloud, snowy],[rain]], # 雪のち雨
             '30': [[windysnowcloud, windysnow]] # 暴風雪
            }[file]
    return code
    
wfont ='fonts/iconvault_forecastfont.ttf'
def weather_icons(forecast):
    '''prepare weather icons for forecast
    
        @param forcast [dict] forcast data
        @return [list(dict)] list of icon data
    '''
    fonts=weather_fonts(forecast['image']['url'])
    text_list = []
    if len(fonts) > 1:
        font_size = 150
        for f in fonts[0]:
            text_list.append({"string": f['font'], "xy":(200,160), "font_size":font_size, "align":'bottomright', "color":f['color'], "font":wfont })
        for f in fonts[1]:
            text_list.append({"string": f['font'], "xy":(120,80), "font_size":font_size, "align":'topleft', "color":f['color'], "font":wfont })
    else:
        for f in fonts[0]:
            text_list.append({"string": f['font'], "xy":(160,120), "font_size":270, "align":'center', "color":f['color'], "font":wfont })
    return text_list
