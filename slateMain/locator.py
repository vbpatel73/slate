
class mainPage:
    whatWeDo_link = '.dropdown-toggle'
    privateEquity = 'a[title="Private Equity"]'
    instSeparateAccounts = 'a[title="Institutional Separate Accounts"]'
    public = 'a[title="Public"]'
    slateSecurities = 'a[title="Slate Securities"]'
    realEstate_link = 'a[title="Real Estate"]'
    about_link = '//a[contains(text(),"About")]'
    team_link = '//a[contains(text(),"Team")]'
    contact_link = '(//a[contains(text(),"Contact")])[1]'
    Logo = 'a[title="Logo"]'
    investor_login_link = '.investor-login-button'
    terms_link = 'a[href="/terms-use"]'
    privacy_policy_link = 'a[href="/privacy-policy"]'
    contact_us_link = 'a[href="/contact-us"]'
    business_lines_titles = 'div[class="views-field views-field-title"]'

class estatePage:
    selectCountry = '(//select[@title="Country"])[2]'
    selectState = '(//select[@title="State"])[2]'
    city = '(//input[@title="City"])[2]'
    sliderValue = '(//div[@id="edit-field-total-square-ft-value-wrapper"]//span)[1]'
    sliderStart = '(//a[@class="ui-slider-handle ui-state-default ui-corner-all"])[1]'
    sliderEnd = '(//a[@class="ui-slider-handle ui-state-default ui-corner-all"])[2]'
    searchBtn = '(//button[.="Search"])[3]'
    buildingType = '(//div[@title="Building Type" ])[2]//span'
    noOfProperties = 'div[class="view-header"]'

#class aboutPage:

