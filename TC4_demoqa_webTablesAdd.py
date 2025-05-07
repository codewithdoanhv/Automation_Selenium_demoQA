import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox

class TestWebTablesAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/webtables")
        self.wait = WebDriverWait(self.driver, 15)

    def test_web_tables_add(self):
        try:
            add_button = self.wait.until(EC.presence_of_element_located((By.ID, "addNewRecordButton")))
            add_button.click()
            time.sleep(1)
            first_name = self.wait.until(EC.presence_of_element_located((By.ID, "firstName")))
            first_name.send_keys("Doan")
            time.sleep(1)
            self.driver.find_element(By.ID, "lastName").send_keys("Automation")
            time.sleep(1)
            self.driver.find_element(By.ID, "userEmail").send_keys("doan.automation@example.com")
            time.sleep(1)
            self.driver.find_element(By.ID, "age").send_keys("29")
            time.sleep(1)
            self.driver.find_element(By.ID, "salary").send_keys("50000")
            time.sleep(1)
            self.driver.find_element(By.ID, "department").send_keys("IT")
            time.sleep(1)
            submit_button = self.driver.find_element(By.ID, "submit")            
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(1)
            submit_button.click()
            time.sleep(1)
            table_row = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Doan')]")))
            self.assertTrue(table_row.is_displayed())
            time.sleep(2)
            
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Ket qua", "Test Passed")
            root.destroy()

        except Exception as e:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Ket qua", f"Test Failed\nLoi: {str(e)}")
            root.destroy()
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()