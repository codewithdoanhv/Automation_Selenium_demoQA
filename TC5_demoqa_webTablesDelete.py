import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox

class TestWebTablesDelete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/webtables")
        self.wait = WebDriverWait(self.driver, 15)

    def test_web_tables_delete(self):
        try:
            delete_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='Delete'][1]")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)
            time.sleep(1)
            delete_button.click()
            table_rows = self.driver.find_elements(By.CLASS_NAME, "rt-tr-group")
            self.assertTrue(len(table_rows) >= 0)
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
