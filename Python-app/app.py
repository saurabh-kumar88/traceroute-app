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
        cmd_output = []
        response = subprocess.run(
            [cmd, args], stdout=subprocess.PIPE, capture_output=Trues)
        # cmd_output.append(response.stdout.decode('utf-8'))
        self.getCoordinates()

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
        print("City : {}".format(response.city))
        # return {'lat': response.latitude,
        #         'log': response.longitude,
        #         'city': response.city}

    def mapPlotter(self):
        # plot coordinates on map
        pass


if __name__ == "__main__":

    obj = TraceRoute()
    print(obj.getCoordinates('52.95.67.180'))
    # pb = ProgressBar(total=100, prefix='Here', suffix='Now',
    #                  decimals=3, length=50, fill='X', zfill='-')
    # pb.print_progress_bar(2)
    # time.sleep(5)
    # print(obj.runCommand('tracert', 'google.com'))

    # data = obj.runCommand('tracert', 'google.com')
    # print(obj.dataCleanig_tracetroute(data))
    # subprocess.Popen('dir', shell=True)

    # stdout = out.stdout.decode('utf-8')
    # print(stdout)
