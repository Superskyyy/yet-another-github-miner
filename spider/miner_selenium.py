import random
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from credentials import GITHUB_USERNAME, GITHUB_PASSWORD
from utils.pretty_print import pretty_print

options = Options()
# options.add_argument("--start-maximized")
driver = webdriver.Chrome('../chromedriver.exe', options=options)

driver.get("https://github.com/search?p=1&q=filename%3AMLProject&type=Code")

time.sleep(1)
elem = driver.find_element_by_name("login")
elem.clear()
elem.send_keys(GITHUB_USERNAME)
elem = driver.find_element_by_name("password")
elem.send_keys(Keys.TAB)
elem.send_keys(GITHUB_PASSWORD)
elem.send_keys(Keys.ENTER)

# window to enter 2fa code
time.sleep(15)
# login completed

# Now we are at the search results `code` section
# we simply scrape each page for unique repo

# switch to next page
_dict = {}
# todo support 3 base urls
for page_num in range(100):
    driver.get(f"https://github.com/search?p={page_num + 1}&q=filename%3AMLProject&type=Code")
    time.sleep(random.randint(5, 10))
    driver.refresh()
    time.sleep(random.randint(10, 15))
    repo_urls = driver.find_elements_by_class_name("Link--secondary")

    for n in range(10):  # usually there's exact 10 of them on single pagination
        # noinspection PyBroadException
        try:
            repo_url = driver.find_element_by_css_selector(
                f"#code_search_results > div.code-list > div:nth-child({n + 1}) > div > div.flex-shrink-0.text-small.text"
                f"-bold > a")  # careful with the newline
            url = repo_url.get_attribute('href')
            path_mlproject_suspect = driver.find_element_by_css_selector(
                f"#code_search_results > div.code-list > div:nth-child({n + 1}) > div > p > a")
            path = path_mlproject_suspect.get_attribute('href')
            # some paths are not MLProject the exact file, but with extensions, remove those
            if path[-9:] == "MLproject":
                _dict.setdefault(url, []).append(path)
        except Exception:  # werid page missing entries
            pass

    time.sleep(random.randint(8, 12))

print(_dict)


# scrape and pickle into file
# scrape 3 categories

def retention():
    import pickle

    with open('first_batch_1000_bestmatch.pkl', 'wb') as fp:
        pickle.dump(_dict, fp)


retention()
pretty_print(_dict)
driver.close()
if __name__ == "__main__":
    ...

