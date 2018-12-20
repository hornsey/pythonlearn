"""
    功能：AQI计算
"""

import requests
from bs4 import Beautiful

def get_city_aqi(city):
    """
        返回城市的才
    :param url:
    :return:
    """
    url = "http://pm25.in/" + city_pinyin
    url_text = get_html_text(url)
    resp = requests.get(url,timeout=30)
    bs = BeautifulSoap(resp.text, 'lmsl')
    div_list = bs.find_all('div', {'class': 'span1'})

    for i in range(len(div_list)):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

    return ret.text

def main():
    """
        主程序
    :return:
    """
    city_pinyin = input("请输入城市拼音： ")
    aqi_val = get_city_aqi(city_pinyin)
    print("空气质量为：{}".format(aqi_val))


if __name__ == '__main__':
    main()