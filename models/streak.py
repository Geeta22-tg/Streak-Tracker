class Streak:
    def __init__(self, skill, days:int):
        self.skill = skill
        self.days = int(days)

    def increase_streak(self):
        self.days+=1

    def provide_in_list(self)->list:
        return[self.skill,self.days]
    


