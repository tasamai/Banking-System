
class Person(object):

    def __init__(self, name, password, address = [None, None, None, None]):
        self.name = name
        self.password = password
        self.address = address

    def get_name(self):
        return self.name
        
    def get_address(self):
        return self.address

    def update_name(self, name):
        self.name = name
        
    def update_address(self, houseno,street,city,postco):
        self.address[0] = houseno
        self.address[1] = street
        self.address[2] = city
        self.address[3] = postco

    def print_details(self):
        print("Name %s:" %self.name)
        print("Address: %s" %self.address[0])
        print("         %s" %self.address[1])
        print("         %s" %self.address[2])
        print("         %s" %self.address[3])
        print(" ")


    def check_password(self, password):
        if self.password == password:
            return True
        return False

    def profile_settings_menu(self):
        #print the options you have
         print (" ")
         print ("Your Profile Settings Options Are:")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Update name")
         print ("2) Update address")
         print ("3) Print details")
         print ("4) Back")
         print (" ")
         option = int(input ("Choose your option: "))
         return option

        
    def run_profile_options(self):
        loop = 1           
        while loop == 1:
            choice = self.profile_settings_menu()
            if choice == 1:
                name=input("\n Please enter new name\n: ")
                self.update_name(name)
            elif choice == 2:
                houseno=input("\nInput house number\n")
                street=input("\nInput Street\n")
                city=input("\nInput City\n")
                postco=input("\nInput postcode\n")
                self.update_address(houseno,street,city,postco)
            elif choice == 3:
                self.print_details()
            elif choice == 4:
                loop = 0                     
