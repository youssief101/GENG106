def main():
    try:
        hourly_rate = float(input("Enter rate per hour(QAR)"))
        hours = int(input("Enter total hours worked? "))
        payment = hours * hourly_rate
        f = open('Tax.txt', 'r')
        tax_rate = float(f.read())
        tax_amount = tax_rate * payment
        print(tax_amount)
    except FileNotFoundError:
        print('ERROR: file not found')
    except ValueError:
        print('ERROR: total hours worked must be integer')
    
main()
