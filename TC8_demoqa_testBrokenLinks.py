import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox
import requests

class TestBrokenLinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/broken")
        self.wait = WebDriverWait(self.driver, 15)

    def test_broken_links(self):
        try:
            broken_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Click Here for Broken Link']")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", broken_link)
            href = broken_link.get_attribute("href")
            time.sleep(2)
            response = requests.get(href)
            self.assertEqual(response.status_code, 500)
            time.sleep(2)

            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Ket qua", "Test PASSED")
            root.destroy()

        except Exception as e:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Ket qua", f"Test FAILED\nLoi: {str(e)}")
            root.destroy()
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
