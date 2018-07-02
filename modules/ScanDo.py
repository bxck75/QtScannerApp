import sys,os,nmap

class ScanDo:
    
    # def __init__(self):
    #     self.nm = nmap.PortScanner()
    #     self.ports = str('80')
    #     self.network = '-iR 50'
    #     self.arguments = ' -Pn --open -n -p '+self.ports
    #     # self.AsyncScan()

    def AsyncScan(self):
    
        self.nma = nmap.PortScannerAsync()
        def callback_result(host, scan_result):
            print('------------------')
            print(scan_result['nmap']['command_line'])
            print(scan_result['scan'][host]['addresses']['ipv4'])
            # print(host, scan_result)
            print('------------------')
            HasPort(host, scan_result)
            # print(scan_result['scan'])
            # print(scan_result['scan'][host].all_protocols())
            # if(scan_result['scan'][host].has_tcp(21)):
            #     if(scan_result['scan'][host]['tcp'][21]['state'] == 'open'):
            #         print(scan_result['scan'][host]['tcp'][21])
            #         print(scan_result['scan'][host]['addresses']['ipv4'],21,scan_result['scan'][host]['tcp'][21]['state'])

            # print(scan_result['nmap'])
            # print(scan_result['nmap']['scaninfo']['tcp']['services'])
            # print(scan_result['nmap']['scanstats'])

        def HasPort(host, scan_result):
            for port in self.ports.split(','):
                if(scan_result['scan'][host].has_tcp(int(port))):
                        if(scan_result['scan'][host]['tcp'][int(port)]['state'] == 'open'):
                            print(scan_result['scan'][host]['tcp'][int(port)])
                            print(scan_result['scan'][host]['addresses']['ipv4'],int(port),scan_result['scan'][host]['tcp'][int(port)]['state'])
                        else:
                            print(port + " not open but "+scan_result['scan'][host]['tcp'][int(port)]['state'])

        self.nma.scan(hosts=self.network, arguments=self.arguments, callback=callback_result)
        while self.nma.still_scanning():
            print("Waiting >>>")
            self.nma.wait(2) # you can do whatever you want but I choose to wait after the end of   


    # def scanNetwork(self):
    #     # Function for performing a network scan with nmap with the help of the python-nmap module
    #     returnlist = []

    #     a = self.nm.scan(hosts=self.network, arguments=self.arguments)
    #     print(a['nmap'])
    #     for k, v in a['scan'].items():
    #         # print(v)
    #         if str(v['status']['state']) == 'up':
    #             try:
    #                 print(str(v['scan'][v].all_ip()))
    #                 # print(str(v['nmap']))
    #                 # print(str(v['scan'][v].has_tcp(80)))
    #                 returnlist.append([str(v['addresses']['ipv4']), str(v['addresses']['mac'])])
    #             except:
    #                 pass

        # # returnlist = hostsList array
        # return returnlist

    # # print(scanNetwork('192.168.178.17'))
    # def YieldScan(self):
    #     nm = nmap.PortScannerYield()
    #     for progressive_result in nm.scan(self.network, '80,22-25'):
    #         print(progressive_result)

    def forhosts(self):
        import nmap
        returnlist = []
        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sP -iR 10')
        for host in nm.all_hosts():
                print('----------------------------------------------------')
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('----------')
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    lport.sort()
                    for port in lport:
                        print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

        return returnlist


#Function Main Start
if __name__ == '__main__':
    app = ScanDo()

# print(forhosts('190.168.178.17'))

# print(scanNetwork('192.168.178.17'))