import csv
from csv import DictWriter, DictReader
from flask import Flask, render_template, make_response,render_template
from flask import redirect, request, jsonify, url_for
from Objects import SignInData, LoginData, BudgetData

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route('/signIn', methods=['GET'])
def signInJS():
    jsdata = request.args.get['canvas_data']
    data = loginIn(jsdata)
    return data

#@app.route('/signIn', methods=['POST'])
def signIn(data=SignInData):
    with open('./login.csv', 'a') as file:
        header = ('LoginId', 'Password', 'Name')
        csv_writer = DictWriter(file, fieldnames=header, lineterminator='\n')
        # csv_writer.writeheader()
        csv_writer.writerow({
            'LoginId': data.LoginId,
            'Password': data.Password,
            'Name': data.Name
        })
    return True


@app.route('/loginIn', methods=['POST'])
def loginIn(data=LoginData):
    with open('./login.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['LoginId'] == data.LoginId and row['Password'] == data.Password):
                message = 'Succesfully logged In......'
            else:
                message = 'LoginId and Password does not match....'
    return message

@app.route('/budgetName', methods=['POST'])
def newBudget(data=BudgetData):
    with open('./Budget.csv', 'a') as file:
        header = ('LoginId', 'BudgetName', 'BudgetId', 'Currency')

        csv_writer = DictWriter(file, fieldnames=header, lineterminator='\n')
        # csv_writer.writeheader()
        csv_writer.writerow({
            'LoginId': data.LoginId,
            'BudgetName': data.BudgetName,
            'BudgetId': data.BudgetId,
            'Currency': data.Currency
        })
    return True


data = signIn(SignInData("adhcvufd", "adhcvufd", "adfdfhcvu"))
dfd = loginIn(LoginData("adhcvufd", "adhcvuf"))
print(data)
print(dfd)

if __name__ == "__main__":
    app.run()
