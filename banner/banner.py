from termcolor import colored, cprint

def banner_design():
    logo='''
███████████           █████             █████                        
░░███░░░░░░█          ░░███             ░░███                         
 ░███   █ ░   ██████  ███████    ██████  ░███████    ██████  ████████ 
 ░███████    ███░░███░░░███░    ███░░███ ░███░░███  ███░░███░░███░░███
 ░███░░░█   ░███████   ░███    ░███ ░░░  ░███ ░███ ░███████  ░███ ░░░ 
 ░███  ░    ░███░░░    ░███ ███░███  ███ ░███ ░███ ░███░░░   ░███     
 █████      ░░██████   ░░█████ ░░██████  ████ █████░░██████  █████    
░░░░░        ░░░░░░     ░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░     
                                                                    
    '''

    print(colored(logo, "magenta"))
