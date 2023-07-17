import pytest
from datetime import datetime


@pytest.fixture
def successful_signup():
    unique_number = int(datetime.now().timestamp())
    name = 'test'
    country_code = 7
    email = f'mail%2B{unique_number}%40example.com'
    phone = 9513291234
    marketing_agree = 'true'
    body = f"email={email}&full_name={name}+{name}&country_code={country_code}&phone={phone}&first_name={name}&last_name={name}&company=&signup_purpose=&legal_entity=Malta&forced_le=true&comment=&marketing_agree={marketing_agree}"
    return body

