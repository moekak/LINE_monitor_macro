import time, os, sys
from function.Notification import Notification

class Restart:
      
      def restart_app(self,driver):
            try:
                  # LINEアプリのパッケージ名とアクティビティ名を設定
                  package_name = 'com.android.chrome'
                  
                  # アプリを停止
                  driver.terminate_app(package_name)
                  
                  # 少し待機
                  time.sleep(1)
                  
                  # アプリを再起動
                  driver.activate_app(package_name)
                  time.sleep(1)
                  
                  # スクリプトを再実行
                  self.restart_script()
            except Exception as e:
                  notification = Notification()
                  notification.send_error_with_detail(e, "スクリプトの再実行に失敗しました")

      def restart_script(self):
            print("Restarting script...")
            # pythonファイルの特定をする
            python = sys.executable
            # 現在のプロセスを終(os.execl)
            os.execl(python, python, *sys.argv)