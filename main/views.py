from datetime import datetime
from django.shortcuts import render
from django.template.context_processors import request

# from testPython import db, summationEggsCollected_DateQueryRange, allsummary, summationExpenses_DateSummary, \
#     summationSales_DateQuery, allclients, totalEggsCollectedThisMonth, totalSalesForThisMonth, \
#     totalExpensesForThisMonth, alleggs, allsales, allexpenses, allCustomerNames, historyForSpecificClient, \
#     summationSales, summationEggsCollected, summationExpenses, doesPassExist, allexpenses_farm, summationExpenses_Farm, \
#     summationExpenses_DateSummary_Farm, allsales_farm,allCustomerNames_farms, historyForSpecificClientfarm

def  homepage(request):
    response = render(request, "index.html", {"summary": ""})
    return response
