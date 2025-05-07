import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox

class TestRadioButton(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/radio-button")
        self.wait = WebDriverWait(self.driver, 15)

    def test_radio_button_selection(self):
        try:        
            radio_label = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "label[for='yesRadio']")
            ))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_label)
            radio_label.click()
            
            output = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text-success")))
            self.assertIn("Yes", output.text)
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