import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

fmei =open(r"D:\划线数据\美国.txt",'r',encoding='utf-8')
fri =open(r"D:\划线数据\日本.txt",'r',encoding='utf-8')
fyin =open(r"D:\划线数据\印度.txt",'r',encoding='utf-8')

fmeishuju = fmei.read()
frishuju = fri.read()
fyinshuju = fyin.read()

fmeishuju=fmeishuju.replace("jsonp_1629344292311_69436(","")
frishuju=frishuju.replace("jsonp_1629350871167_29498(","")
fyinshuju=fyinshuju.replace("jsonp_1629350745930_63180(","")
fmeishuju=fmeishuju[:-2]
frishuju=frishuju[:-2]
fyinshuju=fyinshuju[:-2]
fmeishuju=json.loads(fmeishuju)
frishuju=json.loads(frishuju)
fyinshuju=json.loads(fyinshuju)

fmeishuju_trend = fmeishuju['data'][0]['trend']
frishuju_trend = frishuju['data'][0]['trend']
fyinshuju_trend = fyinshuju['data'][0]['trend']
fmeishuju_x=fmeishuju_trend['updateDate'][:314]
fmeishuju_y=fmeishuju_trend['list'][0]['data'][:314]
frishuju_y=frishuju_trend['list'][0]['data'][:314]
fyinshuju_y=fyinshuju_trend['list'][0]['data'][:314]
line = Line()
line.add_xaxis(fmeishuju_x)
line.add_yaxis("美国确诊人数",fmeishuju_y,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",frishuju_y,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",fyinshuju_y,label_opts=LabelOpts(is_show=False))

line.set_global_opts(title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)
line.render('图二.html')
fmei.close()
line