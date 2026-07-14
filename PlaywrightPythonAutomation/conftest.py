import pytest

#conftest file is default file to execute all files test cases.

@pytest.fixture()
def preconditon2():
    print("preconditon2")
    yield                  #this is use becz above is pre cond and belo is post cond so we don't need to write sapartely methods for pre and post
    print("postcondition2")

@pytest.fixture(autouse=True, scope="session")   #if we use autouse=True then we don't need to add parameter manually to the test, it automatically
#execute. if we use scope=session then once this we execute once, pre & post enitre cycle, if we use function in place of sessionthen it will execute before ecach and every test case.
def preconditon():
    print("preconditon")
    yield                  #this is use becz above is pre cond and belo is post cond so we don't need to write sapartely methods for pre and post
    print("postcondition")    