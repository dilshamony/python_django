for team in icc_test_wc_data:
    won=icc_test_wc_data[team]["won"]
    if(won>5):
        print(icc_test_wc_dat[team]["id"]," ",icc_test_wc_data[team]["won"])


#print datails according to input value

per=float(input("enter percentage"))
for data in icc_test_wc_data:
    perc=float(icc_test_wc_data[data]["pct"])
    if perc>=per:
        print(icc_tast_wc_data[id]["id"]," ",icc_test_wc_data[data]["pct"])
    else:
        pass
    break
#print details based on input

id=input("enter team name")
property=input("enter property")
if id in icc_test_wc_data:
    if property in icc_test_wc_data[id]:
