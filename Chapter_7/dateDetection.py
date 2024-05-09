import re

def main():
    mmddyyyy = r"^(0[1-9]|1[012])(\/+?)(0[1-9]|[12][0-9]|3[01])(/+?)([12][0-9]{1,3})$"

    dateRegex = re.compile(mmddyyyy)

    print(validDate("02/29/2000", dateRegex))

def validDate(date, dateRegex):
    
    mo = dateRegex.search(date)
    for i in range(6):
        print(mo.group(i))
    if mo.group(1) == '02':
        day, year = int(mo.group(3), mo.group(6))
        
        if year in range(1,29):
            return True 
        elif year == 29:
            if year % 400 == 0:
                return True
            elif year % 100 == 0:
                return False
            elif year % 4 == 0:
                return True
            return False
            
        
        
    
    if mo.group[1] in ['04', '06', '09', '11']:
        pass

if __name__ == "__main__":
    main()