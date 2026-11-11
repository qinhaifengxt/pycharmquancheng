from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

f = open(r"C:\Users\28161\Desktop\资料\资料\可视化案例数据\动态柱状图数据\1960-2019全球GDP数据.csv",'r',encoding='GB2312')
data_lines = f.readlines()
data_lines.pop(0)
data_dict = {}
for line in data_lines:
    line = line.split(',')
    year = int(line[0])
    country = line[1]
    gdp =float(line[2])
    try:
        data_dict[year].append([country,gdp])
    except:
        data_dict[year] =[]
        data_dict[year].append([country,gdp])

timeline = Timeline({'theme':ThemeType.LIGHT})
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda x: x[1], reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gap in year_data:
        x_data.append(country_gap[0])
        y_data.append(country_gap[1]/100000000)

    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()
    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
# 绘图
timeline.render("1960-2019全球GDP前8国家.html")