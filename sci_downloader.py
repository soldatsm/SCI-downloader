from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tqdm import tqdm
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-list', help='Sequence of DOIs in cmd in quotation marks without commas -- "10.1016/j.promfg.2019.02.324" ', nargs='+')
parser.add_argument('-doi_file', help='path to file with DOIs in separated lines -- 10.1016/j.promfg.2019.02.324')
parser.add_argument('dir', help='Entr a path to folder for aricles in "D:\\article_folder\\" format')
#parser.add_argument('browser', help='Select browser, currently there is only Chromium')


args = parser.parse_args()

def sci_dowloader(url, lst_path=None):

    driver = webdriver.Chrome('D:/chromedriver.exe', options=option)
    driver.get(url)

    if 'article not found' in driver.title:
        sad_list.append(f'{url} -- NOT FOUND')
    else:
        elem = driver.find_element(By.CSS_SELECTOR, 'button').click()
        time.sleep(3)
        driver.close()


if __name__ == '__main__':

    option = webdriver.ChromeOptions()

    prefs = {"download.default_directory" : rf'{args.dir}'}

    option.headless = True
    option.add_experimental_option("prefs", prefs)

    sad_list = []

    if args.doi_file is not None:

        with open(fr'{args.doi_file}', 'r') as read_file:
            dois = read_file.readlines()
            dois = [i.replace('\n', '').replace("'", '').strip() for i in dois]
            read_file.close()
        
        new_urls = [f'https://www.sci-hub.ru/{i}' for i in dois]

        for i in tqdm(new_urls, desc='Downloading', colour='green'):
            sci_dowloader(i)

    elif args.list is not None:

        new_urls = [f'https://www.sci-hub.ru/{i}' for i in args.list]

        for i in tqdm(new_urls, desc='Downloading', colour='green'):
            sci_dowloader(i)

    if len(sad_list) >= 1:

        with open("D:/article_folder/Not_found_articles.txt", 'w') as write_file:
            for i in sad_list:
                write_file.write(i + '\n')

