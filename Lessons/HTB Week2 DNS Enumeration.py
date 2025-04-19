#DNS-AXFR script
#dependencies: dnspython, argparse

import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

#Initialize resolver class from dns.resolver as "NS"
NS = dr.Resolver()

#Target domain
Domain = "inlanefreight.com"

# Resolve nameservers to their IP addresses
try:
    NS.nameservers = [str(dr.resolve("ns1.inlanefreight.com", "A")[0]),
                      str(dr.resolve("ns2.inlanefreight.com", "A")[0])]
except Exception as error:
    print(f"Error resolving nameservers: {error}")
    exit()

#List of found subdomains
Subdomains = []

#Define the function to perform DNS zone transfer
def AXFR(domain, nameserver):
    #Try zone transfer for the given domain and nameserver
    try:
        #Perform the zone transfer
        axfr= dz.from_xfr(dq.xfr(nameserver, domain))

        #If zone transfer is successful
        if axfr:
            print('[*] Successful zone transfer from {}'.format(nameserver))

            #Add found subdomains to the list
            for record in axfr:
                Subdomains.append('{}.{}'.format(record.to_text(), domain))

    #If zone transfer fails
    except Exception as error:
        print(error)
        pass

#Main
if __name__ == "__main__":

        #For each nameserver in the list of nameservers
        for nameserver in NS.nameservers:
            #Perform zone transfer
            AXFR(Domain, nameserver)

        #Print the results
        if Subdomains is not None:
            print('[*] Found subdomains:')
            for subdomain in Subdomains:
                 print('{}'.format(subdomain))

        else:
            print('[*] No subdomains found')
            exit()
