import datetime
import time
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException



def take_input(events):
    n = int(input("Enter number of people you want to send: "))
    for _ in range(n):
        date = input("Enter Date (YYYY-MM-DD): ")
        details = []
        details.append(int(input("Enter Hour in 24-hour format: ")))
        details.append(int(input("Enter Minute: ")))
        contact_type = input("Enter Contact Type (Saved/New): ")
        details.append(contact_type)
        if contact_type == 'Saved':
            details.append(input("Enter contact name: "))
        else:
            details.append(input("Enter contact number with + and country code: "))
        details.append(input_message())
        events[date].append(details)


def input_message():
    print("Enter the message and use the symbol '~' to end the message:\nYour message: ")
    message = []
    while True:
        temp = input()
        if temp.endswith("~"):
            message.append(temp[:-1])
            break
        message.append(temp)
    return "\n".join(message)


def calculate_sleeptime(time_hour, time_min):
    if time_hour not in range(24) or time_min not in range(60):
        raise ValueError("Invalid Time Format")

    current_time = datetime.datetime.now()
    send_time = current_time.replace(hour=time_hour, minute=time_min, second=0, microsecond=0)

    if send_time < current_time:
        return -1  # Time has already passed today

    return (send_time - current_time).total_seconds()


def type_msg_in_inputbox(input_box, message, driver):
    for ch in message:
        if ch == "\n":
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
                Keys.SHIFT).perform()
        else:
            input_box.send_keys(ch)
    input_box.send_keys(Keys.ENTER)
    time.sleep(1)


def send_message_saved_contact(driver, target, msg):
    link = "https://web.whatsapp.com"
    driver.get(link)
    driver.implicitly_wait(30)

    for _ in range(5):
        try:
            user = driver.find_element(By.XPATH, f"//span[@title='{target}']")
            user.click()
            input_box = driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
            type_msg_in_inputbox(input_box, msg, driver)
            print("Message sent successfully to saved contact")
            return
        except Exception as e:
            print("Failed to send message. Retrying...", e)
            time.sleep(1)

    print("Message not sent after multiple attempts")


def send_message_new_contact(driver, phone_number, msg):
    try:
        link = f"https://web.whatsapp.com/send?phone={phone_number}&text&source&data&app_absent"
        driver.get(link)

        # Take a screenshot for debugging
        driver.save_screenshot('whatsapp_debug.png')

        # Wait until the input box is present and clickable
        try:
            input_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='1']"))
            )
            type_msg_in_inputbox(input_box, msg, driver)
            print("Message sent successfully to new contact")
        except TimeoutException:
            print("Failed to locate the message input box. It may not be loaded properly.")
    except NoSuchElementException as e:
        print("Message not sent to new contact. Element not found:", e)
    except Exception as e:
        print("Message not sent to new contact. Unexpected error:", e)


def send_messages(events):
    edge_service = Service("C:\\Users\\user\\edgedriver_win64\\msedgedriver.exe")
    driver = webdriver.Edge(service=edge_service)
    driver.implicitly_wait(15)

    date_today = str(datetime.date.today())

    for date, messages in events.items():
        if date == date_today:
            messages.sort()
            for details in messages:
                left_time = calculate_sleeptime(details[0], details[1])
                if left_time < 0:
                    print("Message cannot be sent as the time has already passed")
                    continue
                print(f"Sending message to {details[3]} after {left_time} seconds")
                time.sleep(left_time)
                if details[2] == 'Saved':
                    send_message_saved_contact(driver, details[3], details[4])
                else:
                    send_message_new_contact(driver, details[3], details[4])
        else:
            print(f"Cannot send messages scheduled for {date} today")

    driver.quit()


events = defaultdict(list)
take_input(events)
print(events)
send_messages(events)
