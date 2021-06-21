"""
script to scrape a website for doctor addresses
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:
    # init driver
    wait = WebDriverWait(driver, 10)

    # load main page
    driver.get('https://healthy.kaiserpermanente.org/northern-california/doctors-locations#/search-result')

    # set start and end values
    num_docs = 0
    target_docs = 50

    # loop until we have at least 50 docs
    while num_docs < target_docs:

        # wait until pagination link is available (indicates loading of details is done)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'kpPagination__link')))

        # get list of doctors in page
        doctors = driver.find_elements_by_class_name('detail-data')

        # get info for each doctor and print it out
        for doctor in doctors:
            print('Physician Name:', doctor.find_element_by_class_name('doctorTitle').get_attribute('text'))
            print('Physician Specialty:', doctor.find_element_by_class_name('specialtyMargin').get_attribute('textContent'))
            print('Practicing Address:', str(doctor.find_element_by_class_name('doctorOffice').get_attribute('textContent')).strip())
            print(str(doctor.find_element_by_class_name('doctorAddress').get_attribute('textContent')).strip())
            try:
                print('Phone:', str(doctor.find_element_by_class_name('doctorPhone').get_attribute('textContent'))[5:])
            except:
                print('Phone: n/a')
            print('---')
            num_docs += 1

        # just wait a bit to make sure the browser is ready etc
        sleep(5)

        # click the Next button
        driver.execute_script("x=document.getElementsByClassName('kpPagination__link');x[x.length-1].click();")
