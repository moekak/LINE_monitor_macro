import os
from dotenv import load_dotenv
from function.Notification import Notification
import mysql.connector
from function.Restart import Restart

# .env ファイルを読み込む
load_dotenv()

class DBconnect: 
      def __init__(self, driver):
            self.conn = None
            self.cursor = None
            self.driver = driver
            self.notification = Notification()
            self.restart_fn = Restart()
            

      def dbconnection(self): 
            try:
                  self.conn = mysql.connector.connect(
                        host=os.getenv('HOST'),
                        user=os.getenv('USER'),
                        password=os.getenv('PASSWORD'),
                        database=os.getenv('DATABASE')
                  )
            except Exception as e:
                  self.notification.send_error_with_detail(e, "データベースコネクションエラーが発生しました。")
                  self.restart_fn.restart_app(self.driver)
                  
            self.cursor = self.conn.cursor()
            return self.cursor

      def close(self):
            if self.cursor:
                  self.cursor.close()
            if self.conn:
                  self.conn.close()
