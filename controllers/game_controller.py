import time
from authentications.login import browser
from config.settings import browser, EC, ignored_exceptions,WebDriverWait, By
from config.config import ALL_WEAKS_TEAMS
from utils.helpers import Utils

class GameController:
    @staticmethod
    def get_all_teams():
        all_teams = WebDriverWait(browser, 50 ,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@class='matchlist-item-teams']")))
        # try:
            

        for team in all_teams:
            print(team.text)
            more_btn = team.find_element_by_tag_name("span")
            # print(more_btn)
            # more_btn.click()
        
        Utils.switch_frame("vflmframe")
        get_time = browser.find_element_by_css_selector(".countdown_amount")#WebDriverWait(browser, 50 ,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH,"//span[@class='countdown_amount']")))
        print(get_time.text) 
        whole_time = Utils.parse_time(get_time.text)
        print(whole_time)
        # Utils.switch_frame("lobbyIframe")
             

        # except Exception as exc:
        #     print(exc)

    @staticmethod
    def statistics():
        stats = WebDriverWait(browser, 50 ,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='statisticsButton']")))
        stats.click()
        all_windows = browser.window_handles
        last_window = all_windows[len(all_windows) - 1]
        browser.switch_to.window(last_window)
        time.sleep(5)
        browser.close()

    @staticmethod
    def check_h2h(index):
        Utils.switch_frame("lobbyIframe")
        h2h = WebDriverWait(browser, 50 ,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH,"//span[@class='match-head-to-head icon']")))
        print(h2h[index].click())        