class DemoUserClass:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def greet(self):
        return f'Hello, {self.username}'

demo_user = DemoUserClass('Inferato', 'test@email.com')   
another_user = DemoUserClass('test_user', 'other@test.com')
breakpoint()
