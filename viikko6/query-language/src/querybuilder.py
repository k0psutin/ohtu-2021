from matchers import *

class QueryBuilder():
    def __init__(self):
        self.queries = []
        self.change = False
        
    def playsIn(self, team):
        self.queries.append(PlaysIn(team))
        return self
    
    def hasAtLeast(self, value, attr):
        self.queries.append(HasAtLeast(value,attr))
        return self
    
    def hasFewerThan(self,value,attr):
        self.queries.append(HasFewerThan(value,attr))
        return self
    
    def oneOf(self, q1,q2):
        self.queries = Or(And(q1),And(q2))
        self.change = True
        return self
    
    def build(self):
        matcher = And(*self.queries) if not self.change else self.queries
        self.queries = []
        self.change = False
        return matcher