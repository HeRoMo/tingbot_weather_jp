# coding: utf-8
import tingbot
from tingbot import *

font = 'fonts/font_1_honokamarugo_1.1.ttf'
wfont ='fonts/iconvault_forecastfont.ttf'

def templature(forcast):
    t_min = '-'
    t_max = '-'
    if forcast['temperature']['min'] != None:
        t_min = forcast['temperature']['min']['celsius']
    if forcast['temperature']['max'] != None:
        t_max = forcast['temperature']['max']['celsius']
    return { 'min': t_min, 'max': t_max }
    
def weather_icon(url):
    sunny  = {'font': u'\uf101', 'color':(255, 165, 0)}
    sun  = {'font': u'\uf113', 'color':(255, 165, 0)}
    base_cloud = {'font': u'\uf105', 'color':(180,180,180)}
    cloudy = {'font': u'\uf106', 'color':(180,180,180)}
    rain   = {'font': u'\uf107', 'color':(100,149,237)}
    windyrain = {'font': u'\uf10e', 'color':(100,149,237)}
    sleet   = {'font': u'\uf10c', 'color':(100,149,237)}
    snow   = {'font': u'\uf102', 'color':(133, 216, 247)}
    snowy   = {'font': u'\uf10b', 'color':(133, 216, 247)}
    windysnow = {'font': u'\uf103', 'color':(133, 216, 247)}
    windy  = {'font': u'\uf115', 'color':(139,137,137)}
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
    
def disp_font(icon, xy=(160,120), font_size=270, align='center'):
    for i in icon:
        screen.text(i['font'], xy=xy, font_size=font_size, align=align, font=wfont, color=i['color'])

def disp_icon(forcast):
    icon=weather_icon(forcast['image']['url'])
    if len(icon) > 1:
        disp_font(icon[0], xy=(200,160), font_size=150, align='bottomright')
        disp_font(icon[1], xy=(120,80), font_size=150, align='topleft')
        # TODO sometime or after
    else:
        disp_font(icon[0])
      
# display weather
# @param forcast [dict] forcast
def disp_weather(forcast):
    disp_icon(forcast)
    
    screen.text(u'%(date)s\n%(dateLabel)s' % forcast, xy=(10,10), align='topleft', font_size=30, font=font, color='black')
    screen.text(u'%(telop)s' % forcast, xy=(310,230), align='bottomright', font=font, font_size=60, color='black')

    # templature
    temp = templature(forcast)
    screen.text(u'%(min)s ℃' % temp, color='blue', font=font, xy=(310, 110), align='topright')
    # screen.text(' / ', color='black', font=font, xy=(160, 140), align='top')
    screen.text(u'%(max)s ℃' % temp, color='red', font=font, xy=(310, 140), align='topright')
