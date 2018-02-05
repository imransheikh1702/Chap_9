
# coding: utf-8

# In[6]:


class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.f_name = first_name.title()
        self.l_name = last_name.title()
        self.u_name = username
        self.e_mail = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.f_name + " " + self.l_name)
        print("  Username: " + self.u_name)
        print("  Email: " + self.e_mail)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.u_name + "!")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges() 
            
class Privileges():    
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges Details are : \n")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege.title())
        else:
            print("- This user has no privileges.")
        
msgs = Admin('imran', 'sheikh', 'im_sheikh', 'imran.sh.iobm@gmail.com', 'karachi')
msgs.describe_user()
msgs.greet_user()

msgs.privileges.show_privileges()
print("\nAdding privileges...")

msgs_privileges = ["can add post", "can delete post", "can ban user"]
msgs.privileges.privileges = msgs_privileges
msgs.privileges.show_privileges()

