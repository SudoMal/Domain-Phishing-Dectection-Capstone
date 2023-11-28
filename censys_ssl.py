#!/usr/bin/env python3

from censys.search import CensysCertificates
import os

# Set your Censys API ID and Secret
os.environ["CENSYS_API_ID"] = " 0724eb4d-0c0d-4967-b4c9-ee3aa905febb "
os.environ["CENSYS_API_SECRET"] = " 1xJQxV0dA745NtEa8uAu3QIlL3D46bfd"

c = CensysCertificates()

# Replace 'example.com' with the domain you want to search for
certificates = c.search("parsed.names: example.com")

for cert in certificates:
    print(cert)
