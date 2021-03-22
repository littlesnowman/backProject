import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import yaml


class BasePage(object):
    def __init__(self,url):
        option = Options()
        option.add_argument('start-maximized')
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(self.url)

    def find_element(self,method):


    def select_menu(self):

    def select_menu_list(self):

    def select_level(self):

    def filter(self):

    def input_key(self,input_value):


    def upload_file(self):


    def click_button(self):


    def read_yaml(self, filename):
        with open(self.filename, 'r', encoding='utf-8') as f:
            yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_data


