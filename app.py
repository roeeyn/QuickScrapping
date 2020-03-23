# import re
# import time
# from selenium import webdriver
# # 11 Cafes
# driver = webdriver.Chrome('./chromedriver')
# driver.get('https://mxcity.mx/2019/12/10-cafes-ideales-para-conocer-en-diciembre/')
# out_container = driver.find_elements_by_class_name('content_post')[0]
# container = out_container.find_element_by_tag_name("div")
# titles = [title.text for title in container.find_elements_by_tag_name("h2") if title.text != "" and title.text != " "]
# addresses = [address.text for address in container.find_elements_by_tag_name("p") if re.search("^Dónde:.*", address.text)]
# schedules = [schedule.text for schedule in container.find_elements_by_tag_name("p") if re.search("^Cuándo:.*", schedule.text)]
# costs = [cost.text for cost in container.find_elements_by_tag_name("p") if re.search("^Cuánto:.*", cost.text)]
# main_tuple_list = zip(titles[1:], addresses, schedules, costs)
# main_list = [{
#     "name": rest_tuple[0],
#     "address": rest_tuple[1],
#     "schedule": rest_tuple[2],
#     "cost": rest_tuple[3]
# } for rest_tuple in main_tuple_list]
# print(main_list)
# driver.quit()

import base64
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://bibliotechnia.com.mx/portal/visor/web/visor.php")
driver.add_cookie(
    {
        "name": "PHPSESSID",
        "value": "jedt8uf304oon3kufo2kdip123",
        "domain": "bibliotechnia.com.mx",
    }
)

# canvas = driver.find_element_by_css_selector("#canvas")
#
# # get the canvas as a PNG base64 string
# canvas_base64 = driver.execute_script(
#     "return arguments[0].toDataURL('image/png').substring(21);", canvas
# )
#
# # decode
# canvas_png = base64.b64decode(canvas_base64)
#
# # save to a file
# with open(r"canvas.png", "wb") as f:
#     f.write(canvas_png)
