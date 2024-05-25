class Nobel:
    def __init__(self,guruh,year,winner):
        self.guruh=guruh
        self.year=year
        self.winner=winner


    def __str__(self):
        return f"Nobel Prize {self.guruh} {self.year}{self.winner}"
    

prs=Nobel("Peace", 2005, " Muhammad Yunus ")
print(prs)


   

        
        