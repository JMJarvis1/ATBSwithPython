import re

def main():

    pwordPatterns = {
        "Has at least one number": r"(\d)+?",
        "Has at least one capital letter": r"([A-Z])+?",
        "Has at least one lowercase letter": r"([a-z])+?",
        "Is at least 8 characters long": r"(\w){8,}",

    }
    
    passwords = ["password5", "admin", "ADMIN", "ABCDefg5", "1234567789" ]
    results = {password:{k:"" for k,v in pwordPatterns.items()} for password in passwords}
    
    for password in passwords:
        for requirement, pattern in pwordPatterns.items():
            results[password][requirement] = checkPasswordStrength(password, pattern)
    
    displayResults(results)

def displayResults(results):
    for password, result in results.items():
        values = []
        print(f"\nPassword: {password}")
        for pattern, value in result.items():
            print(f"\t> {str(pattern + ':').rjust(36)} {str(value)}")
            values.append(value)    
        
        test = "Failed" if False in values else "Passed"
        print(f"\tTest result: {test}")
            
            
        

def checkPasswordStrength(password, pattern):
    " Checks if password includes a specified requirement "

    regex = re.compile(pattern) # regex pattern for password requirement
    return True if regex.search(password) != None else False


if __name__ == "__main__":
    main()