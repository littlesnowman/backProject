import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''-----Options设置窗口最大化-----'''
from selenium.webdriver.support.select import Select

option = Options()
option.add_argument('start-maximized')
driver = webdriver.Chrome(options=option)
driver.get("http://back.test.duiastar.com/")

'''-----打开浏览器后窗口最大化-----'''
# driver.maximize_window()

'''-----添加登陆状态的cookie-----'''
cookies = {"name": "SID", "value": "294c43a4-b672-4a13-8b85-2915a3b88502"}
driver.add_cookie(cookies)
driver.get("http://back.test.duiastar.com/")

'''-----账号密码登陆-----'''
# driver.find_element_by_css_selector("input#user_input").send_keys("xiongxueting@duia.com")
# driver.find_element_by_css_selector("input#user_pwd").send_keys("Duia2020")
# driver.find_element_by_css_selector("button#login_btn").click()

# -----TODO:添加显示等待-----
driver.implicitly_wait(10)
driver.find_element_by_xpath("//a[text()='内容']").click()
sleep(5)

'''-----通过js代码修改display属性展开下拉选项-----'''
js = """elements = document.getElementsByClassName('自然拼读内容管理_sub');
        for(var i=0;i< elements.length;i++)
        {
            elements[i].style.display='block'
         }
      """
driver.execute_script(js)

'''-----定位“星球内容管理”模块并打开-----'''
driver.find_element_by_css_selector("[target='/naturalSpellStar/list']").click()
# driver.find_element_by_xpath("//span[text()='星球内容管理']").click()
sleep(5)

'''-----筛选level3，星球“巨石星球”，“sc”碎片-----'''
s1 = driver.find_element_by_css_selector("#level")
Select(s1).select_by_visible_text("Level3")
s2 = driver.find_element_by_css_selector("#starf")
Select(s2).select_by_visible_text("巨石星球")
s3 = driver.find_element_by_css_selector("#platef")
Select(s3).select_by_visible_text("st")
sleep(2)
'''-----查找-----'''
driver.find_element_by_css_selector("#find").click()

driver.find_elements_by_tag_name("tr")
# -----关闭浏览器-----
# driver.quit()






























