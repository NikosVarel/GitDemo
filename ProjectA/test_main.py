import pytest

@pytest.mark.usefixture("quantity")
@pytest.mark.usefixture("user")
class TestUserInfo:

    def test_hobbie(self,user,quantity):
        print(f"I {user[0]} with last name {user[1]} love to {user[3]} {quantity}!")

    def test_age(self,user):
        print(f"{user[0]} {user[1]} is {int(user[2])} years old!")

# pytest --html=Sheets\report.html -v