class PlayerStats:
    def __init__(self, player_reader):
        self._player_reader = player_reader
        
    def top_scorer_by_nationality(self, nationality):
        return sorted(filter(lambda player: nationality in player.nationality, 
                             self._player_reader.get_players()), 
                      key=lambda player: (player.goals + player.assists), 
                      reverse=True)
        