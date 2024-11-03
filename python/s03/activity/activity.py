class Camper():
    def __init__(self, name, batch, course_type):
        self.name = name
        self.batch = batch
        self.course_type = course_type


    def career_track(self):
        print(f"Currently enrolled in the {self.course_type} program")


    def info(self):
        print(f"My name is {self.name} of batch {self.batch}")  


zuitt_camper = Camper("john", "b422/2024", "MCP")

print(f"camper Name: {zuitt_camper.name}")
print(f"camper Batch: {zuitt_camper.batch}")
print(f"camper Course: {zuitt_camper.course_type}")

zuitt_camper.info()
zuitt_camper.career_track()

        