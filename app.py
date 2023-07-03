from download import Download
from search import Search
import time
import os
class App(Download,Search):
    
    def __init__(self):
        super(Download,self)
        print(">>> Welcome Sir: Mohamed Hesham I'm your reboot".title())
        time.sleep(1)
        print(">>> can i help you".title())
        time.sleep(1)
        print("...")
        order = input(">>> please enter your order: ".title()).lower()
        if order == "":
            self.lifecycle()
            
        if order == 'exit':
            os.system("exit")
            os.system("exit")
            
        if order == 'download':
           download_mod =  Download()
           if download_mod.status == False:
               self.lifecycle()
               
        if order == 'search':
            search_mod = Search()
            if search_mod.status == False:
               self.lifecycle()
        
         
    def lifecycle(self):
        os.system("clear")
        os.system("cls")
        App()
    

App()
    
 