from validate import validate_email


def test_validate_email():
    assert validate_email("jason@ntnu.edu") != None
    assert validate_email("jason@ntnu.edu.edu") != None


def test_with_subdomain():
    assert validate_email("jason.a@subdomain.domain.edu") != None
