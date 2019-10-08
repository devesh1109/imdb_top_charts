from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def retrieve_top_charts(url):
    driver.get(url)
    action = ActionChains(driver)
    action.send_keys(Keys.ESCAPE).perform()
    source_nested = driver.page_source
    soup_local = BeautifulSoup(source_nested, 'html.parser')
    products = soup_local.find_all("div", {"class":"list-description"})
    f = open("top_charts_query.txt", 'w')
    for item_local in products:
        print(item_local)
        f.write(str(item_local)+"\n")


def get_mapping(ind):
    this_key = list_keys[int(ind)]
    if this_key:
        ext_url = dict_top_charts[this_key]
        return ext_url
    else:
        return "Wrong Input. Run Again!"


# base url
base_url = "https://www.imdb.com"
# gets the source code of the base url
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(r"D:\Users\ASUS\PycharmProjects\imdb_top_charts\drivers\chromedriver.exe", chrome_options=options)
driver.get(base_url+"/best-of")
source = driver.page_source
# parses the source code for further extraction
soup = BeautifulSoup(source, 'html.parser')
# finds div of class aux-content-widget-2
links = soup.find("div", {"class": "aux-content-widget-2"})
# gets the p tag under links and creates a soup object
new_soup = BeautifulSoup(str(links.p), "html.parser")
extract_links = new_soup.find_all("a")
dict_top_charts = {}
for i, item in enumerate(extract_links):
    dict_top_charts[item.text] = item['href']
    print(str(i) + "-->" + item.text + "\n")
list_keys = list(dict_top_charts.keys())
a = int(input("Which Top Chart do you want ? \n"))
ext_url = get_mapping(a)
new_url = base_url + ext_url
retrieve_top_charts(new_url)
