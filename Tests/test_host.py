import importlib
import test_measurement

print("Input a module name\n")
module = input()
print("Input a function name\n")
function = input()

i = importlib.import_module(module)

i.measure()
