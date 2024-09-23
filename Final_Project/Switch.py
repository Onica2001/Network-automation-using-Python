
def meniu():
    while True:
        print("1. Configure Etherchannel")
        print("2.Configure STP")
        print("3. Configure RSTP")
        print("4. Configure port-security")
        print("5. Configure BPDUGUARD")
        print("6. Shutdown interfaces")
        print("7. Return to Customer Office")
        option=int(input("Choose an option: "))
        if option==1:
           print()
        elif option==7:
            break
        else:
            print("Invalid option!")

