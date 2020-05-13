from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

firefox_binary = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
driver = webdriver.Firefox(firefox_binary=firefox_binary, executable_path='C:\\ps\\geckodriver.exe')
extension_path = "C:\\ps\\canvasblocker.xpi"
driver.install_addon(extension_path, temporary=True)

driver.get('about:debugging#/runtime/this-firefox')

# wait for extensions to appear
wait = WebDriverWait(driver, 5)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'card')))

# internal uuid for extension pages
internal_uuid = driver.execute_script("""
  let extensions = Array.from(document.querySelectorAll('.card'));
  let canvasblocker = extensions.filter(el => el.querySelector('span').title == 'CanvasBlocker')[0];
  let metadata = Array.from(canvasblocker.querySelectorAll('.fieldpair__description')).map(e => e.innerText);
  return metadata[2];
""")

OPTIONS_PAGE = f'moz-extension://{internal_uuid}/options/options.html'

driver.get(OPTIONS_PAGE)

# import settings
driver.find_element_by_xpath('//button[text()="Load"]').send_keys('C:\\ps\\pluginsettings.json')

driver.quit() 