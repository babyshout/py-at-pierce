def main():
    head(2)
    body(2)
    unitedStates(2)
    body(2)
    tail(2)
    
    
def head(count):
    print("   /\\    " * count);
    print("  /  \\   " * count);
    print(" /    \\  " * count);
    
    
def body(count):
    print("+------+ " * count);
    print("|      | " * count);
    print("|      | " * count);
    print("+------+ " * count);
    
def unitedStates(count):
    print("|United| " * count)
    print("|States| " * count)

def tail(count):
    print("   /\\    " * count)
    print("  /  \\   " * count)
    print(" /    \\  " * count)
    
    
main()
