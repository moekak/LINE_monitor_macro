from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from function.PartsFn import PartsFn
import time
from function.Notification import Notification
from function.Restart import Restart


#Desired Capabilitiesの設定
capabilities = dict(
      platformName='Android',  # 操作対象のプラットフォームを指定します
      automationName='UiAutomator2',  # 使用する自動化エンジンを指定します
      deviceName='SO-05K',  # 操作対象のデバイス名を指定します
      udid='BH903JSCD1',  # デバイスのUDIDを指定
      language='en',  # デバイスの言語設定
      newCommandTimeout=3600  # セッションのタイムアウトを800秒に設定
)


appium_server_url = 'http://localhost:4721' 

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
driver.update_settings({"enforceXPath1": True})

wait = WebDriverWait(driver, 10)
# account_url = {"sg6": "https://line.me/ti/p/E--eFVyG0U", "sg7": "https://line.me/ti/p/21ZdxBNC_O", "sg8": "https://line.me/ti/p/40KjltyGYz"}
pasrts_fn = PartsFn(driver)
notification = Notification()
restart_fn = Restart()

while True:
      notification.send_confirmation()
      file_path = "./url.txt"
      account_url = PartsFn.parse_text_file(file_path)
      print(account_url)
      exit
      
      for key, value in account_url.items():
            try:
                  # googleの検索をクリックする
                  element, error = pasrts_fn.retry_get_element(wait, By.XPATH, '(//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"])')
                  if not element:
                        element_home_btn, error = pasrts_fn.retry_get_element(wait, By.XPATH, '(//android.widget.ImageButton[@content-desc="ホームページを開く"])')
                        if element_home_btn:
                              element_home_btn.click()
                              element, error = pasrts_fn.retry_get_element(wait, By.XPATH, '(//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"])')
                              if element:
                                    element.click()
                              else:
                                    notification.send_error("Googleの検索が見つかりませんでした。再度スクリプトを実行します。")
                                    restart_fn.restart_app(driver)  
                        else:
                              notification.send_error("Googleの検索が見つかりませんでした。再度スクリプトを実行します。")
                              restart_fn.restart_app(driver)  
                  else:
                        element.click()
                        
                  # 検索単語を入れる
                  element_url, error = pasrts_fn.retry_get_element(wait, By.XPATH, '(//android.widget.EditText[@resource-id="com.android.chrome:id/url_bar"])')
                  if not element:
                        notification.send_error("Googleの検索欄が見つかりませんでした。再度スクリプトを実行します。")
                        restart_fn.restart_app(driver)
                        print("no element")
                  else:
                        print(element)
                        element_url.click()
                        element_url.send_keys(value)
                        # Enterキーを押す
                        driver.press_keycode(66)
                        
                  # LINEアプリを開く
                  try:
                        
                        element_btn, error = pasrts_fn.retry_get_element(wait, By.XPATH, '(//android.view.View[@content-desc="LINEアプリを開く"])')
                        element_btn.click()
                  except Exception as e:
                        notification.send_error("LINEのアプリの起動に失敗しました。再度スクリプトを実行します。")
                        restart_fn.restart_app(driver)
                        
                        
                  try:
                        
                        elements_addbtn = WebDriverWait(driver, 7).until(
                              EC.presence_of_all_elements_located((By.XPATH, '(//android.widget.LinearLayout[@resource-id="jp.naver.line.android:id/user_profile_button_area"]/android.view.ViewGroup[1])'))
                        )
                  
                        print(len(elements_addbtn))

                        if len(elements_addbtn) > 0:
                              element_close_btn, error = pasrts_fn.retry_get_element(wait, By.XPATH, '(//android.widget.ImageView[@content-desc="閉じる"])')
                              
                              if element_close_btn:
                                    element_close_btn.click()
                              else:
                                    notification.send_error("LINE画面の閉じるボタンが見つかりませんでした。再度スクリプトを実行します。")
                                    restart_fn.restart_app(driver)
                                    print("no element found")
                        else:
                              # バンされてるかも
                              package_name = 'jp.naver.line.android'
                              driver.terminate_app(package_name)
                              package_name = 'com.android.chrome'
                              driver.activate_app(package_name)
                              
                              pasrts_fn.updateBanFlag(key)
                  except Exception as e:
                        package_name = 'jp.naver.line.android'
                        driver.terminate_app(package_name)
                        package_name = 'com.android.chrome'
                        driver.activate_app(package_name)
                        
                        pasrts_fn.updateBanFlag(key)


            except Exception as e:
                  print(f"{e}: エラーが発生しました")
                  notification.send_error_with_detail(e, "エラーが発生しました。再度スクリプトを実行します。")
                  restart_fn.restart_app(driver)
      
      print("restart within 10 mins")
      time.sleep(600)