import subprocess
from qbittorrent import Client

qb = Client('http://127.0.0.1:8090/')

torrents = qb.torrents()

while True:
    for torrent in torrents:
        if len(qb.torrents(filter='downloading')) == 0 and 'Connected' in subprocess.run(['nordvpn','status'], stdout=subprocess.PIPE).stdout.decode('utf-8'):
            subprocess.run(['nordvpn','disconnect'])
        if len(qb.torrents(filter='downloading')) > 0 and 'Disconnected' in subprocess.run(['nordvpn','status'], stdout=subprocess.PIPE).stdout.decode('utf-8'):
            subprocess.run(['nordvpn', 'connect'])
