from ip2geotools.databases.noncommercial import DbIpCity


def test1(ip_add):
    response = DbIpCity.get(ip_add, api_key='free')
    return {'lat': response.latitude,
            'log': response.longitude}


ip_list = [
    '59.180.212.202',
    '59.180.210.150',
    '72.14.208.12',
    '172.253.68.91',
    '172.253.67.99',
    '216.58.196.100'
]


if __name__ == "__main__":
    for ip in ip_list:
        print(test1(ip))
    # print(test1('72.14.208.12'))
