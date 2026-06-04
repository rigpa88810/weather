import requests
import os
from dotenv import load_dotenv

# 載入 .env 檔案中的環境變數
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "zh_tw"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            
            print("\n" + "="*30)
            print(f" 城市：{city_name.capitalize()}")
            print(f" 溫度：{temp}°C")
            print(f" 濕度：{humidity}%")
            print(f" 狀況：{description}")
            print("="*30 + "\n")
        else:
            print(f"❌ 查詢失敗：找不到 '{city_name}'，請確認拼字是否正確。")
            print(f"🛠️ 偵錯資訊：狀態碼 {response.status_code}, 詳細訊息 {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ 網路連線發生錯誤: {e}")

if __name__ == "__main__":
    print("歡迎使用即時天氣查詢系統！(輸入 'q' 離開)")
    while True:
        user_input = input("請輸入英文城市名稱 (例如: Taipei, Tokyo, London): ")
        if user_input.lower() == 'q':
            print("感謝使用，再見！")
            break
        elif user_input.strip() == "":
            print("請勿輸入空白！")
        else:
            get_weather(user_input)