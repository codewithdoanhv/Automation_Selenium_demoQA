import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox

class TestCheckBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/checkbox")
        self.wait = WebDriverWait(self.driver, 15)

    def test_check_box_selection(self):
        try:
            checkbox = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rct-checkbox")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            time.sleep(1)
            checkbox.click()
            result = self.wait.until(EC.presence_of_element_located((By.ID, "result")))
            self.assertTrue(result.is_displayed())
            time.sleep(2)

            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Ket qua", "Test PASS")
            root.destroy()
            
        except Exception as e:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Ket qua", f"Test FAIL\nLoi: {str(e)}")
            root.destroy()
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()