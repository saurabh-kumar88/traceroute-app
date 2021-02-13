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
        subprocess.run([cmd, args])
        response = subprocess.run([cmd, args], stdout=subprocess.PIPE)
        print(response.stdout.decode('utf-8'))
        try:
            with open('logs.txt', 'w+') as file:
                file.write(response.stdout.decode('utf-8'))
        except Exception as err:
            return False

        return True

    def dataCleanig_tracetroute(self):
        # extract ip addresses from shell command outputs
        self.shell_output = shell_output
        print(' ------- cleaning this data --------- ')

        return shell_output

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
    # pb = ProgressBar(total=100, prefix='Here', suffix='Now',
    #                  decimals=3, length=50, fill='X', zfill='-')
    # pb.print_progress_bar(2)
    # time.sleep(5)
    # print(obj.runCommand('tracert', 'google.com'))

    # data = obj.runCommand('tracert', 'google.com')
    # print(obj.dataCleanig_tracetroute(data))
    subprocess.Popen('dir', shell=True)

    # stdout = out.stdout.decode('utf-8')
    # print(stdout)
