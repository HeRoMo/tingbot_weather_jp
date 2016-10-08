# coding: utf-8
import tingbot
from tingbot import *
import requests
from jp_utils import jptime
from weather import *

# setup code here

params = { 'city': tingbot.app.settings['city'] }
url = "http://weather.livedoor.com/forecast/webservice/json/v1"
screen.brightness = 70

@every(minutes=6)
def loop():
    current_hour = int(jptime.now().strftime('%H'),10)

    res = requests.get(url, params=params).json()
    forecasts = res['forecasts']
    today = forecasts[0]
    tomorrow = forecasts[1]
    location = res['location']
    copyright = { 'provider': res['copyright']['provider'][0]['name'], 'title': res['copyright']['image']['title']}
    
    forecast = today if current_hour < 21 else tomorrow
    # draw screen ##########
    screen.fill(color=(255,250,240))
    screen.text( '%(prefecture)s\n%(city)s' % location,
                font=font, font_size=20, color='black', xy=(310,10), align='topright')
    disp_weather(forecast)
    # copy right
    screen.text(u'%(provider)s / %(title)s' % copyright, xy=(160,240), align='bottom', font=font, font_size=14)

tingbot.run()


