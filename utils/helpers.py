from config.settings import browser, ignored_exceptions, EC, WebDriverWait, By


class Utils:
    @staticmethod
    def switch_frame(selector):
        iframe = WebDriverWait(browser, 50 ,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, f"//iframe[@id='{selector}']")))
        browser.switch_to.frame(iframe)
    
    @staticmethod
    def button_clicker(id):
        browser.execute_script("""
            let vfl_login = document.getElementById('%s')
            if(vfl_login){
                vfl_login.click()
            }
        """ %id)
    
    @staticmethod
    def inner_text_setter(id, text):
        browser.execute_script("""
            let element = document.getElementById('%s');
            if(element) element.innerText = %s
        """ %(id, text))

    @staticmethod    
    def parse_time(time):
        time_list = time.split(":")
        # print("Time ", time_list)
        minutes = time_list[0] 
        seconds = time_list[1]
        minutes = int(minutes) * 60
        seconds = int(seconds)
        return minutes + seconds
