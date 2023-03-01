from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.player import Player
from flask_app.models.roster import Roster
import re

def check_session():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.get_by_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return user


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    # rosters = Roster.get_all()
    return render_template('dashboard.html', user=user, rosters=Roster.get_all())


@app.route('/lineups/new')
def create_lineup():
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    return render_template('lineup_new.html', user=user, players=Player.get_all())


@app.route('/new/roster', methods=['POST'])
def save_roster_data():
    
    user = check_session()

    # Collect the roster data from the form
    roster_data = {
        'user_id': user.id,
        'name': request.form['name'],
        'quarterback_id': extract_player_id(request.form['quarterback']),
        'running_back1_id': extract_player_id(request.form['running_back1']),
        'running_back2_id': extract_player_id(request.form['running_back2']),
        'wide_receiver1_id': extract_player_id(request.form['wide_receiver1']),
        'wide_receiver2_id': extract_player_id(request.form['wide_receiver2']),
        'tight_end_id': extract_player_id(request.form['tight_end']),
        'kicker_id': extract_player_id(request.form['kicker']),
        'defense_id': extract_player_id(request.form['defense'])
    }
    
    print("roster_data:", roster_data)

    # Save the new roster to the database
    roster = Roster(roster_data)
    roster.save(request.form)

    return redirect('/dashboard')


def extract_player_id(player_input):
    # Use regular expressions to extract the player name from the input string
    player_name = re.search(r'(.+) \(', player_input).group(1)

    # Use the Player model to retrieve the player information, including the player ID
    player = Player.get_by_name({'name': player_name})

    if player:
        return player.id
    else:
        return None



@app.route('/rosters/<int:id>')
def view_lineup(id):
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    roster = Roster.get_by_id({'id': id})
    players = Player.get_players_by_roster_id(id)
    return render_template('lineup_view.html', user=user, roster=roster, players=players)



@app.route('/rosters/edit/<int:id>')
def edit_lineup(id):
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    return render_template('lineup_edit.html', user=user, roster=Roster.get_by_id({'id': id}))

@app.route('/rosters/edit/process/<int:id>', methods=['POST'])
def process_edit_lineup(id):
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    if not validate_lineup_form(request.form):
        return redirect(f'/rosters/edit/{id}')

    data = {
        'id': id,
        'name': request.form['name'],
        'salary_used': request.form['salary_used'],
        'created_at': request.form['created_at'],
    }
    Lineup.update_lineup(data)
    return redirect('/dashboard')

@app.route('/rosters/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    check_session()
    Roster.delete({'id':id})
    return redirect('/dashboard')



