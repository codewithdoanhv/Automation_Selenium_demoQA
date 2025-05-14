import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox
import os

class TestPracticeFormSubmission(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.wait = WebDriverWait(self.driver, 15)

    def test_links_new_tab(self):
        try:
            first_name = self.wait.until(EC.presence_of_element_located((By.ID, "firstName")))
            first_name.send_keys("John")
            self.driver.find_element(By.ID, "lastName").send_keys("Doe")
            self.driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
            self.driver.find_element(By.XPATH, "//label[text()='Male']").click()
            self.driver.find_element(By.ID, "userNumber").send_keys("1234567890")
            submit_button = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(1)
            submit_button.click()
            modal = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
            self.assertTrue(modal.is_displayed())
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
         