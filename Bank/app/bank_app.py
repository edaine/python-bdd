from app.bank import Bank
from flask import Flask, render_template, request


app = Flask(__name__)

BANK = Bank()


@app.route('/')
def index():
    print("@app.route('/')")
    if None != request.args.get('account_number'):
        account_number = request.args.get('account_number')
        balance = BANK.get_account_balance(account_number)
        return render_template('index.html', balance=balance)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
