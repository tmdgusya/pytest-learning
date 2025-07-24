import pytest

def test_func1_using_scopes(session_scoped_fixture, module_scoped_fixture, function_scoped_fixture):
    print(f"Running test_func1 -> function_id: {function_scoped_fixture}")
    assert session_scoped_fixture["status"] == "running"
    with open(module_scoped_fixture, "r") as f:
        assert "Module scope data" in f.read()

def test_func2_using_scopes(session_scoped_fixture, module_scoped_fixture, function_scoped_fixture):
    print(f"Running test_func2 -> function_id: {function_scoped_fixture}")
    assert session_scoped_fixture["status"] == "running"
    with open(module_scoped_fixture, "r") as f:
        assert "Module scope data" in f.read()

@pytest.mark.usefixtures("class_scoped_fixture")
class TestClassScopeExample:
    def test_method1(self, function_scoped_fixture):
        print(f"Running test_method1 -> function_id: {function_scoped_fixture}")
        assert True

    def test_method2(self, function_scoped_fixture):
        print(f"Running test_method2 -> function_id: {function_scoped_fixture}")
        assert True