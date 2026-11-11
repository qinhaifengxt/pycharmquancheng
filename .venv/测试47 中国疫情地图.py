import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open(r"C:\Users\28161\Desktop\资料\资料\可视化案例数据\地图数据\疫情.txt",'r',encoding='utf-8')
data = f.read()
f.close()
data_dict = json.loads(data)
province_data_list = data_dict['areaTree'][0]['children']
name_map = {
    "北京": "北京市", "天津": "天津市",
    "上海": "上海市", "重庆": "重庆市",
    "内蒙古": "内蒙古自治区",
    "广西": "广西壮族自治区",
    "西藏": "西藏自治区",
    "宁夏": "宁夏回族自治区",
    "新疆": "新疆维吾尔自治区",
    "香港": "香港特别行政区",
    "澳门": "澳门特别行政区",
}
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]

    if province_name in name_map:
        province_name = name_map[province_name]
    elif not province_name.endswith(("省", "市", "自治区", "特别行政区")):
        province_name += "省"

    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))


map = Map()
map.add('各省份确认人数',data_list,"china")

map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,           # 是否显示
        is_piecewise=True,      # 是否分段
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~9999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~99999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#990033"},
        ]
    )
)
map.render("全国疫情地图.html")