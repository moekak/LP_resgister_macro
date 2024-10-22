from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FunctionParts: 
    def create_webdriver_instance(self):
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        return driver
    
    def access_to_url(self, driver):
        base_url = "https://production1.server-check.tokyo/category"
        driver.get(base_url)
        
    def get_element_by_css(self, driver, waitTime, selector, retry = 1):
        try:
            element = WebDriverWait(driver, waitTime).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            )
            return element
        except Exception as e:
            if(retry > 0):
                self.get_element_by_css(driver, waitTime, selector, retry -1)
            else:
                return False

                    
    def get_element_by_xpath(self, driver, waitTime, xpath, retry = 3):
        try:
            element = WebDriverWait(driver, waitTime).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            if(retry > 0):
                self.get_element_by_xpath(driver, waitTime, xpath, retry -1)
            else:
                return False

                    
    def get_element_by_id(self, driver, waitTime, selector, retry = 3):
        try:
            element = WebDriverWait(driver, waitTime).until(
                EC.element_to_be_clickable((By.ID, selector))
            )
            return element
        except Exception as e:
            if(retry > 0):
                print("retrying...")
                self.get_element_by_id(driver, waitTime, selector, retry -1)
            else:
                print("failed")

        

    def chooseCategory(self, driver, category):
        try:
            print("ww")
            category_btn = self.get_element_by_css(driver, 10, f".{category}")
            href = category_btn.get_attribute("href")
            
            if href:
                print(href)
                driver.get(href)
            else:
                print("エラーが発生しました")

        except Exception as e:
            print(f"エラーが発生しました: {e}")
    
    
    def find_input_by_value_and_class(self, driver, xpath):

        # 明示的な待機を使用して要素を見つける
        element = self.get_element_by_xpath(driver, 3, f"{xpath}")
        
        if element:
            return element
        else:
            return False