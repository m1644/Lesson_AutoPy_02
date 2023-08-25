import yaml
from Lecture_02.module import Site


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])

"""
def test_step1():
    x_selector1 = '''//*[@id="login"]/div[1]/label/input'''
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = '''//*[@id="login"]/div[2]/label/input'''
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = '''//*[@id="app"]/main/div/div/div[2]/h2'''
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "401"
"""

def test_step2():
    x_selector1 = '''//*[@id="login"]/div[1]/label/input'''
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("GB20230583da03")
    x_selector2 = '''//*[@id="login"]/div[2]/label/input'''
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("55aae3d70d")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector4 = '''//*[@id="app"]/main/nav/ul/li[3]/a'''
    ok_label = site.find_element("xpath", x_selector4)
    assert ok_label.text == "Hello, GB20230583da03"

# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))

# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath, "color"))

#test_step1()