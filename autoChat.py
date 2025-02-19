from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation
import pandas as pd
import time
import csv

# Initialize the automation with optional credentials
chat_bot = ChatGPTAutomation(
    chrome_path= '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"',
    chrome_driver_path= r"C:\\Users\\Owner\\Desktop\\chromedriver-win64\\chromedriver.exe",
)
time.sleep(1)
df = pd.read_excel(r"C:\Users\Owner\Downloads\Sample ISBNs for AI age range testing (1).xlsx")
ISBNs = df["ISBN"].astype(str)
ranges = []
counter = 0

try:
    # Sending a prompt
    chat_bot.send_prompt_to_chatgpt("I am going to supply you ISBNs for you to identify the recommended reading interest age and the recommended reading comprehension age. Do not include anything else in your answer. an example for your entire answer would be the following: interest lower-interest upper,comprehension lower-comprehension upper. Do not include any words or spaces. Be as accurate as possible. Use a wide variety of sources to inform your answer (dont let one source have too much influence).")
    ignore = chat_bot.return_last_response()
    time.sleep(1)
    # print("Response:", response)
    # chat_bot.save_conversation("conversation.txt")
    for I in ISBNs:
        # counter += 1 (to limit prompts while testing)
        # if counter >= 10:
        #     break
        chat_bot.send_prompt_to_chatgpt(I)
        time.sleep(0.1)
        response = chat_bot.return_last_response()
        # print("Response:", response)
        # chat_bot.save_conversation("conversation.txt")
        ranges.append(response.split('\n')[0])

    chat_bot.save_conversation("conversation.txt")
    # csv file: ISBNs 1 out of sync of age ranges
    output_file = "output.csv"

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='\\')
        for x, y in zip(ISBNs, ranges):
            writer.writerow([x, y])

    print("Finished")
    quit()

except Exception as e:
    print("An error occurred:", e)
    raise
finally:
    chat_bot.driver.quit()
# Save conversation to a file
# chat_bot.save_conversation("conversation.txt")
