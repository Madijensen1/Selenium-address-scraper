#Task 3. Using selenium, create a webbot to:
# 1) Go to the following website (https://addressify.com.au/)
# 2) Input the following address in the search field (19 martin pl, sydney)
# 3) Print out the suggestions it retrieves

#import relevent libraries
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#set path variable for chrome driver
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

def address_suggestions(address):
	"""
	prints out the suggested addresses that appear in the drop down box on "https://addressify.com.au/".
	address: string
	"""
	#navigate to link
	driver.get("https://addressify.com.au/")

	#find the search bar, type in address
	search = driver.find_element_by_id("addressid")
	search.send_keys(address)

	try:
		#wait until drop down menu appears, then print out the list of addresses that appear
		#note - increased polling rate from default 0.5s -> 0.001s. Requirement was fastest execution, not lowest cpu load
		suggested = WebDriverWait(driver, 5, 0.001).until(
			EC.visibility_of_element_located((By.ID, "ui-id-1"))
		)
		#drop down has appeared - suggested elements will now be populated
		auto_suggest_list = driver.find_elements_by_xpath("html/body/ul")
		for x in auto_suggest_list:
			print(x.text)
	#print any exception that appears
	except Exception as e:
		print("exception: - ",e)


address_suggestions("19 martin pl, sydney")



