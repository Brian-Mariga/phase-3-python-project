# lib/models/team.py

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import sessionmaker, relationship
from models.__init__ import Base, engine ,session

class Team(Base):

    __tablename__ = 'teams'

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String, nullable = False, unique= True)

    __table_args__ = (UniqueConstraint('team_name', name='unique_team_name'),)

    def add_team(team_name):
        if not team_name:
            print('Team Name required')

        else:
            new_team = Team(team_name = team_name)

            try:
                session.add(new_team)
                session.commit()
                print("Team successfully added")

            except Exception as exc:
                session.rollback()
                print(f'Error adding team: {exc}')

    def get_all_teams():
        if teams := session.query(Team).all():
            for team in teams:
                print(team)
        else:
            print('No teams found')

    def get_team_by_id(team_id):
        if team :=session.query(Team).filter(Team.team_id == team_id).first():
            print(team)
        else:
            print(f'Team of id {team_id} not found.')
        

    def get_team_by_name(team_name):
        if team := session.query(Team).filter(Team.team_name == team_name).first():
            print(team)
        else:
            print(f'Team of team name {team_name} not found.')

    def get_players_of_a_team(team_id):
        pass

    def update_team(team_id):
        pass

    def delete_team(team_id):
        pass