scores = [45,70,85,30,90,55]
no_pass = 0
no_fail = 0



total = 0
for score in scores:
    total += score
    if score <= 40:
        no_fail += 1
    else:
        no_pass += 1 

      
print(f"No of Pass: ,{no_pass}")
print(f"No of Fail: ,{no_fail}")  
average = total/len(scores)

print("total: ",total)
   
print("average: ",average)