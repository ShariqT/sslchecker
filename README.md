# SSLChecker

The purpose of this library is to get the status of SSL certificates -- mainly to make sure that the certificate is still valid.

## Usage

```python

import sslcheck

checker = sslcheck.get("google.com")
checker.check_certificate()

print(checker.certificate_info)
# <Certificate(subject=<Name(CN=*.google.com)>, ...)>

print(checker.is_date_expired())
# False

print(checker.days_until_expiry())
# 80
```

checker.certificate_info is an instance of the [x.509 Certificate Class](https://cryptography.io/en/latest/x509/reference/#cryptography.x509.Certificate) and will have the full certificate information. 


