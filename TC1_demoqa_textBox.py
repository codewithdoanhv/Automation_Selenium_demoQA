import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox

class TestTextBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")
        self.wait = WebDriverWait(self.driver, 15)

    def test_enter_text_box(self):
        try:
            full_name = self.wait.until(EC.presence_of_element_located((By.ID, "userName")))
            full_name.send_keys("Doan demo automation")
            time.sleep(1)
            submit_button = self.wait.until(EC.presence_of_element_located((By.ID, "submit")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(1)
            submit_button.click()

            output = self.wait.until(EC.presence_of_element_located((By.ID, "name")))
            self.assertIn("Doan demo automation", output.text)

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