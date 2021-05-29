# importing the necessary libraries and classes
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from messenger import Messenger

# link to udemy site
UDEMY_WEBSITE = "https://www.udemy.com/"

# location of chrome driver application on system
PATH_TO_DRIVER = "C://Chrome Driver/chromedriver.exe"

# creating a chrome driver and inputting the website url
driver = webdriver.Chrome(executable_path=PATH_TO_DRIVER)
driver.get(url=UDEMY_WEBSITE)

# navigating to the search input and submit button
search_input = '.udlite-text-input.udlite-text-input-small.udlite-text-sm.udlite-search-form-autocomplete-input.js' \
               '-header-search-field '
submit_button = '.udlite-search-form-autocomplete-input-group button'

driver.find_element_by_css_selector(search_input).send_keys("machine learning jose")
driver.find_element_by_css_selector(submit_button).click()

try:
    # getting the driver to wait for some time for the page to load the results
    element_to_be_found = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.udlite-focus-visible-target")))
except TimeoutException:
    print("Sorry, the request timed out\nThe selected element could not be found.")
else:
    # clicking on the first course that comes up
    course_name = driver.find_element_by_css_selector("div.udlite-focus-visible-target.udlite-heading-md.course-card--course-title--2f7tE")
    course_name.click()
    try:
        # getting the driver to wait for some time for the page to load the results
        element_to_be_found = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price-text--price-part--Tu6MH")))
    except TimeoutException:
        print("Request TimeOut. The price of the selected element could not be found.")
    else:
        # name of the course
        course_name = driver.find_element_by_css_selector("h1.udlite-heading-xl").text

        # instructor name
        instructor = driver.find_element_by_css_selector(".instructor-links--names--7UPZj a span").text

        # getting the price
        prices = driver.find_elements_by_css_selector(".price-text--price-part--Tu6MH span")
        current_price = float(prices[1].text.split("$")[1])

        # getting the current page url
        current_url = driver.current_url
        if current_price < 15:
            messenger = Messenger()
            messenger.send_mail(name=course_name, instructor=instructor, price=current_price, page_url=current_url)

driver.quit()
