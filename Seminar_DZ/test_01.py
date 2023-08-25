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


def test_step_3_new_post():
    site = Site(testdata["address"])
    x_selector1 = '''//*[@id="login"]/div[1]/label/input'''
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("Ivan1234")
    x_selector2 = '''//*[@id="login"]/div[2]/label/input'''
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("416b69ce0b")
    btn_selector1 = "button"
    btn1 = site.find_element("css", btn_selector1)
    btn1.click()
    btn_selector2 = "#create-btn"
    btn2 = site.find_element("css", btn_selector2)
    btn2.click()
    x_selector3 = '''//*[@id="create-item"]/div/div/div[1]/div/label/input'''
    input3 = site.find_element("xpath", x_selector3)
    input3.send_keys("Test")
    x_selector4 = '''//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'''
    input4 = site.find_element("xpath", x_selector4)
    input4.send_keys("Test")
    x_selector5 = '''//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'''
    input5 = site.find_element("xpath", x_selector5)
    input5.send_keys("Test")
    x_selector6 = '''//*[@id="create-item"]/div/div/div[5]/div/div/label/input'''
    input6 = site.find_element("xpath", x_selector6)
    input6.send_keys("25.08.2023")
    
    Imagepath = """D:\\OneDrive\\Рабочий стол/1234.jpg"""
    x_selector7 = '''//*[@id="create-item"]/div/div/div[6]/div/div/label/input'''
    input7 = site.find_element("xpath", x_selector7)
    input7.send_keys(Imagepath)
    
    btn_selector3 = "div:nth-child(7) > div > button"
    btn3 = site.find_element("css", btn_selector3)
    btn3.click()
    x_selector = '''//*[@id="app"]/main/div/div[1]/div/div[3]'''
    ok_label = site.find_element("xpath", x_selector)
    assert ok_label.text == "Test"
    site.close()


if __name__ == "__main__":
    test_step_1_bad_login()
    test_step_2_good_login()
    test_step_3_new_post()
