mat=[
    ["TLV","Ariel","Jerusalem"],
    ["NYC","WDC"],
    ["London","Manchester"]
]

print("All cities",mat)                 #--> All cities [['TLV', 'Ariel', 'Jerusalem'], ['NYC', 'WDC'], ['London', 'Manchester']]

print("Cities in Israel",mat[0])        #--> Cities in Israel ['TLV', 'Ariel', 'Jerusalem']
print("Cities in USA",mat[1])           #--> Cities in USA ['NYC', 'WDC']
print("Cities in UK",mat[2])            #--> Cities in UK ['London', 'Manchester']

print("Main City in Israel",mat[0][0])     #--> Main City in Israel TLV
print("Main City in USA",mat[1][0])        #--> Main City in USA NYC
print("Main City in UK",mat[2][0])         #--> Main City in UK London