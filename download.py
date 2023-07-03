import os,sys ,time, httplib2 , urllib.request  ,gzip


class Download:
    status = True
    webpath=""
    syspath=""
    dirname=""
    viewfile=""
    def __init__(self):
       
        print(">>> Hi  , You are Now In Download Environment".title())
        self.webpath = self.webPathProccess()
        self.syspath = self.sysPathProccess()
        self.dirname = self.sysdirname()
        self.viewfile=  input(">>> sir you would to open the link after download [yes/no]: ").lower()
        print("...>>> wait for starting download")
        download_string = """
        =================================================
                        DOWNLOAD ENV
        =================================================
        """
        print(download_string)
        time.sleep(2)
        os.system(f"curl -o {self.webpath} > {os.path.join(self.syspath,self.dirname)}")
        if self.viewfile == 'yes':
            os.system(f"START {self.webpath}")
        print(f"...>>> Downloaded {self.dirname}")
        self.status = False
        
            
        
        
    def webPathProccess(self):
        
        Webpath = input(">>> Please Sir Enter Your website Path: ".title())
        if Webpath == "":
            Webpathcheck = input(">>> Sorry Sir The website Path Is Required Please Enter it: ".title())
            if Webpathcheck == "":
                message = ">>> I Need To Path For Download Anything you want it , Sir You Wanna Completing this process [yes/no]: ".title()
                status = input(message).lower()
                if(status == 'no'):
                    print(">>> Thank You Sir For Trust me ".title())
                    self.status = False
        return Webpath
    
    
    def sysPathProccess(self):
        os.system("clear")
        os.system("cls")
        print("... >>> Second Step:-".title())
        print("")
        Syspath = input(">>> Please Sir Enter Your system Path: ".title())
        if Syspath == "":
            Webpathcheck = input(">>> Sorry Sir The system Path Is Required Please Enter it: ".title())
            if Webpathcheck == "":
                message = ">>> I Need To Path For Download Anything you want it , Sir You Wanna Completing this process [yes/no]: ".title()
                status = input(message).lower()
                if(status == 'no'):
                    print(">>> Thank You Sir For Trust me".title())
                    self.status = False
        if not os.path.exists(Syspath):
            print(">>> The system path not right please try again ".title())
            time.sleep(3)
            self.sysPathProccess()
        return Syspath
    
    
    def sysdirname(self):
        print("... >>> Third Step: ".title())
        dirname = input(">>> Please Sir Enter Your Directory Name: ".title())
        if dirname == "":
            Webpathcheck = input(">>> Sorry Sir The system Path Is Required Please Enter it: ".title())
            if Webpathcheck == "":
                message = ">>> I Need To Path For Download Anything you want it , Sir You Wanna Completing this process [yes/no]: ".title()
                status = input(message).lower()
                if(status == 'no'):
                    print(">>> Thank You Sir For Trust me ".title())
                    self.status = False
       
        return dirname
                    
    
        
        
        
    