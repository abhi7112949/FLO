from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:17313"%("abhijeet", "abhijeetPassword"))
passphrse = rpc_connection.walletpassphrase("My name is Abhijeet" , 6000)

get_new_address = rpc_connection.getnewaddress()
#print(get_new_address)


# address = input("Enter the adrrees of receiver: ")
# amount = input("Enter the amount to spend: ")
# comment = input("Enter the comment for youself: ")
# sent = input("Whom the amount was sent to(name): ")
# txComment = input("Enter your comment: ")
#sent_to = rpc_connection.sendtoaddress(address, amount, comment,sent)

#sent_with = rpc_connection.sendtoaddress(address, amount, comment, sent, False, False, 1, 'UNSET', txComment)

flo_address = 'oLAegePoz2J44kpdPT3zNTrHR3bAaACAHb'
flo_message = 'Hello'
sign_message = rpc_connection.signmessage(flo_address,flo_message)
print(sign_message)
