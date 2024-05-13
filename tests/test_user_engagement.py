import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_user_engagement():
    # Set up the Edge WebDriver
    service = Service(EdgeChromiumDriverManager().install())  # This automatically manages the driver
    driver = webdriver.Edge(service=service)

    try:
        # Open the local Dash application
        driver.get("http://localhost:8050")

        # Wait for the upload component to be visible and clickable
        wait = WebDriverWait(driver, 10)
        file_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='file']")))

        # Specify the file path
        file_path = r'C:\Users\crgriffin\PycharmProjects\Diabetes\Diabetes.csv'

        # Set the file in the upload component
        file_input.send_keys(file_path)

        process_button = wait.until(EC.element_to_be_clickable((By.ID, 'evaluate-button')))
        process_button.click()

        # Wait for some expected outcome, e.g., a success message or a table with data
        result_div = wait.until(EC.visibility_of_element_located((By.ID, 'output-data-upload')))
        assert 'File uploaded' in result_div.text  # Adjust the expected text based on your application response

    finally:
        # Close the browser window
        driver.quit()


if __name__ == "__main__":
    test_user_engagement()
