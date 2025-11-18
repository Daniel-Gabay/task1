import logging
import json
class Machine:
    #The constructor    def __init__(self, name: str, os: str, cpu: int, ram: int):
    def __init__(self, name: str, os: str, cpu: int, ram: int):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

        logging.info(f"creating a new machine: {self.name}, os: {self.os}, cpu: {self.cpu}, ram: {self.ram}")

    def to_dict(self):
            return {
                "name": self.name,
                "os": self.os,
                "cpu": self.cpu,
                "ram": self.ram
            }
    

