from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from function.Notification import Notification
from model.Model import Model

class PartsFn:
      
      def __init__(self, driver):
            self.notification = Notification()
            self.model = Model(driver)
            
      def retry_get_element(self,wait, by, value, retries=1, delay=2):
            for attempt in range(retries):
                  try:
                        element = wait.until(EC.presence_of_element_located((by, value)))
                        return element, None
                  except (TimeoutException, Exception) as e:
                        if attempt < retries - 1:
                              print(f"Retry {attempt + 1}/{retries} failed: {e}. Retrying in {delay} seconds...")
                              time.sleep(delay)
                        else:
                              print("All retries failed.")
                              print(value)
                              return False, e
                        
      # テキストファイルからURLデータを取り出す
      def parse_text_file(file_path):
            account_url = {}
            with open(file_path, 'r') as file:
                  for line in file:
                        parts = line.strip().split(None, 1)
                        if len(parts) == 2:
                              key, value = parts
                              account_url[key] = value
            return account_url
      
      def updateBanFlag(self,account_name):
            flag = self.model.selectFlag(account_name)
            if flag == "0": 
                  self.notification.send_msg(account_name)
                  self.model.updateFlag(account_name)