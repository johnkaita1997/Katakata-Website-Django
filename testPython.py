# import os
# from datetime import datetime
# #
# # import firebase_admin
# # import pyrebase
# # from firebase_admin import credentials
# # from firebase_admin import db
#
# #  ! [remote rejected] master -> master (pre-receive hook declined)
# # heroku version
# # heroku login
# # ls
# # git init
# # git add . (space period)
# # git commit -m "first commit"
# #
# # heroku create
# # heroku git:remote -a dry-fortress-56183
# # pip install gunicorn
# # gunicorn kaita.wsgi
# #
# #
# # pip install gunicorn
# # pip install django-heroku
# # pip install dj_database_url
# # pip install python-decouple
# # pip freeze
# # pip freeze > requirements.txt
# #
# # 1YygyjIO
# # on.ubabukoh@gmail.com
# # tmLrZ#54opLklSGJ
# #
# # git push heroku master
#
# # url = static('files/kaita.json')
# data = os.path.abspath(os.path.dirname(__file__)) + f"/main/kaita.json"
# cred = credentials.Certificate(data)
# dbs = firebase_admin.db
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'https://project-home-17291-default-rtdb.firebaseio.com/',
#     'databaseURL': 'https://project-home-17291-default-rtdb.firebaseio.com'
# })
#
# config = {
#     'apiKey': "AIzaSyCk5Tj7c6RK69XW8UU9umgKM7lIq922YJg",
#     'authDomain': "project-home-17291.firebaseapp.com",
#     'databaseURL': "https://project-home-17291-default-rtdb.firebaseio.com",
#     'projectId': "project-home-17291",
#     'storageBucket': "project-home-17291.appspot.com",
#     'messagingSenderId': "411125582224",
#     'appId': "1:411125582224:web:5c18e229fa268ef678cb15",
#     'measurementId': "${config.measurementId}"
# }
#
# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
# auth = firebase.auth()
#
#
# def totalEggsCollectedThisMonth():
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('eggrecords').order_by_child("my").equal_to(currentMY()).get()
#     result = snapshot.values()
#     total = 0
#     for value in result:
#         if "collected" in value.keys():
#             print("There")
#             total += int(value['collected'])
#     return total
#
#
# def totalSalesForThisMonth():
#     ref = dbs.reference("poultry").child("sales").order_by_child("my").equal_to(currentMY()).get()
#     total = 0
#     for value in ref.values():
#         amount = float(value['soldat'])
#         total += amount
#     return round(total, 2)
#
#
# def totalExpensesForThisMonth():
#     print(f"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj {currentMY()}")
#     ref = dbs.reference("poultry")
#     snapshot = ref.child("expenses").order_by_child("my").equal_to(currentMY()).get()
#     total = 0
#     for value in snapshot.values():
#         amount = float(value['amount'])
#         total += amount
#     return total
#
#
# def totalSalesForSpecificMonth():
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('sales').order_by_child('my').equal_to("Dec-2021").get()
#     total = 0
#     for value in snapshot.values():
#         amount = float(value['soldat'])
#         total += amount
#
#
# def historyForSpecificClient():
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('clienthistory').child('Brian Kaita').get()
#     for value in snapshot.values():
#         newdict = value
#         for i in newdict:
#             pass
#
#
# def expensesForSpecificDate():
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('expenses').child('Brian Kaita').get()
#     for value in snapshot.values():
#         newdict = value
#         for i in newdict:
#             pass
#
#
# def alleggs():
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('eggrecords').order_by_child('timestamp').limit_to_last(1000).get()
#     result = snapshot.values()
#     bigdict = {}
#     for value in result:
#         smalldict = {}
#         smalldict['completelybroken'] = value['completelybroken']
#         smalldict['crates'] = value['crates']
#         smalldict['incompletelybroken'] = value['incompletelybroken']
#         smalldict['premature'] = value['premature']
#         smalldict['singleextra'] = value['singleextra']
#         smalldict['date'] = convertDateToBrianType(value['date'])
#         smalldict['small'] = value['small']
#         smalldict['time'] = value['time']
#         smalldict['signleextra'] = value['singleextra']
#         smalldict['collected'] = "N|A"
#         if "collected" in value.keys():
#             smalldict['collected'] = value['collected']
#         bigdict[value['timestamp']] = smalldict
#     return bigdict
#
#
# def allsales():
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('sales').order_by_child('timestamp').limit_to_last(1000).get()
#     result = snapshot.values()
#     bigdict = {}
#     for value in result:
#         smalldict = {}
#         smalldict['date'] = convertDateToBrianType(value['date'])
#         smalldict['extraeggs'] = value['extraeggs']
#         smalldict['fullcrates'] = value['fullcrates']
#         smalldict['fulluser'] = value['fulluser']
#         smalldict['soldat'] = value['soldat']
#         smalldict['transaction'] = value['transaction']
#         smalldict['priceperegg'] = "N|A"
#         if "priceperegg" in value.keys():
#             smalldict['priceperegg'] = round(float(value['priceperegg']), 2)
#         smalldict['description'] = "N|A"
#         if "description" in value.keys():
#             smalldict['description'] = value['description']
#         smalldict['crateprice'] = "N|A"
#         if "crateprice" in value.keys():
#             smalldict['crateprice'] = value['crateprice']
#         smalldict['extraeggs'] = value['extraeggs']
#         smalldict['my'] = value['my']
#         smalldict['collected'] = "N|A"
#         if "collected" in value.keys():
#             smalldict['collected'] = value['collected']
#         bigdict[value['timestamp']] = smalldict
#         if "additions" in value.keys():
#             smalldict['additions'] = value['additions']
#         bigdict[value['timestamp']] = smalldict
#     return bigdict
#
#
# def allexpenses():
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('expenses').order_by_child('timestamp').limit_to_last(1000).get()
#     result = snapshot.values()
#     bigdict = {}
#     for value in result:
#         smalldict = {}
#         smalldict['suppliername'] = "N|A"
#         if "suppliername" in value.keys():
#             smalldict['supplier'] = value['suppliername']
#         smalldict['description'] = "N|A"
#         if "description" in value.keys():
#             smalldict['description'] = value['description']
#         smalldict['layer'] = "N|A"
#         if "layer" in value.keys():
#             smalldict['layer'] = value['layer']
#         smalldict['unit'] = "N|A"
#         if "unit" in value.keys():
#             smalldict['unit'] = value['unit']
#         smalldict['quantity'] = "N|A"
#         if "quantity" in value.keys():
#             smalldict['quantity'] = value['quantity']
#         smalldict['amountperunit'] = "N|A"
#         if "amountperunit" in value.keys():
#             smalldict['amountperunit'] = value['amountperunit']
#         smalldict['date'] = convertDateToBrianType(value['date'])
#         smalldict['amount'] = value['amount']
#         smalldict['expensetype'] = value['expensetype']
#         smalldict['transaction'] = value['transaction']
#         smalldict['my'] = value['my']
#         bigdict[value['timestamp']] = smalldict
#     return bigdict
#
#
# def allCustomerNames():
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('clientnames').get()
#     result = snapshot.values()
#     for value in result:
#         name = value['name']
#     return result
#
#
# def historyForSpecificClient(startdate, enddate, clientName):
#     ref = dbs.reference('poultry').child('clienthistory').child(clientName)
#     snapshot = ref.order_by_child('timestamp').limit_to_last(1000).get()
#     result = snapshot.values()
#     bigger_dict = {}
#     for value in result:
#         if 'date' in value.keys():
#             databaseDate = value['date']
#             correnctedDbDate: str = datetime.strptime(databaseDate, '%d-%b-%Y').strftime('%Y-%m-%d')
#             print(startdate, enddate, correnctedDbDate)
#             if startdate <= correnctedDbDate <= enddate:
#                 dict = {}
#                 dict['collected'] = "N|A"
#                 # Random Comment
#                 if "collected" in value.keys():
#                     dict['collected'] = value['collected']
#                 dict['crateprice'] = "N|A"
#                 if "crateprice" in value.keys():
#                     dict['crateprice'] = value['crateprice']
#                 dict['fullcrates'] = "N|A"
#                 if "fullcrates" in value.keys():
#                     dict['fullcrates'] = value['fullcrates']
#                 dict['date'] = "N|A"
#                 if "date" in value.keys():
#                     dict['date'] = convertDateToBrianType(value['date'])
#                 dict['extraeggs'] = "N|A"
#                 if "extraeggs" in value.keys():
#                     dict['extraeggs'] = value['extraeggs']
#                 dict['fulluser'] = "N|A"
#                 if "fulluser" in value.keys():
#                     dict['fulluser'] = value['fulluser']
#                 dict['my'] = "N|A"
#                 if "my" in value.keys():
#                     dict['my'] = value['my']
#                 dict['priceperegg'] = "N|A"
#                 if "priceperegg" in value.keys():
#                     dict['priceperegg'] = round(float(value['priceperegg']), 2)
#                 dict['soldat'] = "N|A"
#                 if "soldat" in value.keys():
#                     dict['soldat'] = value['soldat']
#                 timestamp = value['timestamp']
#                 dict['returnedamount'] = "N|A"
#                 if "returned" in value.keys():
#                     dict['returnedamount'] = value['returned']
#                 dict['returnedtransaction'] = "N|A"
#                 if "transaction" in value.keys():
#                     dict['returnedtransaction'] = value['transaction']
#                 bigger_dict[timestamp] = dict
#     return bigger_dict
#
#
# def summationSales(date, searchTerm):
#     full = {}
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('sales').order_by_child(searchTerm).equal_to(date).get()
#     total = 0
#     crates = 0
#     collected = 0
#     for value in snapshot.values():
#         amount = float(value['soldat'])
#         crater = float(value['fullcrates'])
#         if 'collected' in value.keys():
#             colle = float(value['collected'])
#             collected += colle
#         total += amount
#         crates += crater
#     full['collected'] = collected
#     full['crates'] = crates
#     full['totalamount'] = total
#     return full
#
#
# def summationEggsCollected(date, searchTerm):
#     full = {}
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('eggrecords').order_by_child(searchTerm).equal_to(date).get()
#     crates = 0
#     collected = 0
#     completelybroken = 0
#     incompletelybroken = 0
#     premature = 0
#     small = 0
#     for value in snapshot.values():
#         completelyd = float(value['completelybroken'])
#         nocompletelyd = float(value['incompletelybroken'])
#         prematureddd = float(value['premature'])
#         craterd = float(value['crates'])
#         smalld = float(value['small'])
#         if 'collected' in value.keys():
#             colle = float(value['collected'])
#             collected += colle
#         crates += craterd
#         completelybroken += completelyd
#         incompletelybroken += nocompletelyd
#         completelybroken += completelyd
#         premature += prematureddd
#         small += smalld
#     full['collected'] = collected
#     full['crates'] = crates
#     full['completelybroken'] = completelybroken
#     full['incompletelybroken'] = incompletelybroken
#     full['premature'] = premature
#     full['small'] = small
#     return full
#
#
# def summationExpenses(date, searchTerm):
#     full = {}
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('expenses').order_by_child(searchTerm).equal_to(date).get()
#     amount = 0
#     for value in snapshot.values():
#         amount += float(value['amount'])
#         full['amount'] = amount
#     full['amount'] = amount
#     return full
#
#
# def summationExpenses_Farm(date, searchTerm):
#     full = {}
#     ref = dbs.reference('farm')
#     snapshot = ref.child('expenses').order_by_child(searchTerm).equal_to(date).get()
#     amount = 0
#     for value in snapshot.values():
#         amount += float(value['amount'])
#         full['amount'] = amount
#     full['amount'] = amount
#     return full
#
#
# def convertDateToBrianType(originalDate):
#     chosenDate = datetime.strptime(originalDate, '%d-%b-%Y').strftime('%d/%m/%Y')
#     return str(chosenDate)
#
#
# def allclients():
#     ref = db.child("poultry").child("clientnames").get()
#     return len(ref.pyres)
#
#
# def summationSales_DateQuery(startdate, enddate):
#     order = []
#     full = {}
#     bigdict = {}
#     ref = dbs.reference('poultry').child('sales').order_by_child('timestamp').limit_to_last(1000).get()
#     snapshot = ref
#     total = 0
#     crates = 0
#     collected = 0
#     for value in snapshot.values():
#         if 'date' in value.keys():
#             databaseDate = value['date']
#             correnctedDbDate: str = datetime.strptime(databaseDate, '%d-%b-%Y').strftime('%Y-%m-%d')
#             print(startdate, enddate, correnctedDbDate)
#             if startdate <= correnctedDbDate <= enddate:
#                 amount = float(value['soldat'])
#                 crater = float(value['fullcrates'])
#                 if 'collected' in value.keys():
#                     colle = float(value['collected'])
#                     collected += colle
#                 total += amount
#                 crates += crater
#                 full['collected'] = collected
#                 full['crates'] = crates
#                 full['totalamount'] = total
#
#                 smalldict = {}
#                 smalldict['date'] = convertDateToBrianType(value['date'])
#                 smalldict['extraeggs'] = value['extraeggs']
#                 smalldict['fullcrates'] = value['fullcrates']
#                 smalldict['fulluser'] = value['fulluser']
#                 smalldict['soldat'] = value['soldat']
#                 smalldict['transaction'] = value['transaction']
#                 smalldict['priceperegg'] = "N|A"
#                 if "priceperegg" in value.keys():
#                     smalldict['priceperegg'] = round(float(value['priceperegg']), 2)
#                 smalldict['description'] = "N|A"
#                 if "description" in value.keys():
#                     smalldict['description'] = value['description']
#                 smalldict['crateprice'] = "N|A"
#                 if "crateprice" in value.keys():
#                     smalldict['crateprice'] = value['crateprice']
#                 smalldict['extraeggs'] = value['extraeggs']
#                 smalldict['my'] = value['my']
#                 smalldict['collected'] = "N|A"
#                 if "collected" in value.keys():
#                     smalldict['collected'] = value['collected']
#                 bigdict[value['timestamp']] = smalldict
#
#     order.append(full)
#     order.append(bigdict)
#     return order
#
#
# def summationExpenses_DateSummary(startdate, enddate):
#     full = {}
#     order = []
#     bigdict = {}
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('expenses').order_by_child('timestamp').limit_to_last(10000).get()
#     amount = 0
#     for value in snapshot.values():
#         if 'date' in value.keys():
#             databaseDate = value['date']
#             correnctedDbDate: str = datetime.strptime(databaseDate, '%d-%b-%Y').strftime('%Y-%m-%d')
#             print(startdate, enddate, correnctedDbDate)
#             if startdate <= correnctedDbDate <= enddate:
#                 amount += float(value['amount'])
#                 full['amount'] = amount
#                 smalldict = {}
#                 smalldict['supplier'] = "N|A"
#                 if "supplier" in value.keys():
#                     smalldict['supplier'] = value['supplier']
#                 smalldict['description'] = "N|A"
#                 if "description" in value.keys():
#                     smalldict['description'] = value['description']
#                 smalldict['layer'] = "N|A"
#                 if "layer" in value.keys():
#                     smalldict['layer'] = value['layer']
#                 smalldict['description'] = "N|A"
#                 if "description" in value.keys():
#                     smalldict['description'] = value['description']
#                 smalldict['unit'] = "N|A"
#                 if "unit" in value.keys():
#                     smalldict['unit'] = value['unit']
#                 smalldict['quantity'] = "N|A"
#                 if "quantity" in value.keys():
#                     smalldict['quantity'] = value['quantity']
#                 smalldict['amountperunit'] = "N|A"
#                 if "amountperunit" in value.keys():
#                     smalldict['amountperunit'] = value['amountperunit']
#                 smalldict['date'] = convertDateToBrianType(value['date'])
#                 smalldict['amount'] = value['amount']
#                 smalldict['expensetype'] = value['expensetype']
#                 smalldict['transaction'] = value['transaction']
#                 smalldict['my'] = value['my']
#                 bigdict[value['timestamp']] = smalldict
#
#     order.append(full)
#     order.append(bigdict)
#     return order
#
#
# def summationExpenses_DateSummary_Farm(startdate, enddate):
#     full = {}
#     order = []
#     bigdict = {}
#     ref = dbs.reference('farm')
#     snapshot = ref.child('expenses').order_by_child('timestamp').limit_to_last(10000).get()
#     amount = 0
#     for value in snapshot.values():
#         if 'date' in value.keys():
#             databaseDate = value['date']
#             correnctedDbDate: str = datetime.strptime(databaseDate, '%d-%b-%Y').strftime('%Y-%m-%d')
#             print(startdate, enddate, correnctedDbDate)
#             if startdate <= correnctedDbDate <= enddate:
#                 amount += float(value['amount'])
#                 full['amount'] = amount
#                 smalldict = {}
#                 smalldict['supplier'] = "N|A"
#                 if "supplier" in value.keys():
#                     smalldict['supplier'] = value['supplier']
#                 smalldict['description'] = "N|A"
#                 if "description" in value.keys():
#                     smalldict['description'] = value['description']
#                 smalldict['layer'] = "N|A"
#                 if "layer" in value.keys():
#                     smalldict['layer'] = value['layer']
#                 smalldict['description'] = "N|A"
#                 if "description" in value.keys():
#                     smalldict['description'] = value['description']
#                 smalldict['unit'] = "N|A"
#                 if "unit" in value.keys():
#                     smalldict['unit'] = value['unit']
#                 smalldict['quantity'] = "N|A"
#                 if "quantity" in value.keys():
#                     smalldict['quantity'] = value['quantity']
#                 smalldict['amountperunit'] = "N|A"
#                 if "amountperunit" in value.keys():
#                     smalldict['amountperunit'] = value['amountperunit']
#                 smalldict['date'] = convertDateToBrianType(value['date'])
#                 smalldict['amount'] = value['amount']
#                 smalldict['expensetype'] = value['expensetype']
#                 smalldict['transaction'] = value['transaction']
#                 smalldict['my'] = value['my']
#                 bigdict[value['timestamp']] = smalldict
#
#     order.append(full)
#     order.append(bigdict)
#     return order
#
#
# def summationEggsCollected_DateQueryRange(startdate, enddate):
#     full = {}
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('eggrecords').order_by_child('timestamp').limit_to_last(100000).get()
#     crates = 0
#     collected = 0
#     bigdict = {}
#     order = []
#     completelybroken = 0
#     incompletelybroken = 0
#     premature = 0
#     small = 0
#     for value in snapshot.values():
#         if 'date' in value.keys():
#             databaseDate = value['date']
#             correnctedDbDate: str = datetime.strptime(databaseDate, '%d-%b-%Y').strftime('%Y-%m-%d')
#             print(startdate, enddate, correnctedDbDate)
#             if startdate <= correnctedDbDate <= enddate:
#                 completelyd = float(value['completelybroken'])
#                 nocompletelyd = float(value['incompletelybroken'])
#                 prematureddd = float(value['premature'])
#                 craterd = float(value['crates'])
#                 smalld = float(value['small'])
#                 if 'collected' in value.keys():
#                     colle = float(value['collected'])
#                     collected += colle
#                 crates += craterd
#                 completelybroken += completelyd
#                 incompletelybroken += nocompletelyd
#                 completelybroken += completelyd
#                 premature += prematureddd
#                 small += smalld
#                 full['collected'] = collected
#                 full['crates'] = crates
#                 full['completelybroken'] = completelybroken
#                 full['incompletelybroken'] = incompletelybroken
#                 full['premature'] = premature
#                 full['small'] = small
#
#                 smalldict = {}
#                 smalldict['completelybroken'] = value['completelybroken']
#                 smalldict['crates'] = value['crates']
#                 smalldict['incompletelybroken'] = value['incompletelybroken']
#                 smalldict['premature'] = value['premature']
#                 smalldict['singleextra'] = value['singleextra']
#                 smalldict['date'] = convertDateToBrianType(value['date'])
#                 smalldict['small'] = value['small']
#                 smalldict['time'] = value['time']
#                 smalldict['signleextra'] = value['singleextra']
#                 smalldict['collected'] = "N|A"
#                 if "collected" in value.keys():
#                     smalldict['collected'] = value['collected']
#                 bigdict[value['timestamp']] = smalldict
#
#     order.append(full)
#     order.append(bigdict)
#     return order
#
#
# def allsummary(startdate, enddate):
#     ref = dbs.reference('poultry')
#     snapshot = ref.child('summary').get()
#     result = snapshot.values()
#     bigdict = {}
#     full = []
#
#     firstdict = {}
#     firstdict['date'] = "12/22/2021"
#     firstdict['name'] = "Balance B/F"
#     firstdict['state'] = "N|A"
#     firstdict['debit'] = "N|A"
#     firstdict['credit'] = "N|A"
#     firstdict['balance'] = "N|A"
#     bigdict['9999999999999'] = firstdict
#
#     totcredit = 0
#     totdebit = 0
#
#     for value in result:
#         if 'date' in value.keys():
#             databaseDate = value['date']
#             correnctedDbDate: str = datetime.strptime(databaseDate, '%d-%b-%Y').strftime('%Y-%m-%d')
#             print(startdate, enddate, correnctedDbDate)
#             if startdate <= correnctedDbDate <= enddate:
#                 smalldict = {}
#                 smalldict['state'] = "N|A"
#                 smalldict['credit'] = "N|A"
#                 smalldict['debit'] = "N|A"
#
#                 state = ''
#                 credit = ''
#                 debit = ''
#
#                 if "state" in value.keys():
#                     smalldict['state'] = value['state']
#                     state = value['state']
#                 smalldict['operation'] = "N|A"
#                 if "operation" in value.keys():
#                     operation = value['operation']
#                     if operation == "Credit":
#                         smalldict['credit'] = value['amount']
#                         credit = value['amount']
#                         totcredit += float(value['amount'])
#                     elif operation == "Debit":
#                         smalldict['debit'] = value['amount']
#                         debit = value['amount']
#                         totdebit += float(value['amount'])
#
#                 firstdict['date'] = "12/22/2021"
#                 firstdict['name'] = "Balance B/F"
#                 firstdict['state'] = "N|A"
#                 firstdict['debit'] = "N|A"
#                 firstdict['credit'] = "N|A"
#                 firstdict['balance'] = "N|A"
#
#                 smalldict['date'] = convertDateToBrianType(value['date'])
#                 smalldict['amount'] = value['amount']
#                 smalldict['name'] = value['name']
#                 smalldict['balance'] = round(float(value['balance']), 2)
#                 bigdict[value['timestamp']] = smalldict
#
#     hola = (round(totdebit, 2), round(totcredit, 2))
#     full.append([hola, bigdict])
#     return full
#
#
# def currentMY():
#     mydate = datetime.now()
#     month = mydate.strftime("%b")
#     year = mydate.strftime("%Y")
#     return f'{month}-{year}'
#
#
# def brianwebremember():
#     ref = dbs.reference('web')
#     snapshot = ref.child('brianweb').get()
#     if snapshot:
#         return True
#     else:
#         return False
#
#
# def homewebremember():
#     ref = dbs.reference('web')
#     snapshot = ref.child('homeweb').get()
#     if snapshot:
#         return True
#     else:
#         return False
#
#
# def doesPassExist(password):
#     ref = dbs.reference('users')
#     snapshot = ref.child(password).get()
#     if snapshot:
#         return True
#     else:
#         return False
#
#
# def allexpenses_farm():
#     ref = dbs.reference('farm')
#     snapshot = ref.child('expenses').order_by_child('timestamp').limit_to_last(1000).get()
#     result = snapshot.values()
#     bigdict = {}
#     for value in result:
#         smalldict = {}
#         smalldict['suppliername'] = "N|A"
#         if "suppliername" in value.keys():
#             smalldict['supplier'] = value['suppliername']
#         smalldict['description'] = "N|A"
#         if "description" in value.keys():
#             smalldict['description'] = value['description']
#         smalldict['layer'] = "N|A"
#         if "layer" in value.keys():
#             smalldict['layer'] = value['layer']
#         smalldict['unit'] = "N|A"
#         if "unit" in value.keys():
#             smalldict['unit'] = value['unit']
#         smalldict['quantity'] = "N|A"
#         if "quantity" in value.keys():
#             smalldict['quantity'] = value['quantity']
#         smalldict['amountperunit'] = "N|A"
#         if "amountperunit" in value.keys():
#             smalldict['amountperunit'] = value['amountperunit']
#         smalldict['date'] = convertDateToBrianType(value['date'])
#         smalldict['amount'] = value['amount']
#         smalldict['expensetype'] = value['expensetype']
#         smalldict['transaction'] = value['transaction']
#         smalldict['my'] = value['my']
#         bigdict[value['timestamp']] = smalldict
#     return bigdict
#
#
# def allsales_farm():
#     ref = dbs.reference('farm')
#     snapshot = ref.child('sales').order_by_child('timestamp').limit_to_last(1000).get()
#     result = snapshot.values()
#     bigdict = {}
#     for value in result:
#         smalldict = {}
#         smalldict['date'] = convertDateToBrianType(value['date'])
#         smalldict['soldat'] = value['soldat']
#         smalldict['transaction'] = value['transaction']
#         smalldict['fulluser'] = value['fulluser']
#         smalldict['description'] = "N|A"
#         if "description" in value.keys():
#             smalldict['description'] = value['description']
#         smalldict['my'] = value['my']
#         bigdict[value['timestamp']] = smalldict
#         if "items" in value.keys():
#             smalldict['items'] = [value for value in value['items'].values()]
#             print(smalldict['items'])
#         bigdict[value['timestamp']] = smalldict
#     return bigdict
#
#
# # value = {'1645255149271': {'itemname': 'Sample Item', 'price': '30.0', 'quantity': '2.0'},
# #          '1645255149279': {'itemname': 'Test 5', 'price': '20.0', 'quantity': '2.0'}}
# #
# # print([value for value in value.values()])
#
#
#
# def allCustomerNames_farms():
#     ref = dbs.reference('farm')
#     snapshot = ref.child('clientnames').get()
#     result = snapshot.values()
#     for value in result:
#         name = value['name']
#     return result
#
#
#
#
# def historyForSpecificClientfarm(startdate, enddate, clientName):
#     ref = dbs.reference('farm').child('clienthistory').child(clientName)
#     snapshot = ref.order_by_child('timestamp').limit_to_last(1000).get()
#     result = snapshot.values()
#     bigger_dict = {}
#     for value in result:
#         if 'date' in value.keys():
#             databaseDate = value['date']
#             correnctedDbDate: str = datetime.strptime(databaseDate, '%d-%b-%Y').strftime('%Y-%m-%d')
#             print(startdate, enddate, correnctedDbDate)
#             if startdate <= correnctedDbDate <= enddate:
#                 dict = {}
#                 dict['collected'] = "N|A"
#                 # Random Comment
#                 dict['date'] = "N|A"
#                 if "date" in value.keys():
#                     dict['date'] = convertDateToBrianType(value['date'])
#                 dict['fulluser'] = "N|A"
#                 if "fulluser" in value.keys():
#                     dict['fulluser'] = value['fulluser']
#                 dict['items'] = "N|A"
#                 if "items" in value.keys():
#                     dict['items'] = value['items']
#                 dict['description'] = "N|A"
#                 if "description" in value.keys():
#                     dict['description'] = value['description']
#                 dict['my'] = "N|A"
#                 if "my" in value.keys():
#                     dict['my'] = value['my']
#                 dict['soldat'] = "N|A"
#                 if "soldat" in value.keys():
#                     dict['soldat'] = value['soldat']
#                 timestamp = value['timestamp']
#                 dict['returnedtransaction'] = "N|A"
#                 if "transaction" in value.keys():
#                     dict['returnedtransaction'] = value['transaction']
#                 bigger_dict[timestamp] = dict
#     return bigger_dict
