import yaml
from module import Site


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step_1_bad_login():
    site = Site(testdata["address"])
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
    site.close()


def test_step_2_good_login():
    site = Site(testdata["address"])
    x_selector1 = '''//*[@id="login"]/div[1]/label/input'''
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("Ivan1234")
    x_selector2 = '''//*[@id="login"]/div[2]/label/input'''
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("416b69ce0b")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = '''//*[@id="app"]/main/nav/ul/li[3]/a'''
    ok_label = site.find_element("xpath", x_selector3)
    assert ok_label.text == "Hello, Ivan1234"
    site.close()


if __name__ == "__main__":
    test_step_1_bad_login()
    test_step_2_good_login()
