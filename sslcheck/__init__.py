# Based on code from Sharuzzaman Ahmat Raslan
from cryptography import x509
import socket
import ssl
import pprint
from datetime import datetime
import pytz

class Sslcheck():
  def __init__(self, domain):
    self.domain = domain
    self.certificate_info = None
    self.context = None
  
  def check_certificate(self):
    # create default context
    self.context = ssl.create_default_context()

    # override context so that it can get expired cert
    self.context.check_hostname = False
    self.context.verify_mode = ssl.CERT_NONE
    with socket.create_connection((self.domain, 443)) as sock:
      with self.context.wrap_socket(sock, server_hostname=self.domain) as ssock:

        # get cert in DER format
        data = ssock.getpeercert(True)

        # convert cert to PEM format
        pem_data = ssl.DER_cert_to_PEM_cert(data)

        # pem_data in string. convert to bytes using str.encode()
        # extract cert info from PEM format
        cert_data = x509.load_pem_x509_certificate(str.encode(pem_data))

        # load cert info in instance variable
        self.certificate_info = cert_data
  

  def is_date_expired(self):
    today = datetime.now(tz=pytz.UTC)
    return today > self.certificate_info.not_valid_after_utc
  
  def days_until_expiry(self):
    today = datetime.now(tz=pytz.UTC)
    time_left = self.certificate_info.not_valid_after_utc  - today 
    return time_left.days



def get(domain):
  return Sslcheck(domain)