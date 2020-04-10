class Section:
    lower=0
    upper=0
    
    def __init__(self, lower, upper):

        if not(isinstance(lower,int) 
            or isinstance(upper,int)
        ):
            raise TypeError("input not int value")
        
        elif lower>upper:
            raise ValueError("lower has larger value than upper value")
        
        else:
            self.lower=lower
            self.upper=upper

    
    def toString(self):
        return "["+str(self.lower)+", "+str(self.upper)+"]"
    
    def num_in(self, number):
        return ((number-self.lower)*(self.upper-number)>=0)

    def equal(self,other):
        return (self.lower==other.lower) and (self.upper==other.upper)

if __name__ =="__main__":
    x=Section(3,8)
    y=Section(3,8)
    z=Section(4,8)
    print(x.upper,x.lower)
    print(y.toString())
    print(x.num_in(3))
    print(x.equal(y))
    print(y.equal(z))