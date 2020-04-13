from .MainSetup import *
from .locator import *



@pytest.fixture(scope="session", autouse=True)
														
def browser(getBrowser):
	d = driver(getBrowser)
	d.get('https://www.slateretailreit.com/')	
	yield d
	d.close()
	



@regression
@allure.feature("Main page Links")
def test_main_page(browser):
	Click(browser,mainPage.whatwedo_link)
	Screenshot(browser)


@regression
@allure.feature("Investors Page")
@allure.testcase("Verify Investor page")
def investorPage(browser):
	Click(browser, mainPage.investorsLink)	
	Click(browser, mainPage.financialReports)
	Click(browser, mainPage.unitInformation)
	Screenshot(browser)
	Click(browser, mainPage.presentations)
	Click(browser, mainPage.financialReports)
	Click(browser, mainPage.distributions)
	Screenshot(browser)
	Click(browser, mainPage.analystCoverage)
	Click(browser, mainPage.regulatoryFilings)
	Click(browser, mainPage.taxInformation)
	Click(browser, mainPage.governance)
	Screenshot(browser)
	Click(browser, mainPage.committees)
	Click(browser, mainPage.policies)
	Click(browser, mainPage.furtherInformation)



@regression
@allure.feature("Portfolio Page")
@allure.testcase("Verify Portfolio page")
def test_searchOnEstatePage(browser):
	Click(browser, mainPage.portfolioLink)
	Click(browser, mainPage.state)
	Select(Element(browser, mainPage.state)).select_by_visible_text('Ohio')
	Type(browser,mainPage.city,'Lancaster')	
	browser.execute_script("arguments[0].style = 'left: 15%;';", Element(browser,mainPage.sliderStart))
	browser.execute_script("arguments[0].style = 'left: 85%;';", Element(browser, mainPage.sliderEnd))	
	Click(browser,mainPage.searchBtn)
	assert Element(browser,mainPage.noOfProperties)
	Screenshot(browser)

@regression
@allure.feature("Team Page")
def test_about_page(browser):
	Click(browser, mainPage.teamLink)
	Type(browser, mainPage.searchByName,'Andrew' +Keys.ENTER)
	time.sleep(2)
	assert Element(browser,mainPage.filteredName).text == 'Andrew Agatep'
	Screenshot(browser)


@regression
@allure.feature("News Page")
def test_news_page(browser):
	Click(browser, mainPage.newsLink)
	Click(browser,mainPage.agreeCookie)
	Click(browser,mainPage.AcquisitionsDispositions)
	Screenshot(browser)
	Click(browser,mainPage.Appointment)
	Screenshot(browser)
	Click(browser,mainPage.BoardofTrustees)
	Screenshot(browser)
	Click(browser,mainPage.Distributions)
	Screenshot(browser)
	Click(browser,mainPage.EquityOffering)
	Screenshot(browser)
	Click(browser,mainPage.FinancialResults)
	Screenshot(browser)
	Click(browser,mainPage.Other)
	Screenshot(browser)
	Click(browser,mainPage.Webcast)
	Screenshot(browser)

@regression
@test
@allure.feature("Terms Page")
def test_terms_page(browser):
	Click(browser, mainPage.termsLink)
	Screenshot(browser)

@regression
@test
@allure.feature("Privacy Policy Page")
def test_privacy_page(browser):
	Click(browser, mainPage.privacyPolicyLink)
	Screenshot(browser)

@regression
@test
@allure.feature("Contact Page")
def test_contact_page(browser):
	Click(browser, mainPage.contactLink)
	Screenshot(browser)

@regression
@test
@allure.feature("Sign Up Page")
def test_signup_page(browser):
	Click(browser, mainPage.signUpBtn)
	Screenshot(browser)





# pytest -n=2 --tb=no --alluredir=Selenium//report Selenium/test_slateMain.py
# allure serve Pytest/reports
# python -m http.server 8000 --bind 127.0.0.1

