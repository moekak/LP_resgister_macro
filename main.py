from function.FunctionParts import FunctionParts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


function = FunctionParts()

def set_data_to_list():
    path = "./data.txt"
    with open(path, "r", encoding='utf-8') as file:
        data_list = [line.strip() for line in file]
        return data_list
    
def set_data_to_obj():
    data = set_data_to_list()
    servers = []
    
    for item in data:
        parts = item.split(' ')  # スペースで文字列を区切って配列に変換
        
        if(len(parts) >= 1):
            domain = parts[0]
            group = parts[1]
            # group = parts[2]
            # content = parts[3]
            
            server_dict = {"domain": domain, "group": group}
            servers.append(server_dict)

    return servers



        
def select_lp_create(driver):
    lp_create_btn = function.get_element_by_css(driver, 10, ".js_createLP_btn")
    lp_create_btn.click()


def set_data_to_input(driver):
    data = set_data_to_obj()

    for lp in data:
        try:
            
            print("start!")
            driver.refresh()
            select_lp_create(driver)
            lp_domain = function.get_element_by_css(driver, 10, ".js_lp_domain")
            lp_options = driver.find_elements(By.CSS_SELECTOR, ".select_group")
            lp_content = function.get_element_by_css(driver, 10, ".js_lp_content")
            lp_group_btn = function.get_element_by_css(driver, 10, ".js_lp_group")
            lp_domain.send_keys(lp["domain"])

            print(lp_options)
            
            for option in lp_options:
                print(f"オプションテキスト: {option.text}")
                
                if option.text == lp["group"]:
                    print("一致するオプションが見つかりました。クリックします。")
                    lp_group_btn.click()
                    option.click()
                    submit_btn = function.get_element_by_css(driver, 10, ".js_create_lp")
                    submit_btn.click()
                    break
                else:
                    print("一致するオプションが見つかりませんでした。")
    
        except Exception as e:
            print(e)
        
    
def main():
    try:
        driver = function.create_webdriver_instance()
        function.access_to_url(driver)
        category  = input("カテゴリー名を入力してください::　")
        # category  = "テスト"
        function.chooseCategory(driver, category)
        set_data_to_input(driver)
    except Exception as e:
        print(e)
        
main()