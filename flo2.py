from flask import Flask, render_template, url_for, flash, redirect,jsonify,request
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from forms import GetAddressForm,GetPvtForm,SignForm,VerifyForm

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
    #pvt_key = rpc_connection.dumpprivkey(new_address)
    if form.validate_on_submit():
    #return(new_address)
        return render_template('home.html' , new_address = new_address ,form=form)
    return render_template('home.html' , new_address = new_address ,form=form)


@app.route("/pvt" , methods =['GET', 'POST'])
def private():
    form = GetPvtForm()
    addr = 'oLAegePoz2J44kpdPT3zNTrHR3bAaACAHb'
    #pvt_key=addr
    pvt_key=rpc_connection.dumpprivkey(addr)
    #return render_template('pvt.html' , pvt_key=pvt_key,form=form)

    if form.validate_on_submit():
        addr=form.address.data
        #form.address.data=addr
        pvt_key=rpc_connection.dumpprivkey(addr)
        # form.address = form.address.data
        #
        # #addr = form.address.data
        # pvt_key = rpc_connection.dumpprivkey(form.address)
    #return(new_address)
        return render_template('pvt.html', pvt_key=pvt_key,form=form)
    return render_template('pvt.html' , pvt_key=pvt_key,form=form)


@app.route("/sign" , methods =['GET','POST'])
def sign():
    form = SignForm()
    flo_address = 'oSbXr1v7MEkJVXnVM7ZZ2d6uvuodpS8uDV'
    flo_message = 'my message'
    sign_message = rpc_connection.signmessage(flo_address,flo_message)
    if form.validate_on_submit():
        flo_address = form.address.data
        flo_message = form.message.data
        sign_message = rpc_connection.signmessage(flo_address,flo_message)
    #return(new_address)
        return render_template('sign.html' , flo_address=flo_address,flo_message=flo_message,sign_message=sign_message,form=form)
    return render_template('sign.html' , flo_address=flo_address,flo_message=flo_message,sign_message=sign_message,form=form)


@app.route("/verify" , methods =['GET','POST'])
def verify():
    form = VerifyForm()
    flo_address = 'oSbXr1v7MEkJVXnVM7ZZ2d6uvuodpS8uDV'
    flo_message = 'my message'
    flo_signature = 'IOi8XCB3sZGCMR4Ti0T7I8B3ifHGH+ifciY+otDQ8zaQHbjJ/GBjA3ORjRnPPI3T+OHOeEXvJGBhKM+m3OEVfCs='
    verify_message = rpc_connection.verifymessage(flo_address,flo_signature,flo_message)
    if form.validate_on_submit():
        # if verify_message == True:
        #     flash(f'The message- {form.message.data}is verified!','success')
        # else:
        #     flash(f'The message- {form.message.data}is not verified!','success')
        flo_address = form.address.data
        flo_message = form.message.data
        flo_signature = form.signature.data
        verify_message = rpc_connection.verifymessage(flo_address,flo_signature,flo_message)
        if verify_message == True:
            flash(f' "{form.message.data}" verified!','success')
        else:
            flash(f' "{form.message.data}" - Verification Failed!','warning')

    #return(new_address)
        return render_template('verify.html' , flo_address=flo_address,flo_signature=flo_signature,flo_message=flo_message,verify_message=verify_message,form=form)
    return render_template('verify.html' , flo_address=flo_address,flo_signature=flo_signature,flo_message=flo_message,verify_message=verify_message,form=form)



if __name__ == '__main__':
    app.run(debug=True)
