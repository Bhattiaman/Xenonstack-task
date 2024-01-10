import subprocess

def get_cpu_info():
    try:
        cpu_info = subprocess.check_output(["lscpu"]).decode("utf-8")
        return cpu_info
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"

def get_memory_info():
    try:
        memory_info = subprocess.check_output(["free", "-h"]).decode("utf-8")
        return memory_info
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"

def internsctl(args):
    parts = args.split()
    if len(parts) == 3 and parts[0] == "internsctl" and parts[1] in ["cpu", "memory"] and parts[2] == "getinfo":
        if parts[1] == "cpu":
            return get_cpu_info()
        elif parts[1] == "memory":
            return get_memory_info()
    else:
        return "Invalid command"

if __name__ == "__main__":
    command = input("Enter command: ")  # This can be "internsctl cpu getinfo" or "internsctl memory getinfo"
    output = internsctl(command)
    print(output)
