
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def chat_with_gpt(prompt):
    driver_path = "C:\\Users\\Owner\\Desktop\\chromedriver-win64\\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Open ChatGPT
        driver.get("https://chat.openai.com/")
        
        # Wait for the input box to become clickable
        wait = WebDriverWait(driver, 15)
        input_box = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))

        # Click on the input box and send the prompt
        input_box.click()
        input_box.send_keys(prompt)
        input_box.send_keys(Keys.RETURN)

        # Wait for the response to appear
        time.sleep(5)  # Adjust if needed

        # Locate the last message in the chat
        messages = driver.find_elements(By.CSS_SELECTOR, ".message")
        response = messages[-1].text  # Get the last message
        
        return response
    except Exception as e:
        return f"Error: {e}"
    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    prompt = "Explain the benefits of renewable energy."
    response = chat_with_gpt(prompt)
    print("ChatGPT Response:")
    print(response)

