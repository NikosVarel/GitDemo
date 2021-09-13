import pytest

@pytest.mark.usefixture("quantity")
@pytest.mark.usefixture("user")
class TestUserInfo:

    def test_hobbie(self,user,quantity):
        print(f"I {user['first_name']} with last name {user['last_name']} love to {user['hobby']} a {quantity}!")

    def test_age(self,user):
        print(f"{user['first_name']} {user['last_name']} is {int(user['age'])} years old!")

# pytest --html=Sheets\report.html -v