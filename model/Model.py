from function.Dbconnect import DBconnect
from function.Notification import Notification
from function.Restart import Restart


class Model: 
      def __init__(self, driver):
            self.driver = driver
            self.db = DBconnect(self.driver)
            self.notification = Notification()
            self.restart_fn = Restart()
            self.cursor = self.db.dbconnection()
            
            
      def close(self):
            self.db.close()  # デストラクタでデータベース接続を閉じる
      def updateFlag(self, account_name):
            try:
                  self.cursor.execute('UPDATE accounts SET is_banned = "1" WHERE account_name = %s', (account_name,))
                  self.db.conn.commit()  # 変更を永続化
            except Exception as e:
                  self.notification.send_error_with_detail(e, "データーベースのフラグの更新に失敗しました。")
                  self.restart_fn.restart_app(self.driver)
            
            
      def selectFlag(self, account_name):
            try: 
                  self.cursor.execute('SELECT is_banned FROM accounts WHERE account_name = %s', (account_name,))
                  data = self.cursor.fetchone()
                  if data:
                        flag = data[0] 
                        return flag
                  else:
                        return None 
            except Exception as e:
                  self.notification.send_error_with_detail(e, "データーベースのフラグの取得に失敗しました。")
                  self.restart_fn.restart_app(self.driver)
            