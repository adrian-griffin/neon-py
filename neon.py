from cmd import Cmd


###[init] [Deploying global vars]
############
global neptVersion
global localSystemOS

###[dec] [Declaring global var values]
############
neptVersion = '0.0.41'

def detectOS():
    import platform
    localSystemOS = platform.system()
    return localSystemOS
localSystemOS = detectOS()



        




class mainGUIPrompt(Cmd):
    import os
    import time
    if localSystemOS == "Windows":
        os.system('cls')
    elif localSystemOS == "Linux":
        os.system('clear')
    elif localSystemOS == 'Darwin':
        os.system('clear')

    print("")
    print("")

    asciiWelcomes = {
"noc1":'''
-------------------------------------------------------------  
            

                ███╗   ██╗ ██████╗  ██████╗
                ████╗  ██║██╔═══██╗██╔════╝
                ██╔██╗ ██║██║   ██║██║     
                ██║╚██╗██║██║   ██║██║     
                ██║ ╚████║╚██████╔╝╚██████╗
                ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝
                           

-------------------------------------------------------------  
''',"neon1":'''
-------------------------------------------------------------  
            
            ███╗   ██╗███████╗ ██████╗ ███╗   ██╗
            ████╗  ██║██╔════╝██╔═══██╗████╗  ██║
            ██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║
            ██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║
            ██║ ╚████║███████╗╚██████╔╝██║ ╚████║
            ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝

-------------------------------------------------------------  
'''}                                 

    print(asciiWelcomes["noc1"])
    intro = '''Helpful Commands:

       '?' -  List All Currently Available Commands
    'help' -  List All Documented Commands
    'exit' -  Exit Out of Nept Terminal
    '''
    print("")
    print("")
    prompt = '''[agriffin@Neon]
    
$  '''
    
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
    
if __name__ == '__main__':
    mainGUIPrompt().cmdloop()