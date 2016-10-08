# coding: utf-8
import tingbot
from tingbot import *

from jp_utils import jptime
from weather import fetch_forecast, weather_icons

# setup code here
city = tingbot.app.settings['city']
font = 'fonts/font_1_honokamarugo_1.1.ttf'

screen.brightness = 70

def disp_weather(forecast):
    '''display weather forecast

       @param forecast [dict] forecast
    '''
    # display weather icon
    icons = weather_icons(forecast)
    for icon in icons:
        screen.text(**icon)

    # display date
    screen.text(u'%(date)s\n%(dateLabel)s' % forecast,
                xy=(10,10),
                align='topleft',
                font_size=30,
                font=font,
                color='black')
    # display weather telop (ex: '晴㝮㝡曇')
    screen.text(u'%(telop)s' % forecast,
                xy=(310,230),
                align='bottomright',
                font=font,
                font_size=60,
                color='black')

    # display templature
    temp = forecast['temperature']
    screen.text(u'%(min)s ℃' % temp, color='blue', font=font, xy=(310, 110), align='topright')
    screen.text(u'%(max)s ℃' % temp, color='red', font=font, xy=(310, 140), align='topright')


@every(minutes=6)
def loop():
    current_hour = int(jptime.now().strftime('%H'),10)

    wf = fetch_forecast(city)
    forecast = wf.today if current_hour < 21 else wf.tomorrow

    # draw screen ##########
    screen.fill(color=(255,250,240))
    # copy right
    screen.text(u'%(provider)s / %(title)s' % wf.copyright, xy=(160,240), align='bottom', font=font, font_size=14)
    disp_weather(forecast)
    # display location
    screen.text( '%(prefecture)s\n%(city)s' % wf.location,
            font=font, font_size=20, color='black', xy=(310,10), align='topright')

tingbot.run()
