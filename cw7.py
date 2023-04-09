list = [10, 20, 30, -69, -7, -25, -87, 69, 34, 88, 69
        ]
 
pos_count, neg_count = 0, 0
 
for num in list:
 
    if num >= 0:
        pos_count += 1
    else:
        neg_count += 1
 
 
print("Positive numbers in the list ", pos_count)
print("Negative numbers in the list", neg_count)