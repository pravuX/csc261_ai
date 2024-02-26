class Employee:
    def __init__(self, name, address, dob, height, weight, job):
        self.name = name
        self.address = address
        self.dob = dob
        self.height = height
        self.weight = weight
        self.job = job

    def describe(self):
        print(f'''
{self.name} is a person living in {self.address}. He was born on {self.dob}.
He is {self.height} feet tall and has {self.weight} kg weight. He has a job.
He works at '{self.job.company.name} company' as {self.job.title} and earns {self.job.payrate}.
The company is situated at {self.job.company.address}.
              ''')


class Job:
    def __init__(self, title, company, payrate):
        self.title = title
        self.company = company
        self.payrate = payrate


class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address


if __name__ == "__main__":
    abc_company = Company("ABC", "Kathmandu")
    ai_researcher = Job("AI Researcher", abc_company, "1.5 lacs pm")
    ram = Employee("Ram", "Nepal", "15 December 1990", 6, 75, ai_researcher)
    ram.describe()
