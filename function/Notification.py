import traceback
from function.LineNotify import LineNotify
from datetime import datetime
class Notification:

      def __init__(self):
            self.line_notify = LineNotify()

      
      def send_error(self, message):
            self.line_notify.send_line_notify(f"\n\n 個人ラインシャドウバン検知システム\n\n{message}")
            
            
      def send_confirmation(self):
            self.line_notify.send_line_notify3(f"\n\n 10分間隔のメッセージです")
      
      def send_msg(self, account_name):
            message = f"\n\nメッセージが受信できていません。シャドウバンされている可能性があります。\n\n アカウント名: {account_name}"
            self.line_notify.send_line_notify2(message)
            
      def send_error_with_detail(self, e, message):
            tb = traceback.extract_tb(e.__traceback__)
            # 最後のコールスタックを取得
            last_call_stack = tb[-1]
            file_name = last_call_stack.filename
            line_number = last_call_stack.lineno
            func_name = last_call_stack.name
            self.line_notify.send_line_notify(f"{message}.\n\n An error occurred in file '{file_name}', line {line_number}, in function '{func_name}'.\nError message: {e}")
      

      

