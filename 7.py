class Person:
    def __init__(self,name,country,date_of_burth):
        self.name=name
        self.country=country
        self.date=date_of_burth

    def ages(self):
        return 2024-self.date



tony=Person(name="Tony",country="USA",date_of_burth=1984)   
print(f"Name: {tony.name}")
print(f"Country: {tony.country}")
print(f"Age: {tony.date}")     
print(f"age:{tony.ages()}")
        