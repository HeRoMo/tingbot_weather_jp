# -*- coding: utf-8 -*-
import tingbot
from tingbot import *
import requests
from jp_utils import jptime

# setup code here
font = tingbot.app.settings['font']
params = { 'city': tingbot.app.settings['city'] }
url = "http://weather.livedoor.com/forecast/webservice/json/v1"

screen.brightness = 70

def templature(forcast):
    t_min = '-'
    t_max = '-'
    if forcast['temperature']['min'] != None:
        t_min = forcast['temperature']['min']['celsius']
    if forcast['temperature']['max'] != None:
        t_max = forcast['temperature']['max']['celsius']
    return { 'min': t_min, 'max': t_max }
    

# display weather
# @param forcast [dict] forcast
def disp_weather(forcast):
    screen.text(u'%(dateLabel)s %(date)s' % forcast, xy=(5,50), align='topleft', font=font)
    screen.text(u'%(telop)s' % forcast, xy=(110,100), align='topleft', font=font, font_size=50)
    screen.image(forcast['image']['url'], scale=2, xy=(10,100), align='topleft')
    
    temp = templature(forcast)
    screen.text(u'%(min)s ℃' % temp, color='blue', font=font, xy=(145, 180), align='topright')
    screen.text(' / ', color='black', font=font, xy=(160, 180), align='top')
    screen.text(u'%(max)s ℃' % temp, color='red', font=font, xy=(175, 180), align='topleft')

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
    screen.fill(color='white')
    screen.text( '%(prefecture)s %(city)s' % location,
                font=font, color='black', xy=(5,5), align='topleft')
    disp_weather(forecast)
    # copy right
    screen.text(u'%(provider)s / %(title)s' % copyright, xy=(160,240), align='bottom', font=font, font_size=14)

tingbot.run()


