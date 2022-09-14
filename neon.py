from cmd import Cmd

class mainGUIPrompt(Cmd):
    from rich import print 
    import os
    import time
    import platform
    import os

    global neonVersion
    global localSystemOS
    global LOGIN_BOOL

    neonVersion = '0.0.41'

    #!#!    CHANGE THIS LATER DUMBASS    #!#! 
    LOGIN_BOOL = False

    def detectOS():
        import platform
        localSystemOS = platform.system()
        return localSystemOS

    localSystemOS = detectOS()

    def wipeterm():
        import os
        if localSystemOS == "Windows":
            os.system('cls')
        elif localSystemOS == "Linux":
            os.system('clear')
        elif localSystemOS == 'Darwin':
            os.system('clear')

    wipeterm()

    def loginAuthMessage_NONETYPE():
        import time
        print("")
        print('NOTICE: No user accounts have been set up!')
        time.sleep(.7)
        print("")
        print("Navigate to 'config/users/generate' to set up a user!")
        print("")        
        time.sleep(2)
        print("Logging in as: 'guest'")
        time.sleep(1)

    if LOGIN_BOOL == False:
        loginAuthMessage_NONETYPE()


    #last_output = ''

    def do_shell(self, line):
        import os
        "Execute CLI commands on your external OS from within the Neon OS"
        print("Executing: ", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output




    

    print("")
    print("")

    asciiWelcomes = {
"noc1":'''
  ███╗   ██╗ ██████╗  ██████╗
  ████╗  ██║██╔═══██╗██╔════╝
  ██╔██╗ ██║██║   ██║██║     
  ██║╚██╗██║██║   ██║██║     
  ██║ ╚████║╚██████╔╝╚██████╗
  ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝
                           

''',"neon1":'''
                                        ███╗   ██╗███████╗ ██████╗ ███╗   ██╗
                                        ████╗  ██║██╔════╝██╔═══██╗████╗  ██║
                                        ██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║
                                        ██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║
                                        ██║ ╚████║███████╗╚██████╔╝██║ ╚████║
                                        ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
'''}                                 

    print(asciiWelcomes["neon1"])
    print("")
    print('''                                   NEON OS v(0.2.20) running from a Windows machine.

------------------------------------------------------------------------------------------------------------------------


  [ ? ]  --   # Display help commands
  [ q ]  --   # Exit NeonOS

  '''+str()+str()+'''
------------------------------------------------------------------------------------------------------------------------''')
    print("")

    def onboardNewUser():
        print('''   New? To get started, type [ config ] to change into the /config/ folder.
Then do the same to get into /config/users/generate/

   Otherwise, to quickly set up a new user without providing credentials or other userful
information, enter [ adduser.noconf ]
''')

    if LOGIN_BOOL == False:
        onboardNewUser()

    def promptConfig(LOGIN_BOOL):
        U_NAME = 'agriffin'
        if LOGIN_BOOL == False:
            prompt = "[_please_log_in!_@NEON] $ "
        else: 
            prompt = "["+str(U_NAME)+"@NEON] $ "
        return prompt
    
    prompt = promptConfig(LOGIN_BOOL)

    
    def do_exit(self, inp):
        print("")
        print("Peace ✌️") 
        print("")
        return True
    
    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')
    
    def do_add(self, inp):
        print("adding '{}'".format(inp))
    
    def help_add(self):
        print("Add a new entry to tfhe system.")
    
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
    
        print("Default: {}".format(inp))
    
    do_EOF = do_exit
    help_EOF = help_exit


    pageStorageDict = {
        "confyg":{ 
            "users":['generate','edit','remove'],
            "yadayada":['data'],   
        },
        "remote":{
            "ssh":['default','tunneled'],
            "smh":[""]
        }


    }

    def do_ls(pageStorageDict):
        print(pageStorageDict)

    def do_confyg(pageStorageDict):
        print(pageStorageDict["confyg"])


    
if __name__ == '__main__':
    mainGUIPrompt().cmdloop()