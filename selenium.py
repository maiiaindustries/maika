from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def get_upcoming_events(url):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = "C:\Google Drive\scripts\python3\python_other\selenium_from_Sviridov\chromedriver.exe"
    driver = webdriver.Chrome(
        chrome_options=chrome_options, executable_path=chrome_driver)

    driver.implicitly_wait(10)
    driver.get(url)

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.send_keys("")
    password.send_keys("")

    login = driver.find_element_by_tag_name("button")
    login.click()

    time.sleep(5)
    result = driver.find_elements_by_class_name("graph-legend-series")[1]
    result_txt = result.text
    print(result_txt)
    quota = result_txt.replace("quota_gb ", "")
    #quota = result_txt.replace("RAM quota ", "")

    driver.close()
    return(quota)


res = get_upcoming_events("https://dashboard.netcracker.com/d/DS70Rb7mz/cloud-iaas_cloud_project_space?refresh=1m&panelId=1&fullscreen&orgId=1&var-Cloud=cloud01&var-Tenant=TELU_IM_SOW55WO14&var-Vm=All&var-instance=All&var-host=All&var-disk=vda&var-disk=vdb&var-insthost=All&var-lower_tenant=telu_im_sow55wo14")
print(res)
