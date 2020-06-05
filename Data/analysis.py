import yaml


# 存储测试数据
data_list = []
# [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")]
# 打开文件
with open("./search.yml", "r", encoding="utf-8") as f:
    # 解析数据
    data = yaml.safe_load(f)

    # print(data.values())

    for i in data.values():
        # print(i.get("input"), i.get("exp"))
        # print("-----" * 10)
        data_list.append((i.get("input"), i.get("exp")))


