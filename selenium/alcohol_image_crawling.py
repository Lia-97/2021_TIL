from selenium import webdriver
import time
import json
import pickle
from urllib.request import urlretrieve

with open('alcohol.json', encoding='UTF8') as alcohol:
    alcohol_list = json.load(alcohol)

search_list = []
for dic in alcohol_list:
    search_list.append(f"{dic['product']} {dic['category']}")

def Get_src():
    path = 'chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get('https://www.google.com') # google 열기
    for idx, word in enumerate(search_list[51:], 52):
        driver.get(f'https://www.google.com/search?q={word}&tbm=isch&ved=2ahUKEwin_7Tv6ajwAhUK5JQKHahvBwYQ2-cCegQIABAA&oq=%EC%B2%AD%EB%AA%85%EC%A3%BC500+%EC%95%BD%EC%A3%BC&gs_lcp=CgNpbWcQA1AAWABgkdgfaABwAHgAgAEAiAEAkgEAmAEAqgELZ3dzLXdpei1pbWc&sclient=img&ei=lHeNYKflPIrI0wSo350w&bih=610&biw=1263&hl=ko')
        # element = driver.find_element_by_name('q')# 구글 검색창 찾기
        # element.send_keys(word)
        # element.submit()
        # img_btn = driver.find_element_by_link_text('이미지')
        # img_btn.click()
        time.sleep(1)
        # tool = driver.find_element_by_css_selector('.PNyWAd.ZXJQ7c')
        # tool.click()
        # size = driver.find_element_by_css_selector('.DZjDQ')
        # size.click()
        # big = driver.find_element_by_class_name('Hm7Qac')
        # big.click()
        # time.sleep(1)
        first_img = driver.find_element_by_class_name('rg_i')
        first_img.click()
        time.sleep(3)
        try:
            large_img = driver.find_element_by_css_selector('.n3VNCb').get_attribute('src')
            # time.sleep(4)
            # img_src = large_img.get_attribute('src')
            time.sleep(3)
            urlretrieve(large_img, f'alcohol_pic/{idx}.jpg')
        except:
            pass
        # driver.execute_script("window.open('')")
        # tab = driver.window_handles[-1]
        # driver.switch_to.window(tab)
        # driver.get(img_src)
        # time.sleep(5)
        # driver.save_screenshot(f'alcohol_pic/{idx}.jpg')
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
    return


# def Save_src(result):
#     with open('img_src.txt','wb') as f:
#         pickle.dump(result,f)
#
#
# def Load_src():
#     with open('img_src.txt', 'rb') as f:
#         result = pickle.load(f)
#     return result


if __name__ == "__main__":
    Get_src()
    # Save_src(result)
    # result = Load_src()
