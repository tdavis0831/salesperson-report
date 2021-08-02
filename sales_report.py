"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #creating empty list to use
melons_sold = [] #creating empty list to use

f = open('sales-report.txt') #opens the report
for line in f:
    line = line.rstrip() #strips the white space at end of line
    entries = line.split('|') #splits the text at the pipe char

    salesperson = entries[0] #name of sales person are index 0
    melons = int(entries[2]) #takes the 2nd indx and makes them integers

    if salesperson in salespeople: #checking to see if name in new list
        position = salespeople.index(salesperson) #if they are in the list, we find the index of where they are in the list 

        melons_sold[position] += melons #adds melons to their total (running )
    else: #if name not in list, add it to the salesperson dictionary
        salespeople.append(salesperson) #adds the name
        melons_sold.append(melons) # adds the melons


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') 
    #prints out the name of sales people and how many melons they sold


#could create a dictionary and add the key being the name and the value being the melons sold # Create a list of data and unpack its values

            """name, total, melons_sold = line.split('|')
            sales_people_and_sales={}
            # Set or increment the salesperson's total melons sold
            if salesperson_name in mels_by_sales:
                sales_people_and_sales[name] += int(melons_sold)
            else:
                sales_people_and_sales[name] = int(melons_sold)"""
                