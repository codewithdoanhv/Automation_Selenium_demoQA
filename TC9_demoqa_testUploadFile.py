import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import messagebox
import os

class TestUploadFile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/upload-download")
        self.wait = WebDriverWait(self.driver, 15)

    def test_upload_file(self):
        try:
            file_input = self.wait.until(EC.presence_of_element_located((By.ID, "uploadFile")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", file_input)
            time.sleep(1)
            file_path = os.path.abspath("test.txt")
            with open(file_path, "w") as f:
                f.write("Test file")
            file_input.send_keys(file_path)
            output = self.wait.until(EC.presence_of_element_located((By.ID, "uploadedFilePath")))
            self.assertTrue(output.is_displayed())
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
