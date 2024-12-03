from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation
import time

# Initialize the automation with optional credentials
print("1")
chat_bot = ChatGPTAutomation(
    chrome_path= '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"',
    chrome_driver_path= r"C:\\Users\\Owner\\Desktop\\chromedriver-win64\\chromedriver.exe",
    username="hugodutemple47@gmail.com",
    password="Barca110&"
)
print("2")
time.sleep(5)
print("3")

try:
    # Sending a prompt
    chat_bot.send_prompt_to_chatgpt("Hello, ChatGPT!")
    response = chat_bot.return_last_response()
    print("Response:", response)
    chat_bot.save_conversation("conversation.txt")

except Exception as e:
    print("An error occurred:", e)
finally:
    chat_bot.driver.quit()
# Save conversation to a file
# chat_bot.save_conversation("conversation.txt")
