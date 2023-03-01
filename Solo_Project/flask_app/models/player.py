from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import roster
from flask import flash

db = "lineup_builder"
class Player:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.position = data['position']
        self.salary = data['salary']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM players;"
                
        results = connectToMySQL(db).query_db(query)
        players = []
        for result in results:
            this_player = cls(result)
            players.append(this_player)
            
        return players

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM players WHERE players.id = %(id)s;"

        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return False
        this_player = cls(result[0])
        
        return this_player


    
    @classmethod
    def get_by_name(cls, query_params):
        query = "SELECT * FROM players WHERE players.name = %(name)s"
        results = connectToMySQL(db).query_db(query, query_params)
        if results:
            return cls(results[0])
        else:
            return None


    @classmethod
    def get_by_position(cls,data):
        query = "SELECT * FROM players WHERE players.position = %(position)s;"
        
        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return False
        this_player = cls(result[0])
        
        return this_player
    


    @classmethod
    def get_players_by_roster_id(cls, roster_id):
        query = """
            SELECT players.*, 
                CASE 
                    WHEN players.id = rosters.quarterback_id THEN 'QB' 
                    WHEN players.id = rosters.running_back1_id THEN 'RB1' 
                    WHEN players.id = rosters.running_back2_id THEN 'RB2' 
                    WHEN players.id = rosters.wide_receiver1_id THEN 'WR1' 
                    WHEN players.id = rosters.wide_receiver2_id THEN 'WR2' 
                    WHEN players.id = rosters.tight_end_id THEN 'TE' 
                    WHEN players.id = rosters.kicker_id THEN 'K' 
                    WHEN players.id = rosters.defense_id THEN 'DEF' 
                    ELSE '' 
                END AS position 
            FROM players 
            JOIN rosters ON 
                players.id = rosters.quarterback_id OR 
                players.id = rosters.running_back1_id OR 
                players.id = rosters.running_back2_id OR 
                players.id = rosters.wide_receiver1_id OR 
                players.id = rosters.wide_receiver2_id OR 
                players.id = rosters.tight_end_id OR 
                players.id = rosters.kicker_id OR 
                players.id = rosters.defense_id 
            WHERE rosters.id = %(roster_id)s
        """
        data = {'roster_id': roster_id}
        results = connectToMySQL(db).query_db(query, data)
        players = []
        for result in results:
            this_player = cls(result)
            players.append(this_player)
        return players




