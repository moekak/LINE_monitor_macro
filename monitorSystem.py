
import psutil
from function.LineNotify import LineNotify

line_notify = LineNotify()

def is_python_script_running(script_name):
      # システム上で実行中のすべてのプロセスを反復処理( プロセスID,プロセス名,プロセスを起動したコマンドライン)
      for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            # プロセス名を取得し、プロセス名がpythonで始まるかチェック
            if proc.info['name'].lower().startswith('python'):
                  # 各コマンドライン引数に script_name が含まれているかチェック
                  if any(script_name in arg for arg in proc.info['cmdline']):
                        return True
      return False

# 使用例
script_name = "shadowBan.py"
if is_python_script_running(script_name):
      print(f"{script_name} is running")
else:
      line_notify.send_line_system_error("シャドウバン検知システムが正常に動作していない可能性があります。")
      print(f"{script_name} is not running")