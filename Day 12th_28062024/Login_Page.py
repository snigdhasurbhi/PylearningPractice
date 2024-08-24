#web automation-selenium
#open the browser
# we will automate the process of opening the browser and navigating to a web page
class VWOLogin_page:
    email:None
    password=None

    def __init__(self,driver):
        self.driver=driver
        self.email="id=email"
        self.password="id=password"
        self.signin_button="id=signin"
        self.error_message="class=error-message"
        self.forgot_password_link="class=forgot-password-link"
        self.create_account_link="class=create-account-link"

        self.need_help_link="class=need-help-link"
        self.terms_of_use_link="class=terms-of-use-link"
        self.privacy_policy_link="class=privacy-policy-link"

        self.cookie_policy_link="class=cookie-policy-link"
    def enter_email(self,email):
        self.driver.find_element_by_id(self.email).send_keys(email)
        #find_element_by_id is used to find the element by id
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password).send_keys(password)
        #find_element_by_id is used to find the element by id
    def click_signin_button(self):
        self.driver.find_element_by_id(self.signin_button).click()
        #find_element_by_id is used to find the element by id
    def get_error_message(self):
        return self.driver.find_element_by_class_name(self.error_message).text
        #find_element_by_class_name is used to find the element by class name
    def click_forgot_password_link(self):
        self.driver.find_element_by_class_name(self.forgot_password_link).click()
        #find_element_by_class_name is used to find the element by class name
    def click_create_account_link(self):
        self.driver.find_element_by_class_name(self.create_account_link).click()
        #find_element_by_class_name is used to find the element by class name
    def click_need_help_link(self):
        self.driver.find_element_by_class_name(self.need_help_link).click()
        #find_element_by_class_name is used to find the element by class name
    def click_terms_of_use_link(self):
        self.driver.find_element_by_class_name(self.terms_of_use_link).click()
        #find_element_by_class_name is used to find the element by class name
    def click_privacy_policy_link(self):
        self.driver.find_element_by_class_name(self.privacy_policy_link).click()
        #find_element_by_class_name is used to find the element by class name
    def click_cookie_policy_link(self):
        self.driver.find_element_by_class_name(self.cookie_policy_link).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin_button()

amit=VWOLogin_page()
amit.login("amait21@gmail.com", "password")

promod=VWOLogin_page()
promod.login("promode21@gmail.com", "password")


