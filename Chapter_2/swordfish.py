while True:
    name = input("Who are you? ")
    if name.capitalize() != "Joe":
        continue
    print("Hello, Joe. What is the password? (It is a fish.)")
    while True:
        password = input("password: ")
        if password == 'swordfish':
            break
        else:
            continue
    print("Access granted.")
    break