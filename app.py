import subprocess
import os
from ip2geotools.databases.noncommercial import DbIpCity
import time
from console_progressbar import ProgressBar


class TraceRoute:
    def __init__(self):
        pass

    def runCommand(self, cmd, args):
        # run shell command in subprocess and save the resuts in array as strings
        self.cmd = cmd
        self.args = args
        route_data = []
        response = subprocess.run([cmd, args], stdout=subprocess.PIPE)
        # print(response.stdout.decode('utf-8'))
        route_data.append(response.stdout.decode('utf-8'))
        return route_data

    def dataCleanig(self):
        # extract ip addresses from shell command outputs
        pass

    def getCoordinates(self, ip_add):
        # get latitudes and longitudes from routers ip addresses
        self.ip_add = ip_add
        response = DbIpCity.get(ip_add, api_key='free')
        return {'lat': response.latitude,
                'log': response.longitude}

    def mapPlotter(self):
        # plot coordinates on map
        pass


if __name__ == "__main__":
    obj = TraceRoute()
    pb = ProgressBar(total=100, prefix='Here', suffix='Now',
                     decimals=3, length=50, fill='X', zfill='-')
    pb.print_progress_bar(2)
    time.sleep(5)
    print(obj.runCommand('ping', 'google.com'))
