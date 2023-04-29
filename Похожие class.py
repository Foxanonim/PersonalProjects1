class workers:
    def __init__(self, workername = "John"):
        self.workername = workername

class company:
    def __init__(self, name = "Company"):
        self.name = name
        self.workers = []
    def add_worker(self, workers):
        self.workers.append(workers)

    def print_workers(self):
        if self.workers != []:
            print(f'Name of {self.name} workers')
            for workers in self.workers:
                print(workers.workername)
        else:
            print(f'There are no passengers in car')

george = workers('George')
billy = workers('Billy')
PrivatBank = company("PrivatBank")

PrivatBank.add_worker(george)
PrivatBank.add_worker(billy)

PrivatBank.print_workers()