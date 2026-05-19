import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{folder}/{name}_{timestamp}.png"

    driver.save_screenshot(file_path)
    return file_path
