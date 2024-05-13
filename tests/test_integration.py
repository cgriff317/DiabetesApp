import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pyautogui
import time


class TestDashAppIntegration(unittest.TestCase):
    def setUp(self):
        # Setup Edge WebDriver
        service = Service(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        options.use_chromium = True  # Ensure using the Chromium-based Edge
        options.headless = True  # Run in headless mode
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get("http://127.0.0.1:8050/")  # URL where the Dash app is running

    def test_file_upload(self):
        # Wait for the button to be clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Select Files')]"))
        )
        select_files_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Select Files')]")
        select_files_button.click()

        # Wait for the file input to be visible and ready for interaction
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.find_element(By.ID, "upload-data").is_displayed() and
                           driver.find_element(By.ID, "upload-data").is_enabled()
        )

        # Use PyAutoGUI to handle the file explorer
        pyautogui.write(r'C:\Users\crgriffin\Diabetes.csv')  # Type the file path directly
        pyautogui.press('enter')  # Press Enter to submit the file path and close the dialog

        # Verify if visualization content appears
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, "visualization"))
        )
        visualization_content = self.driver.find_element(By.ID, "visualization")
        self.assertTrue(visualization_content.is_displayed(), "Visualization content is not displayed")

    def tearDown(self):
        # Close the browser window and quit the driver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
