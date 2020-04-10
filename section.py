class Section:
    val = [0,0]
    def __init__(self, lower, upper):

        if not(isinstance(lower,int) 
            or isinstance(upper,int)
        ):
            raise TypeError("input not int value")
        
        elif lower>upper:
            raise ValueError("lower has larger value than upper value")
        
        else:
            self.val[0]=lower
            self.val[1]=upper

    
    def toString(self):
        return str(self.val)
    
    def num_in(self, number):
        return ((number-self.val[0])*(self.val[1]-number)>=0)

    def equal(self,other):
        return self.val==other.val

if __name__ =="__main__":
    x=Section(3,8)
    y=Section(3,8)
    z=Section(4,8)
    print(x.val)
    print(y.toString())
    print(x.num_in(3))
    print(x.equal(y))
    print(y.equal(z))