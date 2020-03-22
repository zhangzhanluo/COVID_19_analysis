# COVID_19_analysis

2019新型冠状病毒统计及可视化分析的一个mini项目。
A simple statistic and visualization program of COVID-19.

基于[requests](https://requests.readthedocs.io/zh_CN/latest/)、[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)、[pyecharts](https://pyecharts.org/#/zh-cn/)实现了简单的2019新型冠状病毒数据的获取、清洗及可视化。  
Data acquisition, cleaning, and visualization are based on the packages of [requests](https://requests.readthedocs.io/en/master/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start), and [pyecharts](https://pyecharts.org/#/en-us/), respectively.


## 文件说明 Document Illustration

||||
|------|------|------| 
|statistic_outside_China.py | 主要的统计代码文件 | Statistic Code File  |
|visualization_inside_China.py | 主要的可视化代码文件 | Visualization Code File  |
|render.html | 结果文件（html格式） | Result (html format) | 
|png/ | 结果文件（png格式） | Result (png format) | 
|ppt/  | 项目详细说明(可视化部分) | Project Detailed Illustration (Visualization)|

## 成果 Results

### 统计部分 Statistic Part

![alt country confirmed](png/Cumulative%20Diagnosis.png)

![alt Confirmed Cases of Selected Countries](png/Confirmed%20Cases%20of%20Selected%20Countries.png)

### 可视化部分 Visualization Part

![alt Confirmed cases](png/Confirmed%20cases.png)

![alt country current confirmed](png/Current%20Diagnosis.png)

![alt shanghai confirmed](png/Cumulative%20Diagnosis%20Shanghai.png)
