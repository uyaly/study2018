# encoding:utf-8
def setup(self):
    self.driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities={'latform': 'WINDOWS',
                              'browserName': 'firefox', 'version': '',
                              'javascriptEnabled': True}
    )
    self.driver.implicitly_wait(30)
    self.vase_url = "http://thewebsite.org/"
    self.verificationError = []
    self.accept_next_alert = True
