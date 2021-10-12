from config.config import BET_URL, VIRTUAL_FOOTBALL_URL
from config.settings import browser, EC, ignored_exceptions,WebDriverWait, By
from utils.helpers import Utils 

class Login:
    @staticmethod
    def login(MOBILE_NUMBER, password):
        browser.get(BET_URL)
        browser.get(BET_URL)
        
        browser.find_element_by_id("MobileNumber").send_keys(MOBILE_NUMBER)
        browser.find_element_by_id("Password").send_keys(password)

        browser.find_element_by_id("Login").click()
        # return browser
        browser.refresh()
    
    @staticmethod
    def start():
        browser.get(VIRTUAL_FOOTBALL_URL)
        # Close Cookie
        cookiePopupClose = WebDriverWait(browser, 50 ,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH,"//button[@id='cookiePopupClose']")))
        if cookiePopupClose[0].is_enabled:
            cookiePopupClose[0].click()

        Utils.switch_frame("lobbyIframe")
            
        
    