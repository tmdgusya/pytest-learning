import random
import time
import os

import pytest
from mycalc.calculator import Calculator

@pytest.fixture(scope='function')
def calculator_instance():
    print(f"  [SETUP] Calculator instance")
    yield Calculator()
    print(f"  [END] Calculator instance")

@pytest.fixture(scope="function")
def function_scoped_fixture():
    unique_id = random.randint(1000, 9999)
    print(f"  [SETUP] Function Scoped: {unique_id}")
    yield unique_id
    print(f"  [TEARDOWN] Function Scoped: {unique_id}")

@pytest.fixture(scope="class")
def class_scoped_fixture():
    print(f"  [SETUP] Class Scoped: {__name__}")
    yield
    print(f"  [TEARDOWN] Class Scoped: {__name__}")

@pytest.fixture(scope="module")
def module_scoped_fixture():
    print(f"  [SETUP] Module Scoped: {__name__}")
    module_file = "module_temp_file.txt"
    with open(module_file, "w") as f:
        f.write("Module scope data")
    yield module_file
    print(f"  [TEARDOWN] Module Scoped: {__name__}")
    os.remove(module_file)

@pytest.fixture(scope="session")
def session_scoped_fixture():
    start_time = time.time()
    print(f"  [SETUP] Session Scoped: {__name__}")
    session_data = {"start": start_time, "status": "running" }
    yield session_data
    end_time = time.time()
    session_data["status"] = "finished"
    print(f"  [TEARDOWN] Session Scoped: {end_time}")

@pytest.fixture(autouse=True, scope="function")
def auto_print_start_end():
    print(f"  [SETUP] Function Automatic Print: {__name__}")
    yield
    print(f"  [TEARDOWN] Function Automatic Print: {__name__}")

