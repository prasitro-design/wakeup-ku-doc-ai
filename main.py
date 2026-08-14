import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def wake_up_streamlit(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        print(f"กำลังเปิดหน้าเว็บ: {url}")
        driver.get(url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(10)  # รอให้ระบบเชื่อมต่อ WebSocket สมบูรณ์
        print("ปลุกแอป Streamlit สำเร็จ!")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    STREAMLIT_URL = "https://estad-ku-doc-ai.streamlit.app"  # เปลี่ยนเป็น URL ของคุณ
    wake_up_streamlit(STREAMLIT_URL)