# FTP is not the most secure way to transfer files, ssh is probably better

from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/specificdomain-or-location/')

def grabFile():
    filename = 'fileName.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETF ', + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    filename = 'fileName.txt'
    ftp.storebinary('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()
