import requests

class LineNotify:
      def send_line_notify(self, notification_message):
            """
            LINEに通知する
            """
            line_notify_token = 'YRYDpNFVfaCQJgWAmQsJ2jA7tsb58AxLdAaljiyZk0m'  # アクセストークンをここに入力
            line_notify_api = 'https://notify-api.line.me/api/notify'
            headers = {'Authorization': f'Bearer {line_notify_token}'}
            data = {'message': notification_message}
            try:
                  response = requests.post(line_notify_api, headers=headers, data=data, timeout=10 )
                  return response.status_code, response.text
            except ConnectionError:
                  print("接続に失敗しました。ネットワーク接続を確認してください。")
            except requests.exceptions.Timeout:
                  print("リクエストがタイムアウトしました。")
            except Exception as e:
                  print(e)
                  
      def send_line_notify3(self, notification_message):
            """
            LINEに通知する
            """
            line_notify_token = 'SPFMi1mwV06U8mkCQGHbagNqp4GWlIKpLHdtG9w8AD0'  # アクセストークンをここに入力
            line_notify_api = 'https://notify-api.line.me/api/notify'
            headers = {'Authorization': f'Bearer {line_notify_token}'}
            data = {'message': notification_message}
            try:
                  response = requests.post(line_notify_api, headers=headers, data=data, timeout=10 )
                  return response.status_code, response.text
            except ConnectionError:
                  print("接続に失敗しました。ネットワーク接続を確認してください。")
            except requests.exceptions.Timeout:
                  print("リクエストがタイムアウトしました。")
            except Exception as e:
                  print(e)
      
      def send_line_notify2(self, notification_message):
            """
            LINEに通知する
            """
            line_notify_token = 'W85cKc2AE8vzyWjFE50lNzQaxxYssWrAIG8grB5d3ho'  # アクセストークンをここに入力
            line_notify_api = 'https://notify-api.line.me/api/notify'
            headers = {'Authorization': f'Bearer {line_notify_token}'}
            data = {'message': notification_message}
            try:
                  response = requests.post(line_notify_api, headers=headers, data=data, timeout=10 )
                  return response.status_code, response.text
            except ConnectionError:
                  print("接続に失敗しました。ネットワーク接続を確認してください。")
            except requests.exceptions.Timeout:
                  print("リクエストがタイムアウトしました。")
            except Exception as e:
                  print(e)
                  
      def send_line_system_error(self, notification_message):
            """
            LINEに通知する
            """
            line_notify_token = '74wEC7ut48nhaxM6Pj7q9X5rlFvoRI0g294dvVkbwDU'  # アクセストークンをここに入力
            line_notify_api = 'https://notify-api.line.me/api/notify'
            headers = {'Authorization': f'Bearer {line_notify_token}'}
            data = {'message': notification_message}
            try:
                  response = requests.post(line_notify_api, headers=headers, data=data, timeout=10 )
                  return response.status_code, response.text
            except ConnectionError:
                  print("接続に失敗しました。ネットワーク接続を確認してください。")
            except requests.exceptions.Timeout:
                  print("リクエストがタイムアウトしました。")
            except Exception as e:
                  print(e)
      

      
            
