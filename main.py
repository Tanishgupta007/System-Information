import platform

my_system = platform.uname()

print(f"System : {my_system.system}")
print(f"Node name : {my_system.node}")
print(f"Version : {my_system.version}")
print(f"Release : {my_system.release}")
print(f"Machine : {my_system.machine}")
print(f"Processor : {my_system.processor}")