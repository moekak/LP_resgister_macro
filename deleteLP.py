from function.FunctionParts import FunctionParts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time





function = FunctionParts()

def set_data_to_list():
      path = "./url.txt"
      with open(path, "r", encoding='utf-8') as file:
            return file.readlines()
      
def main():
      try:
            driver = function.create_webdriver_instance()
            function.access_to_url(driver)
            category  = input("カテゴリー名を入力してください:　")
            function.chooseCategory(driver, category)
            
            data = set_data_to_list()
            for item in data:
                  if item.startswith(('http://', 'https://')):
                        item = item.split('://', 1)[1]
                        item = ' '.join(item.split())

                        # 改行文字を除去
                        item = item.replace('\n', '').replace('\r', '')
                  # XPathを使用して要素を見つけドメインのdataIDを取得する
                  
                  xpath = f"//input[@value='{item}' and contains(@class, 'js_domain')]"
                  print(xpath)
                  element = function.find_input_by_value_and_class(driver, xpath)
                  
                  
                  if element == False:
                        print("skip")
                        continue
                  element_dataId = element.get_attribute("data-id")
                  
                  print(element_dataId)
                  # XPathを使用して要素を見つけドメインのdataIDを取得する
                  xpathBtn = f"//button[contains(@class, 'js_delete_btn') and @data-id='{element_dataId}']"
                  
                  print(xpathBtn)
                  element = function.find_input_by_value_and_class(driver, xpathBtn)
                  if element == False:
                        print("skip")
                        continue
                  element_dataId = element.get_attribute("data-id")
                  
                  
                  # 要素まで画面をスクロール
                  try:
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                        time.sleep(10)
                        element.click()   
                  except Exception as e:
                        continue
                  
            
                  element_delete = function.get_element_by_xpath(driver, 3, "//button[@type='submit' and @class='btn btn-danger' and text()='削除']")
                  if element_delete  == False:
                        print("skip")
                        continue
                  element_delete.click()
      except Exception as e:
            print(e)

main()

