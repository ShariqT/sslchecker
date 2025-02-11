import ssldatechecker


def test_sslcheck_class():
  checker = ssldatechecker.get("google.com")
  checker.check_certificate()
  assert 'not_valid_after_utc' in dir(checker.certificate_info)

def test_sslcheck_if_cert_is_expired():
  checker = ssldatechecker.get("google.com")
  checker.check_certificate()
  assert checker.is_date_expired() == False


def test_sslcheck_days_until_expiry():
  checker = ssldatechecker.get("google.com")
  checker.check_certificate()
  assert checker.days_until_expiry() > 5

