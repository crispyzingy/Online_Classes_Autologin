from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.Firefox()  # comment out if you want to mute
## mute ##
# profile = webdriver.FirefoxProfile()
# profile.set_preference("media.volume_scale", "0.0")
# browser = webdriver.Firefox(firefox_profile=profile)

url = "https://whiteboard.myperfectice.com/b/"
link_end = {
    "se": "man-k42-kfr",
    "ml": "sum-khm-khr",
    "spcc": "pra-rrq-gww",
    "css": "ash-cxx-ch6",
    "dwm": "atu-zzw-ecw",
}

# address = link_end["se"]
# address = link_end["ml"]
# address = link_end["spcc"]
address = link_end["css"]
# address = link_end["dwm"]


final_url = url + address
browser.get(final_url)


## send_keys(), submit() for search. Browser - back, forward, refresh, quit ##
selector = "#_b_" + address + "_join_name"
elem = browser.find_element_by_css_selector(selector)
elem.send_keys("Arbaaz Khan A")

elem = browser.find_element_by_css_selector(".btn-primary")
elem.click()

elem = WebDriverWait(browser, 10).until(
    expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, ".icon-bbb-listen")
    )
)
elem.click()
