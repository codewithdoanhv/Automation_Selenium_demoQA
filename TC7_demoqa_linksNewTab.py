import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox

class TestLinksNewTab(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/links")
        self.wait = WebDriverWait(self.driver, 15)

    def test_links_new_tab(self):
        try:
            link = self.wait.until(EC.presence_of_element_located((By.ID, "simpleLink")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
            time.sleep(1)
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.assertEqual(self.driver.current_url, "https://demoqa.com/")
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
        