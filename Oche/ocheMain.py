from .MainSetup import *
from .locator import *


@pytest.fixture(scope="session", autouse=True)#, params=[driver("chrome")])
												
def browser(getBrowser):
	d = driver(getBrowser)
	d.get('http://oche.ca/')	
	yield d
	d.close()
	

@regression
@allure.title("Verify Who We are link")
@allure.feature("Who We are link")
def whoWeArePage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.whoWeAre)).perform()
	Screenshot(browser)

@regression
@allure.title("Verify meet The Team link")
@allure.feature("meet The Team link")
def meetTheTeamPage(browser):	
	Click(browser, mainPage.meetTheTeam)	
	Screenshot(browser)

@regression
@allure.title("Verify Join Oche Team link")
@allure.feature("Join Oche Team link")
def joinOcheTeamPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.whoWeAre)).perform()
	Click(browser,mainPage.joinOcheTeam)
	Screenshot(browser)

@regression
@allure.title("Verify How we Help link")
@allure.feature("How we Help link")
def howWeHelpPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.howWeHelp)).perform()
	Screenshot(browser)

@regression
@allure.title("Verify Questions link")
@allure.feature("Questions link")
def questionsPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.howWeHelp)).perform()
	Click(browser, mainPage.questions)
	Screenshot(browser)

@regression
@allure.title("Verify oche Approach link")
@allure.feature("oche Approach link")
def ocheApproachPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.howWeHelp)).perform()
	Click(browser, mainPage.ocheApproach)
	Screenshot(browser)

@regression
@allure.title("Verify Resources link")
@allure.feature("Resources link")
def resourcesPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.howWeHelp)).perform()
	Click(browser, mainPage.resources)
	Screenshot(browser)

@regression
@allure.title("Verify Testimonials link")
@allure.feature("Testimonials link")
def testimonialsPage(browser):
	ActionChains(browser).move_to_element(Element(browser,mainPage.howWeHelp)).perform()
	Click(browser, mainPage.testimonials)
	Screenshot(browser)

@regression
@allure.title("Verify who Is Vulnerable link")
@allure.feature("who Is Vulnerable link")
def whoIsVulnerablePage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.howWeHelp)).perform()
	Click(browser, mainPage.whoIsVulnerable)
	Screenshot(browser)

@regression
@allure.title("Verify News & Reports link")
@allure.feature("News & Reports link")
def newsReportsPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.newsReports)).perform()
	Screenshot(browser)

@regression
@allure.title("Verify oche Brochures link")
@allure.feature("oche Brochures link")
def ocheBrochuresPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.newsReports)).perform()
	Click(browser, mainPage.ocheBrochures)
	Screenshot(browser)

@regression
@allure.title("Verify Presentations link")
@allure.feature("Presentations link")
def presentationsPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.newsReports)).perform()
	Click(browser, mainPage.presentations)
	Screenshot(browser)

@regression
@allure.title("Verify Reports link")
@allure.feature("Reports link")
def reportsPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.newsReports)).perform()
	Click(browser, mainPage.reports)
	Screenshot(browser)

@regression
@allure.title("Verify Terms Of Reference link")
@allure.feature("Terms Of Reference link")
def termsOfReferencePage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.newsReports)).perform()
	Click(browser, mainPage.termsOfReference)
	Screenshot(browser)

@regression
@allure.title("Verify Outreach link")
@allure.feature("Outreach link")
def outreachPage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.newsReports)).perform()
	Click(browser, mainPage.outreach)
	Screenshot(browser)

@regression
@allure.title("Verify Media link")
@allure.feature("Media link")
def whoIsVulnerablePage(browser):
	ActionChains(browser).move_to_element(Element(browser, mainPage.newsReports)).perform()
	Click(browser, mainPage.media)
	Screenshot(browser)

@regression
@allure.title("Verify Events link")
@allure.feature("Events link")
def eventsPage(browser):
	Click(browser, mainPage.events)
	Screenshot(browser)

@regression
@allure.title("Verify contact Us link")
@allure.feature("contact Us link")
def contactUsPage(browser):
	Click(browser, mainPage.contactUs)
	Screenshot(browser)

@regression
@allure.title("Verify Request Referral link")
@allure.feature("Request Referral link")
def requestReferralPage(browser):
	Click(browser, mainPage.requestReferral)
	Screenshot(browser)
# pytest -n=2 --tb=no --alluredir=Selenium//report Selenium/slateMain.py
# allure serve Pytest/reports
# python -m http.server 8000 --bind 127.0.0.1

