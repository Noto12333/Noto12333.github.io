
class MiniBank:
    mainUserInfo = {}
    def first_option(self):
        fuser_input :int = int(input("Press 1 to login : \n Press 2 to register :"))
        if fuser_input == 1:
            self.login()

        elif fuser_input == 2:
            self.register()

    def returnId(self):
        id = len(self.mainUserInfo)
        for i in range(id,id+1):
            return i

    def login(self):
        print("\n\n________This is from login __________\n\n")
        l_username :str = input("Pls enter username :")
        l_passcode :int = int(input("Pls enter passcode :"))
        exitUser = self.existUser(l_username,l_passcode)
        if exitUser:
            print("\n\n_______Login Success________")
            self.menu()

        else:
            print("___user does not exist____")

    def menu(self):
        print("\n\n_________This is from application___________\n\n")
        menuInput = int(input("Press 1 to transfer :\n Press 2 to withdraw :\n Press 3 to updater userdata :"))
        if menuInput == 1:
            transfreUsername = input("Pls enter user name to transfer : ")
            trasferId = self.transfreId(transfreUsername)
            print("Transfer Id is :",trasferId)
            amount : int = int(input("Enter amount to transfer {0}:".format(self.mainUserInfo[trasferId]["r_username"])))
            print("Amount is :",amount)

        elif menuInput == 2:
            pass
        elif menuInput == 3:
            print("\n\n_________This is from update user data___________\n\n")
            updateUserInput :int = int(input("Press 1 to change Name : \n Press 2 to change passcode :\n Press 3 to change amount:"))
            if updateUserInput == 1:
                oldUsername :str = input("Pls enter old user name : ")
                oldPasscode :int = int(input("Pls enter old passcode :"))
                exitUser = self.existUser(oldUsername,oldPasscode)
                if exitUser:
                    self.updatUsername(oldUsername)
                    print(self.mainUserInfo)

            elif updateUserInput == 2 :
                oldUsername: str = input("Pls enter old user name : ")
                oldPasscode: int = int(input("Pls enter old passcode :"))
                exitUser = self.existUser(oldUsername, oldPasscode)
                if exitUser:
                    self.updatePasscode(oldUsername)
                    print(self.mainUserInfo) 

            elif updateUserInput == 3:
                updateUsername:str = input("Pls enter your user name :") 
                updatePasscode: int = int(input("Pls enter your passcode :"))
                exitUser = self.existUser(updateUsername,updatePasscode)
                if exitUser:
                    self.updateAmount(updateUsername)
                    print(self.mainUserInfo)


    def updateAmount(self,updateUsername):
        myId = self.transfreId(updateUsername)
        newAmount :int = int(input("Enter amount to update :"))
        oldAmount = self.mainUserInfo[myId]["r_amount"]
        updateAmount = oldAmount + newAmount
        self.mainUserInfo[myId]["r_amount"] = updateAmount


    def updatePasscode(self,oldUsername):
        myId = self.transfreId(oldUsername)
        newPasscode: int = int(input("Pls enter new passcode :"))
        self.mainUserInfo[myId]["r_passcode"] = newPasscode
        print("\n________Passcode change successfully__________\n\n")

    def updatUsername(self,oldUsername):
        myId = self.transfreId(oldUsername)
        newUsername: str = input("Pls enter new user name :")
        self.mainUserInfo[myId]["r_username"] = newUsername
        print("\n________Name change successfully__________\n\n")



    def transfreId(self, Username):
        userInfoLen = len(self.mainUserInfo)
        for i in range(0,userInfoLen+1):
            if self.mainUserInfo[i]["r_username"] == Username:
                return i
        return None

    def existUser(self,l_username,l_passcode):
        user_count = len(self.mainUserInfo)
        for i in range(0, user_count + 1):
            if l_username == self.mainUserInfo[i]["r_username"] and l_passcode == self.mainUserInfo[i]["r_passcode"]:
                return True
        return None


    def register(self):
       print("_________This is from register ________")
       r_username : str = input("Pls enter username to register :")
       r_passcode1 : int = int(input("Pls enter passcode to register :"))
       r_passcode2 : int = int(input("Pls enter passcode again to confirm :"))
       r_amount :int = int(input("Pls enter amount :"))
       if r_passcode1 == r_passcode2:
           id = self.returnId()
           form = {id:{"r_username":r_username,"r_passcode":r_passcode1,"r_amount":r_amount}}
           self.mainUserInfo.update((form))
           print(self.mainUserInfo)
           print("________Register Successful__________")
           #amount = int(input("Enter amount : "))
       else:
           print("_____Pls Check Your register____")


if __name__ == "__main__":
    miniBank : MiniBank = MiniBank()
    while True:
        miniBank.first_option()