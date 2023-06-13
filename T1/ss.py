
class cal():
    def __init__(self, number):
        self.number = number
        
    def add(self, add_num):
        
        return cal(self.number + add_num)
    
        
    def min(self, sub_num):
        
        return cal(self.number - sub_num)
    
    def __str__(self):
        return str(self.number)

m = cal(5).add(10).min(4)
    
print(m)


