import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox
import os

class TestPracticeFormMandatory(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.wait = WebDriverWait(self.driver, 15)

    def test_practice_form_mandatory(self):
        try:
            submit_button = self.wait.until(EC.presence_of_element_located((By.ID, "submit")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(1)
            submit_button.click()
            time.sleep(1)            
            error_border = self.driver.find_element(By.ID, "firstName")
            style = error_border.value_of_css_property("border-color")
            self.assertEqual(style, "rgb(220, 53, 69)")  # Bootstrap's danger color
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
         