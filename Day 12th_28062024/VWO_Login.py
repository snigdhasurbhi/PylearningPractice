#web automation-selenium
#open the browser
# we will automate the process of opening the browser and navigating to a web page
class VWOLogin_page:
    email:None
    password=None

    def __init__(self):
        self.email= "email"
        self.password="password"
        self.signin_button="id=signin"
        self.error_message="class=error-message"
        self.forgot_password_link="class=forgot-password-link"
        self.create_account_link="class=create-account-link"

        self.need_help_link="class=need-help-link"
        self.terms_of_use_link="class=terms-of-use-link"
        self.privacy_policy_link="class=privacy-policy-link"

        self.cookie_policy_link="class=cookie-policy-link"

    def login(self, email, password):
        print("Trying to login with " + email + " and " + password)
        #code to enter email and password
        if self.password == "password":
            print("Login successful")
        else:
            print("Not allowed to login")

        if self.email is not None:
            print(f"Finding email field and sending email {email}")
            #code to find the email field and send the email
        if self.password is not None:
            print(f"Finding password field and sending password {password}")
            #code to find the password field and send the password
        if self.signin_button is not None:
            print("Finding signin button and clicking it")
        if self.error_message is not None:
            print("Checking for error message")
            #code to check for error message
        if self.forgot_password_link is not None:
            print("Finding forgot password link and clicking it")
            #code to find forgot password link and click it
        if self.create_account_link is not None:
            print("Finding create account link and clicking it")
            #code to find create account link and click it
        if self.need_help_link is not None:
            print("Finding need help link and clicking it")



amit=VWOLogin_page()
amit.login("amait21@gmail.com", "password")

promod=VWOLogin_page()
promod.login("promode21@gmail.com", "ssword")
promod.login("XXXXXXXXXXXXXXXXXXX", "passrd")