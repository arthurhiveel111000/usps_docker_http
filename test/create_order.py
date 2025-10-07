import hashlib
import json
import time
import requests
from collections import OrderedDict

# ========== 基础配置 ==========
# API_URL = "http://146.190.133.102/digisys/api/express/createOrder"
API_URL = "http://47.86.56.111/its-api/api/fba/createOrder"

apikey = ""          # API 授权码
apisecret = ""           # API 密钥
usertoken = ""      # 用户唯一标识

# ========== 请求体 ==========
# 使用 OrderedDict 严格控制字段顺序
body = OrderedDict([
    ("customerOrderNo", "202510070001"),
    ("refNo2", "PC-00000001-01"),
    ("refNo3", ""),
    ("logisticsProductCode", "US-EXPRESS"),
    ("signatureType", 10),
    ("fbaWarehouseCode", ""),
    ("consignee", OrderedDict([
        ("consigneeName", "cm liu"),
        ("consigneeCompany", None),
        ("consigneePhone", "14343423"),
        ("consigneeCountry", "US"),
        ("consigneeProvince", "OHOH"),
        ("consigneeCity", "MORAINE"),
        ("consigneeDistrict", None),
        ("consigneePostcode", "837732"),
        ("consigneeAddress", "3155 ELBEE RD")
    ])),
    ("packages", [
        OrderedDict([
            ("packageWeightD", 1),
            ("packageNo", "PKG-202510070001"),
            ("packageLengthD", 10),
            ("packageWidthD", 10),
            ("packageHeightD", 10)
        ])
    ])
])

def generate_signature(apikey, apisecret, usertoken, timestamp, body):
    body_str = json.dumps(body, ensure_ascii=False, separators=(',', ':'))
    # ⚠ 按文档要求顺序拼接
    sign_str = f"{apikey}{apisecret}{usertoken}{timestamp}{body_str}"
    # sign_str = "abcdefg123customer1587202455254{orderNo:\"1234567890\"}"
    # sign_str = "abcdefg123customer1587202455254{orderNo:”1234567890”}"

    print("拼接字符串：", sign_str)
    print("签名前 JSON：", body_str)
    return hashlib.md5(sign_str.encode('utf-8')).hexdigest()

def create_order():
    timestamp = str(int(time.time() * 1000))
    signature = generate_signature(apikey, apisecret, usertoken, timestamp, body)
    # signature = generate_signature("abcdefg", "123", "customer", "1587202455254", {"orderNo": "1234567890"})
    print("签名字符串：", signature)

    headers = {
        "apikey": apikey,
        "signature": signature,
        "timestamp": timestamp,
        "usertoken": usertoken,
        "Content-Type": "application/json;charset=UTF-8"
    }

    response = requests.post(API_URL, headers=headers, json=body)
    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    create_order()