#!/usr/bin/env python3
import whois

domain = "www.whois.com"
whois_data = whois.whois(domain)
print(whois_data)
