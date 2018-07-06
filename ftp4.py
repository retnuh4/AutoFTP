import ftputil #high level library for comm with ftp servers
from subprocess import Popen #allows batch files to be called

with ftputil.FTPHost('replace_with_hostname', 'replace_with_username', 'replace_with_password') as ftp_host: #connect
    # to ftp client(server(hostname or ip), username, password
    files = ftp_host.listdir(ftp_host.curdir) #define files variable as the current directory when connecting
    for file in files:
        if ftp_host.path.isfile(file):
            ftp_host.download(file, file) #for loop to go through individually and download each "file" within the list "files"
p = Popen("replace_with_batch", cwd=r"C:/replace/with/directoryToThe/storedBatchFile") #calling batch file that moves
#  the downloaded files to a folder and copies it to the network location
# the batch should be located within the same directory the program is running in
stdout, stderr = p.communicate() # not really sure
print("Finished!") #confirmation message
