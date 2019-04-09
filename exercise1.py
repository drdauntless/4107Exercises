def helperWaysToMakeBill(amountWanted):
    bills = [100, 50, 20, 10 ,5, 1]
    return waysToMakeBill(amountWanted, bills, 0)
def waysToMakeBill(amount, bills, index):
    if(amount == 0):
        return 1
    if(amount<0 or index>=len(bills)):
        return 0
    withFirstBill=waysToMakeBill(amount-bills[index], bills, index)
    withoutFirstBill= waysToMakeBill(amount,bills, index+1)
    #print(withoutFirstBill)
    return withFirstBill + withoutFirstBill
print(helperWaysToMakeBill(500))
