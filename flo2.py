from flask import Flask, render_template, url_for, flash, redirect,jsonify,request
from bitcoinrpc.bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from forms import GetAddressForm

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:17313"%("abhijeet", "abhijeetPassword"))
passphrse = rpc_connection.walletpassphrase("My name is Abhijeet" , 60000)

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/" , methods =['GET' , 'POST'])
@app.route("/home" , methods =[ 'POST'])
def home():
    form = GetAddressForm()
    new_address = rpc_connection.getnewaddress()
    pvt_key = rpc_connection.dumpprivkey(new_address)
    if form.validate_on_submit():
    #return(new_address)
        return render_template('home.html' , new_address = new_address , pvt_key=pvt_key,form=form)
    return render_template('home.html' , new_address = new_address , pvt_key=pvt_key,form=form)

if __name__ == '__main__':
    app.run(debug=True)
