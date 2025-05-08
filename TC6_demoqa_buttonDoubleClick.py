import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox
from selenium.webdriver.common.action_chains import ActionChains

class TestButtonsDoubleClick(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/buttons")
        self.wait = WebDriverWait(self.driver, 15)

    def test_buttons_double_click(self):
        try:
            double_click_button = self.wait.until(EC.presence_of_element_located((By.ID, "doubleClickBtn")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", double_click_button)
            time.sleep(1)
            ActionChains(self.driver).double_click(double_click_button).perform()
            message = self.wait.until(EC.presence_of_element_located((By.ID, "doubleClickMessage")))
            self.assertIn("You have done a double click", message.text)
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
