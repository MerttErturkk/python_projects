from LAB_1_TASK_3 import stock,prices,rechnung


#%% Program 1 writes stock to a file 

stockFile = open(r'C:\Users\ERTURK\Desktop\stock.txt',"w")

for key,val in stock.items():
    stockFile.write(str(key)+" "+str(val)+"\n")
stockFile.close()

#%% Program 2 reads and iterates trough lines
with open(r'C:\Users\ERTURK\Desktop\stock.txt',"r") as stock:
    lines=stock.readlines()
    for line in lines:
        print(line)