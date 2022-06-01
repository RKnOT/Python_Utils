
#!/usr/bin/python2
#
# Simple script to demonstrate how to delete all files/sub-folders in the shared folder
#
from smb.SMBConnection import SMBConnection

dry_run = True  # Set to True to test if all files/folders can be "walked". Set to False to perform the deletion.
userID = 'Administrator'
password = '2292'
client_machine_name = 'testclient'   # Usually safe to use 'testclient'
server_name = 'pi'   # Must match the NetBIOS name of the remote server
share_name = '\\\\pi\\d$'

server_ip = '192.168.178.106' # Must point to the correct IP address
domain_name = ''           # Safe to leave blank, or fill in the domain used for your remote server
shared_folder = 'PVDataLog'  # Set to the shared folder name



conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True, is_direct_tcp=True)
conn.connect(server_ip, 445)
a= conn.listPath(shared_folder, share_name)
print(dir(conn))
print(conn.smb_message)

def walk_path(path):
    print ('Walking path', path)
    for p in conn.listPath(path, share_name):
        print(p.filename)
        '''
        if p.filename!='.' and p.filename!='..':
            parentPath = path
            if not parentPath.endswith('/'):
                parentPath += '/'

            if p.isDirectory:
                walk_path(parentPath+p.filename)
                print ('Deleting folder (%s) in %s' % ( p.filename, path ))
                if not dry_run:
                    conn.deleteDirectory(shared_folder, parentPath+p.filename)
            else:
                print ('Deleting file (%s) in %s' % ( p.filename, path ))
                if not dry_run:
                    conn.deleteFiles(shared_folder, parentPath+p.filename)
        '''

# Start and delete everything at shared folder root

#path = share_name + '\\'
#print(path) 
#walk_path('\\')

'''
import tempfile
from twisted.internet import reactor
from smb.SMBProtocol import SMBProtocolFactory

class RetrieveFileFactory(SMBProtocolFactory):

    def __init__(self, *args, **kwargs):
        SMBProtocolFactory.__init__(self, *args, **kwargs)

    def fileRetrieved(self, write_result):
        file_obj, file_attributes, file_size = write_result

        # Retrieved file contents are inside file_obj
        # Do what you need with the file_obj and then close it
        # Note that the file obj is positioned at the end-of-file,
        # so you might need to perform a file_obj.seek() to if you
        # need to read from the beginning
        file_obj.close()

        self.transport.loseConnection()

    def onAuthOK(self):
        d = self.retrieveFile(self.service, self.path, tempfile.NamedTemporaryFile())
        d.addCallback(self.fileRetrieved)
        d.addErrback(self.d.errback)

    def onAuthFailed(self):
        print ('Auth failed')

# There will be some mechanism to capture userID, password, client_machine_name, server_name and server_ip
# client_machine_name can be an arbitary ASCII string
# server_name should match the remote machine name, or else the connection will be rejected
userID = 'Administrator'
password = '2292'
client_machine_name = '\\\pi\d$'
server_name = 'pi' 
server_ip = '192.168.178.106'
dir_name = 'PVDataLog'

#userID = 'Administrator'
#pw = '2292'

#server_name = 'pi'
#share_name = '\\\pi\d$'
#server_ip = '192.168.178.106'



factory = RetrieveFileFactory(userID, password, client_machine_name, server_name, use_ntlm_v2 = True)
factory.service = dir_name
factory.path = '/2020_05_03.CSV'
a = reactor.connectTCP(server_ip, 139, factory)
print(dir(factory))
print(factory.listPath())
print('---')
'''
