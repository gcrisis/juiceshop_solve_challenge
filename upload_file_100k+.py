import requests
import os

def upload_file_larger_than_100kB(server):
    f=open('ttt','w')
    f.truncate(1024*150)
    f=open('ttt','r')
    files = {'file':('ttt',f,'application/json')}
    r = requests.post(server+'/file-upload',files=files)
    if not r.ok:
        print 'error'
    print 'success'
    os.remove('ttt')

server = 'http://localhost:3000'
upload_file_larger_than_100kB(server)
