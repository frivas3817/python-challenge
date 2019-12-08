import os, csv
file_to_load= os.path.join("Resources","budget_data.csv")
file_to_output= os.path.join("analysis","budget_analysis.txt")

tot_m= 0
pre_rev=0
total_rev=0
month_of_change=[]
rev_change_list=[]
great_inc=["",0]
great_dec=["",9999999999]

with open(file_to_load) as revenue_data:
    reader=csv.DictReader(revenue_data)
    for row in reader:
        tot_m +=1
        total_rev=int(row["Profit/Losses"])
        rev_change=int(row["Profit/Losses"])- pre_rev
        pre_rev=int(row["Profit/Losses"])
        rev_change_list +=[rev_change]
        month_of_change +=[row["Date"]]
        if rev_change > great_inc[1]:
            great_inc[0]=row["Date"]
            great_inc[1]=rev_change
        if rev_change < great_dec[1]:
            great_dec[0]=row["Date"]
            great_dec[1]=rev_change
rev_avg=sum(rev_change_list)/ len(rev_change_list)
output=(
    f"\nFinancial Analysis\n"
    f"===================\n"
    f"Total Months: {tot_m}\n"
    f"Total Revenue: ${total_rev}\n"
    f'Averahe Revenue Change: ${rev_avg}\n"
    f'Greatest Increase in Revenue: {great_inc[0]} ${great_inc[1]}\n"
    f'Greatest Decrease in Revenue: {great_dec[0]} ${great_dec[0]}\n")
print(output)
with open(file_to_output,"w") as txt_file:
    txt_file.write(output)
