import requests
from bs4 import BeautifulSoup
import json
import time
import random

# 1. 配置区域
TARGET_URL = "https://jnbk-brakes.com/catalogue/cars" # 目标网址
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_data():
    print(f"🚀 开始抓取: {TARGET_URL}")
    response = requests.get(TARGET_URL, headers=HEADERS)
    
    if response.status_code != 200:
        print("❌ 抓取失败")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    new_data = []

    # 2. 解析逻辑 (这里需要你用 F12 检查网页后修改)
    # 假设我们要抓取所有品牌链接
    # 注意：以下选择器是示例，必须根据实际网页修改
    brands = soup.select('.brand-list a') 
    
    for brand in brands[:10]: # 先抓取前10个测试
        brand_name = brand.text.strip()
        # 这里需要进一步请求详情页获取 OE 号...
        # 模拟数据结构：
        new_data.append({
            "brand": brand_name,
            "model": "示例车型",
            "oe_number": "示例OE号",
            "part_number": "示例零件号"
        })
        
    return new_data

# 3. 保存逻辑
if __name__ == "__main__":
    data = get_data()
    if data:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ 成功抓取 {len(data)} 条数据，已更新 data.json")
    else:
        print("⚠️ 未获取到数据")