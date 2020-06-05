import yaml

data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '您好'}, 'value': '您好'},
    'search_test_001': {'except': [4, 5, 6], 'value': 456}
}}

# 将data写入到 当前目录下 ww.yml文件中
with open("./ww.yml", "a") as f:   # 以a模式:追加写入文件
    # 写yaml数据
    yaml.safe_dump(data, f, encoding='utf-8', allow_unicode = True)