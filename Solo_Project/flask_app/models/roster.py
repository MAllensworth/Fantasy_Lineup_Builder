from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import player
from flask import flash
import re
from datetime import datetime


db = "lineup_builder"
class Roster:
    def __init__(self,data):
        self.id = data.get('id', None)
        self.name = data['name']
        self.user_id = data['user_id']
        self.quarterback_id = data['quarterback_id']
        self.running_back1_id = data['running_back1_id']
        self.running_back2_id = data['running_back2_id']
        self.wide_receiver1_id = data['wide_receiver1_id']
        self.wide_receiver2_id = data['wide_receiver2_id']
        self.tight_end_id = data['tight_end_id']
        self.kicker_id = data['kicker_id']
        self.defense_id = data['defense_id']
        self.created_at = data.get('created_at', datetime.now())
        self.salary_used = None 
        self.creator = None

        self.quarterback = None
        self.running_back1 = None
        self.running_back2 = None
        self.wide_receiver1 = None
        self.wide_receiver2 = None
        self.tight_end = None
        self.kicker = None
        self.defense = None
        

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM rosters 
                    JOIN users ON rosters.user_id = users.id
                    JOIN players AS quarterback ON rosters.quarterback_id = quarterback.id
                    JOIN players AS running_back1 ON rosters.running_back1_id = running_back1.id
                    JOIN players AS running_back2 ON rosters.running_back2_id = running_back2.id
                    JOIN players AS wide_receiver1 ON rosters.wide_receiver1_id = wide_receiver1.id
                    JOIN players AS wide_receiver2 ON rosters.wide_receiver2_id = wide_receiver2.id
                    JOIN players AS tight_end ON rosters.tight_end_id = tight_end.id
                    JOIN players AS kicker ON rosters.kicker_id = kicker.id
                    JOIN players AS defense ON rosters.defense_id = defense.id
                    """
                
        results = connectToMySQL(db).query_db(query)
        
        rosters = []
        for result in results:
            this_roster = cls(result)
            this_roster.creator = user.User.get_by_id({'id': result['user_id']})
            rosters.append(this_roster)
            
            salary_list = [
                result['salary'], 
                result['running_back1.salary'], 
                result['running_back2.salary'], 
                result['wide_receiver1.salary'], 
                result['wide_receiver2.salary'], 
                result['tight_end.salary'], 
                result['kicker.salary'], 
                result['defense.salary']
            ]
            
            this_roster.salary_used = sum(salary_list)
        return rosters


    def save(self, form_data):
        query = "INSERT INTO rosters (name, user_id, quarterback_id, running_back1_id, running_back2_id, wide_receiver1_id, wide_receiver2_id, tight_end_id, kicker_id, defense_id) VALUES (%(name)s, %(user_id)s, %(quarterback_id)s, %(running_back1_id)s, %(running_back2_id)s, %(wide_receiver1_id)s, %(wide_receiver2_id)s, %(tight_end_id)s, %(kicker_id)s, %(defense_id)s);"

        data = {
            'name': self.name,
            'user_id': self.user_id,
            'quarterback_id': self.quarterback_id,
            'running_back1_id': self.running_back1_id,
            'running_back2_id': self.running_back2_id,
            'wide_receiver1_id': self.wide_receiver1_id,
            'wide_receiver2_id': self.wide_receiver2_id,
            'tight_end_id': self.tight_end_id,
            'kicker_id': self.kicker_id,
            'defense_id': self.defense_id,
        }
        roster_id = connectToMySQL(db).query_db(query, data)
        self.id = roster_id



    @classmethod
    def save_roster_data(cls, form_data):
        lineup_name = form_data.pop('lineup_name', None)
        if lineup_name:
            form_data['name'] = lineup_name

        # Parse player data from form data
        player_data = {}
        salary_total = 0
        for key, value in form_data.items():
            if isinstance(value, str):
                # Use regular expressions to extract the player name and salary from the input value
                match = re.match(r'^(.+)\s+\(\$([0-9,]+)\)$', value)
                if match:
                    player_name = match.group(1)
                    player_salary = int(match.group(2).replace(',', ''))
                    salary_total += player_salary
                    player_data[key] = {'name': player_name, 'salary': player_salary}
            else:
                pass

        # Get the player ID for each player and add it to the roster data
        roster_data = {
            'user_id': form_data['user_id'],
            'name': form_data['name'],
            'quarterback_id': None,
            'running_back1_id': None,
            'running_back2_id': None,
            'wide_receiver1_id': None,
            'wide_receiver2_id': None,
            'tight_end_id': None,
            'kicker_id': None,
            'defense_id': None,
            # 'salary': salary_total
            'salary': None
        }
        

        for position_name, player_info in player_data.items():
            player_name = player_info['name']
            salary = player_info['salary']

            # Get the player ID from the database
            query = "SELECT id FROM players WHERE name = %(name)s"
            data = {'name': player_name}
            result = connectToMySQL(db).query_db(query, data)
            if not result:
                print(f'No player found with name {player_name}')
            else:
                player_id = int(result[0]['id'])
                player_id = int(player_id) # convert to integer

                # Update the roster data with the player ID for this position
                if position_name in player_positions:
                    roster_data[player_positions[position_name]] = player_id


        # Create a new roster record in the database
        Roster.save(roster_data)


    @classmethod
    def get_by_id(cls,data):
        query = """ SELECT * FROM rosters 
                    JOIN users ON rosters.user_id = users.id
                    JOIN players AS quarterback ON rosters.quarterback_id = quarterback.id
                    JOIN players AS running_back1 ON rosters.running_back1_id = running_back1.id
                    JOIN players AS running_back2 ON rosters.running_back2_id = running_back2.id
                    JOIN players AS wide_receiver1 ON rosters.wide_receiver1_id = wide_receiver1.id
                    JOIN players AS wide_receiver2 ON rosters.wide_receiver2_id = wide_receiver2.id
                    JOIN players AS tight_end ON rosters.tight_end_id = tight_end.id
                    JOIN players AS kicker ON rosters.kicker_id = kicker.id
                    JOIN players AS defense ON rosters.defense_id = defense.id
                    WHERE rosters.id = %(id)s;"""

        result = connectToMySQL(db).query_db(query,data)


        if not result:
            return False
        
        this_roster = cls(result[0])
        salary_list = [
            result[0]['salary'], 
            result[0]['running_back1.salary'], 
            result[0]['running_back2.salary'], 
            result[0]['wide_receiver1.salary'], 
            result[0]['wide_receiver2.salary'], 
            result[0]['tight_end.salary'], 
            result[0]['kicker.salary'], 
            result[0]['defense.salary']
        ]
        
        this_roster.salary_used = sum(salary_list)
        
        return this_roster


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM rosters WHERE id=%(id)s;"
        return connectToMySQL(db).query_db(query,data)