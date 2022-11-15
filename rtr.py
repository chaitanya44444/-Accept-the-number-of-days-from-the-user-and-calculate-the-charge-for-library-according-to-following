days=int(input("write the days"))
if days > 0 and days <= 5:
    fine = 2 * days

if days >= 6 and days <= 10:
    fine = 3 * days

if days > 10 and days <= 15:
    fine = 4 * days

if days > 15:
    fine = 5 * days
    print(fine)
        
