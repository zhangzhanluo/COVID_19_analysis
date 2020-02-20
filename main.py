import time
import json
import requests
from bs4 import BeautifulSoup
from pyecharts import options as opts
from pyecharts.charts import Map, Page

"""

第一步：数据获取
使用爬虫（requests+BeautifulSoup），从丁香园网站上爬取。

"""

r = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
area_stat_raw = soup.find(id='getAreaStat').get_text()

"""

第二步：数据清洗
从网站上爬下来的数据需要根据网站的具体情况进行分析，进而根据网站搭建的方式提取有用的信息。

"""

area_stat_js = area_stat_raw[len('try { window.getAreaStat = '): -len('}catch(e){}')]
area_stat = json.loads(area_stat_js)

# 进行省级和市级统计
province_name = []
p_current_confirmed_count = []
p_confirmed_count = []
city_name = []
c_current_confirmed_count = []
c_confirmed_count = []
for province in area_stat:
    province_name.append(province['provinceShortName'])
    p_current_confirmed_count.append(province['currentConfirmedCount'])
    p_confirmed_count.append(province['confirmedCount'])
    if province['provinceShortName'] == '上海':
        for city in province['cities']:
            if city['cityName'] == '待明确地区' or city['cityName'] == '外地来沪人员':
                continue
            city_name.append(city['cityName'])
            c_current_confirmed_count.append(city['currentConfirmedCount'])
            c_confirmed_count.append(city['confirmedCount'])

"""

第三部：数据可视化
基于pyecharts分别做全国现存确诊、累计确诊的省级分布图以及上海市的累计确诊区级分布图。

"""
page = Page(page_title='iDesignLab')

# 省级现存确诊
chart = Map(init_opts=opts.InitOpts(width='1500px', height='800px'))
chart.add('现存确诊', [list(z) for z in zip(province_name, p_current_confirmed_count)], 'china')
chart.set_global_opts(
    toolbox_opts=opts.ToolboxOpts(is_show=True, pos_top='20px'),
    title_opts=opts.TitleOpts(title='2019-nCoV疫情地图：{}（{}）'.format('现存确诊', time.asctime()), pos_left='center',
                              pos_top='20px'),
    legend_opts=opts.LegendOpts(is_show=False),
    visualmap_opts=opts.VisualMapOpts(
        is_piecewise=True,
        pieces=[
            {'min': 10000},
            {'min': 500, 'max': 9999},
            {'min': 100, 'max': 499},
            {'min': 10, 'max': 99},
            {'min': 1, 'max': 9},
            {'max': 0}]))
page.add(chart)

# 省级累计确诊
chart = Map(init_opts=opts.InitOpts(width='1500px', height='800px'))
chart.add('累计确诊', [list(z) for z in zip(province_name, p_confirmed_count)], 'china')
chart.set_global_opts(
    toolbox_opts=opts.ToolboxOpts(is_show=True, pos_top='20px'),
    title_opts=opts.TitleOpts(title='2019-nCoV疫情地图：{}（{}）'.format('累计确诊', time.asctime()), pos_left='center',
                              pos_top='20px'),
    legend_opts=opts.LegendOpts(is_show=False),
    visualmap_opts=opts.VisualMapOpts(
        is_piecewise=True,
        pieces=[
            {'min': 10000},
            {'min': 500, 'max': 9999},
            {'min': 100, 'max': 499},
            {'min': 10, 'max': 99},
            {'min': 1, 'max': 9},
            {'max': 0}]))
page.add(chart)

# 上海市累计确诊
chart = Map(init_opts=opts.InitOpts(width='1500px', height='800px'))
chart.add('累计确诊', [list(z) for z in zip(city_name, c_confirmed_count)], '上海')
chart.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
chart.set_global_opts(
    toolbox_opts=opts.ToolboxOpts(is_show=True, pos_top='20px'),
    title_opts=opts.TitleOpts(title='2019-nCoV疫情地图：{}（{}）'.format('累计确诊', '上海市，' + time.asctime()), pos_left='center',
                              pos_top='20px'),
    legend_opts=opts.LegendOpts(is_show=False),
    visualmap_opts=opts.VisualMapOpts(
        is_piecewise=True,
        pieces=[
            {'min': 49},
            {'min': 40, 'max': 49},
            {'min': 30, 'max': 39},
            {'min': 20, 'max': 29},
            {'min': 10, 'max': 19},
            {'max': 10}]))
page.add(chart)

page.render()
