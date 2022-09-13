from asyncio import subprocess
from cmd import Cmd
import os
import time

###[init] [Deploying global vars]
############
global neptVersion
global localSystemOS

###[dec] [Declaring global var values]i
############
neptVersion = '0.0.41'
def detectOS():
    import platform
    localSystemOS = platform.system()
    return localSystemOS
localSystemOS = detectOS()

class mainGUIPrompt(Cmd):
    import os

    last_output = ''
    def do_shell(self, line):
        "Execute CLI command on your external OS within the Neon OS"
        print("Executing: ", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output



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

    print(asciiWelcomes["noc1"])
    print("      Smartaira Neon-OS --> v0.2.20")
    intro = '''Helpful Commands:

       '?' -  Help
       'q' -  Exit
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