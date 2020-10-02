class SignInData:
    def __init__(self, LoginId, Password, Name):
        self.LoginId = LoginId
        self.Password = Password
        self.Name = Name
class LoginData:
    def __init__(self, LoginId, Password):
        self.LoginId = LoginId
        self.Password = Password
class BudgetData:
    def __init__(self, LoginId, BudgetName, BudgetId, Currency):
        self.LoginId = LoginId
        self.BudgetName = BudgetName
        self.BudgetId = BudgetId
        self.Currency = Currency
        