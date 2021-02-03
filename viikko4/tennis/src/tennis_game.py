class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def won_point(self, name):
        if self.name == name:
            self.score += 1
        
    def __str__(self):
        return f"{self.name}"
        
class Score:
   
    def __init__(self, p1, p2):
        self.level = ["Love","Fifteen","Thirty","Forty"]
        self.p1 = p1
        self.p2 = p2
        
    def point(self, player):
        self.p1.won_point(player)
        self.p2.won_point(player)
        
    def get_score(self):
        if self.has_win(self.p1,self.p2) or self.has_win(self.p2,self.p1):
            return self.winner()
        elif self.has_tie():
            return self.tie()
        elif self.has_deuce():
            return self.deuce()
        elif self.has_adv():
            return self.adv()
        else:
            return  f"{self.level[self.p1.score]}-{self.level[self.p2.score]}"
    
    def has_win(self, p1, p2):
        return p1.score >= 4 and p1.score - p2.score >= 2
    
    def has_deuce(self):
        return self.p1.score == 4 and self.p2.score == 4
    
    def has_tie(self):
        return self.p1.score == self.p2.score and self.p1.score < 4 and self.p2.score < 4
    
    def has_adv(self):
        return self.p1.score >= 4 or self.p2.score >= 4
    
    def tie(self):
        return f"{self.level[self.p1.score]}-All"    
            
    def deuce(self):
        return f"Deuce"       
    
    def winner(self):
        return f"Win for {self.p1}" if self.has_win(self.p1,self.p2) else f"Win for {self.p2}"
        
    def adv(self):
        if self.p1.score - self.p2.score == 1:
                 return f"Advantage {self.p1.name}"
        else:
            return f"Advantage {self.p2.name}"
            
    
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.score = Score(Player(player1_name), Player(player2_name))

    def won_point(self, player):
        self.score.point(player)
            
    def get_score(self):
        return self.score.get_score()
