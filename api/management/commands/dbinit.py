from django.core.management.base import BaseCommand, CommandError
import os
import sqlite3
import csv

class Command(BaseCommand):
    help = 'populate db with test data'

    def handle(self, *args, **options):

        player_file = os.path.dirname(__file__) + "/../../../data/players.csv"
        team_file = os.path.dirname(__file__) + "/../../../data/teams.csv"
        database_file = "db.sqlite3"

        sql_create_players_table = """ CREATE TABLE IF NOT EXISTS api_player (
                                                player_id integer PRIMARY KEY,
                                                league text,
                                                season text,
                                                stage text,
                                                player text,
                                                team text,
                                                player_GP text,
                                                player_MIN text,
                                                player_FGM text,
                                                player_FGA text,
                                                player_3PM text,
                                                player_3PA text,
                                                player_FTM text,
                                                player_FTA text,
                                                player_TOV text,
                                                player_PF text,
                                                player_ORB text,
                                                player_DRB text,
                                                player_REB text,
                                                player_AST text,
                                                player_STL text,
                                                player_BLK text,
                                                player_PTS text,
                                                birth_year text,
                                                birth_month text,
                                                birth_date text,
                                                height text,
                                                height_cm text,
                                                weight text,
                                                weight_kg text
                                            ); """

        sql_create_teams_table = """ CREATE TABLE IF NOT EXISTS api_team (
                                                team_id integer PRIMARY KEY,
                                                team text,
                                                abbr text
                                            ); """

        # database = '/../../../db.sqlite3'

        conn = sqlite3.connect(database_file)
        c = conn.cursor()
        c.execute(sql_create_players_table)
        c.execute(sql_create_teams_table)
        conn.commit()

        db = sqlite3.connect(database_file)

        with open (player_file, 'r') as f:
            print('Processing players...')
            reader = csv.reader(f)
            columns = next(reader) 
            query = 'insert into api_player({0}) values ({1})'
            query = query.format(','.join(columns), ','.join('?' * len(columns)))
            print(query)
            cursor = db.cursor()
            for data in reader:
                print(data)
                cursor.execute(query, data)
            db.commit()

        with open (team_file, 'r') as f:
            print('Processing teams...')
            reader = csv.reader(f)
            columns = next(reader) 
            query = 'insert into api_team({0}) values ({1})'
            query = query.format(','.join(columns), ','.join('?' * len(columns)))
            print(query)
            cursor = db.cursor()
            for data in reader:
                print(data)
                cursor.execute(query, data)
            db.commit()





