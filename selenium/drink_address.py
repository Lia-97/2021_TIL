from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

drinks = ['익선반주', '옳은', '백곰 막걸리', '미월', '난지당', '디히랑', '공간 뒷동산',
         '술다방', '뎐', '박경자식당', '산울림1992', '정작가의 막걸릿집', '누룩나무',
         '작', '삼씨오화', '여정막걸리', '솟대막걸리양조장', '역전회관', '윤서울',
         '안씨막걸리', '학술적연구소', '이파리', '주유별장', '묵전', '모우모우']


def Get_address():
    result = []
    path = 'chromedriver.exe'
    driver = webdriver.Chrome(path)
    for drink in drinks:
        driver.get('https://map.kakao.com/')  # kakao 지도 열기
        search_ele = driver.find_element_by_name('q')
        search_ele.send_keys(drink)
        search_ele.send_keys(Keys.ENTER)
        time.sleep(2)
        address = driver.find_elements_by_css_selector('#info\.search\.place\.list > li')
        for a in address:
            if a.get_attribute('class') == 'AdItem':
                continue
            link_name = a.find_element_by_css_selector('div strong .link_name').text
            if link_name.replace(' ', '') == drink.replace(' ', ''):
                ad = a.find_element_by_css_selector('div.info_item > .addr > p').text
                if '서울' in ad:
                    result.append({
                        'store': drink,
                        'address': ad
                    })

    return result


def Save_json(result):
    file_path = 'address.json'

    with open(file_path, 'w') as output:
        json.dump(result, output)


def Open_json(file_path):
    with open(file_path, 'r') as output:
        json_data = json.load(output)
        print(json_data)


if __name__ == '__main__':
    result = Get_address()
    Save_json(result)
    Open_json(file_path = 'address.json')
