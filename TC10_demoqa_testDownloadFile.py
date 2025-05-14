import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import tkinter as tk
from tkinter import messagebox

class TestDownloadFile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/upload-download")
        self.wait = WebDriverWait(self.driver, 10)

    def test_download_file(self):
        try:
            download_button = self.wait.until(EC.presence_of_element_located((By.ID, "downloadButton")))
            self.driver.execute_script ("arguments[0].scrollIntoView(true);", download_button)
            time.sleep(2)
            download_button.click()
            time.sleep(5)
            # Check if the file is downloaded
            download_path = os.path.expanduser("~/Downloads/sampleFile.jpeg")
            self.assertTrue(os.path.exists(download_path))
            time.sleep(2)

            # Show a message box to indicate success
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            messagebox.showinfo("Ket qua", "Test Download File Passed")
            root.destroy()  # Close the message box

        except Exception as e:
            # Show a message box to indicate failure           
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            messagebox.showinfo("Ket qua",f"Test Download File Failed: {str(e)}")
            root.destroy()  # Close the message box
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

