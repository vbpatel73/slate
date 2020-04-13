from functools import reduce
import pytest
import time
import requests as rq
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import allure
import openpyxl as xl
from selenium import webdriver as wd
from openpyxl.drawing import image
import time, shutil, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from allure_commons.types import AttachmentType
from pyutil import filereplace
import os, random, json , re
from tabulate import tabulate
import win32com.client as cli



smoke = pytest.mark.smoke
regression = pytest.mark.regression
test = pytest.mark.test

os.chdir("Oche")


def Click(driver,locator):
	element =""		
	l = "By.CSS_SELECTOR" if "//" not in locator  else "By.XPATH"	
	try:
		element =  driver.find_element(eval(l),locator)
		element.click()
	except :
		try:
			element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((eval(l), locator))) # visibility_of_element_located
			driver.execute_script("arguments[0].scrollIntoView({behaviour:'smooth'});", element)
			driver.execute_script("window.scrollBy(0, -150);")		
			element.click()
		except:
			try:
				element =  driver.find_element(eval(l),locator)
				driver.execute_script("arguments[0].click();",element)
			except NoSuchElementException as e:			
				print(element.text +" has been failed")
	
	

def Type(driver,locator,val):
	element =""		
	l = "By.CSS_SELECTOR" if "//" not in locator  else "By.XPATH"	
	try:
		element =  driver.find_element(eval(l),locator)
		element.send_keys(val)
	except:
		try:
			element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((eval(l), locator))) # visibility_of_element_located
			driver.execute_script("arguments[0].scrollIntoView({behaviour:'smooth'});", element)
			driver.execute_script("window.scrollBy(0, -150);")
			element.send_keys(val)
		except:
			try:
				element =  driver.find_element(eval(l),locator)
				driver.execute_script("arguments[0].value ='"+val+"';",element)
			except NoSuchElementException as e:
				print(element.text +" has been failed")	
	

def Element(driver,locator):
	element =""			
	#waitForpageToLoad(driver)
	l = "By.CSS_SELECTOR" if "//" not in locator  else "By.XPATH"
	
	try:
		element =  driver.find_element(eval(l),locator)
	except:
		try: 
			element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((eval(l), locator)))  # visibility_of_element_located
		except:
			try:
				element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((eval(l), locator)))
				# driver.execute_script("arguments[0].scrollIntoView({behaviour:'smooth'});", element)
				# driver.execute_script("window.scrollBy(0, -150);")
			except NoSuchElementException as e:
				print(element.text +" has been failed")
	return element

def Elements(driver,locator):
	element =""			
	#waitForpageToLoad(driver)
	l = "By.CSS_SELECTOR" if "//" not in locator  else "By.XPATH"

	try:
		element = WebDriverWait(driver, 10).until(
			EC.visibility_of_all_elements_located((eval(l), locator)))  # visibility_of_element_located
	except NoSuchElementException as e:
		Screenshot(driver)
		print(element.text +" has been failed")	
	return element

def clickToNavigate(driver,loc):
	timeout = time.time()+60
	old = driver.current_url	
	Element(driver,loc).click()
	time.sleep(1)
	while timeout >time.time():
		new = driver.current_url		
		if new == old :			
			time.sleep(0.5)
		else : 			
			time.sleep(1)
			break

def driver(v="CHROME"):	
		
	if str.upper(v) == "CHROME" :
		driver = wd.Chrome(r"..\drivers\chromedriver.exe")		
	elif str.upper(v) == "FIREFOX" :
		driver = wd.Firefox(executable_path=r"..\drivers\geckodriver.exe")		
	elif str.upper(v) == "IE":
		driver = wd.Ie(r"..\drivers\IEDriverServer.exe")	
	driver.implicitly_wait(5)
		
	driver.maximize_window()	
	return driver

def waitForpageToLoad(browser):
	timeout = time.time()+60
	time.sleep(1)
	while timeout >time.time():
		state = browser.execute_script("return document.readyState")
		if state != "complete" :
			print("waiting for page to load")
			time.sleep(0.5)
		else:			
			break

# def exeJs(driver,loc,action,value='') :
# 	Ele = Element(driver,loc)	
# 	if action == "click" :
# 		driver.execute_script("arguments[0].click();",Ele)
# 	elif action == "type" :
# 		driver.execute_script("arguments[0].value ='"+value+"';",Ele)
# 	time.sleep(1)	


	

def Screenshot(browser):
	browser.get_screenshot_as_png()
	#allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
	

def sendEmailReport():
	
	with open('.report.json','r') as e:
		a = json.load(e)

	tt = datetime.datetime.fromtimestamp(round(a["created"], 0))
	et = str(round(a["duration"], 2))
	failed = str(a["summary"]["failed"]) if "failed" in a["summary"] else '0'
	passed = str(a["summary"]["passed"]) if "passed" in a["summary"] else '0'
	total = str(a["summary"]["total"]) if "total" in a["summary"] else '0'
	collected = str(a["summary"]["collected"]) if "collected" in a["summary"] else '0'
	skipped = str(a["summary"]["skipped"]) if "skipped" in a["summary"] else '0'
	ef = str(a["summary"]["expected failures"]) if "expected failures" in a["summary"] else '0'
	error = str(a["summary"]["error"]) if "error" in a["summary"] else '0'
	ep = str(a["summary"]["expected passed"]) if "expected passed" in a["summary"] else '0'
	url = "http://127.0.0.1:8000/"+str(tt.strftime('%y%m%d_%H%M'))
	#shutil.copy(root_dir+r'\report.txt',root_dir+r'\report1.txt')
	
	with open('report.txt', 'r') as f:
		content = f.read()
	
	with open('report1.txt', 'w') as g:
		replacement = [("#total", total), ("#et", et), ("#time", str(tt)), ("#passed", passed), ("#skipped", skipped),
					   ("#ef", ef), ("#error", error), ("#ep", ep), ("#failed", failed),("#url",url)]
		d = reduce(lambda a, kv: a.replace(*kv), replacement, content)
		# print(d)
		g.write(d)
	
	with open('report1.txt', 'r') as g:	
				c =g.read()
	
	
	os.system(r"allure generate report -c -o reports/" + str(tt.strftime('%y%m%d_%H%M')))
	time.sleep(3)

	outlook = cli.Dispatch('outlook.application')
	mail = outlook.CreateItem(0)
	# mail.Display ()  # required to paste chart
	mail.To = 'vikash.patel@onx.com'
	mail.Subject = 'Test Execution Report of  ' + str(tt)
	mail.HTMLBody = c
	mail.Send()

	time.sleep(5)

	#os.remove('report1.txt')	
	#shutil.rmtree("report")

#sendEmailReport()

# if __name__ == "__main__" :
# 	driver()
# 	load_data()
# 	load_element()
# 	Data()
# 	Element()
# 	sendEmailReport()