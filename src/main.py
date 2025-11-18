import json 
from machine import Machine

def save_machine(machine, file_path="src/configs/instances.json"):


    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
        
    data.append(machine.to_dict())
    


    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("Machine saved successfully")


def read_user():
    #enter machine name 
        name = input("enter machine name: ").strip()
        while len(name) >=10: 
            print("you didn't enter a name . . ")
            name = input("enter machine name: ").strip()
        

        #os must be ubuntu, centos or windows
        os = input("Operating System (ubuntu, centos, windows): ").strip()
        while  os not  in ["ubuntu", "centos", "windows"]:
            print(f"the {os} is not valid os. try again. ")
            os = input("Operating System (ubuntu, centos, windows): ").strip()



    #cpu must be a positive number
        cpu = input("CPU cores (number): ").strip()
        while not cpu.isdigit() or int (cpu) <= 0:
            print("CPU must be a positive number. ")
            cpu = input("CPU cores (number) ").strip()
        cpu = int (cpu)



        ram = (input("RAM size (GB): ")).strip()
        while not ram.isdigit() or int (ram) <= 0:
            print("RAM must be a positive number. ")
            ram = input("RAM size (GB): ").strip()
        ram = int (ram)


        return Machine(name, os, cpu, ram)


print("starting the program . . .")
machine = read_user()
save_machine(machine)




