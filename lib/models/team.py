# lib/models/team.py

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import sessionmaker, relationship
from models.__init__ import Base, engine ,session

class Team(Base):

    __tablename__ = 'teams'

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String, nullable = False, unique= True)

    players = relationship("Player", back_populates="team")

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

    @classmethod
    def get_team_name_by_id(cls, team_id):
        team = cls.get_team_by_id(team_id)
        if team:
            return team.team_name
        else:
            return "Unknown"

    def get_all_teams():
        return session.query(Team).all()

    def get_team_by_id(team_id):
        return session.query(Team).filter(Team.team_id == team_id).first()
        

    def get_team_by_name(team_name):
        if team := session.query(Team).filter(Team.team_name == team_name).first():
            print(team)
        else:
            print(f'Team of team name {team_name} not found.')

    def update_team(team_id):
        if team:= Team.get_team_by_id(team_id):
            try:
                new_team_name = input("Enter the new team's name(leave empty to keep current): ")

                if new_team_name:
                    team.team_name = new_team_name

                session.commit()
                print("Team details updated successfully:\n",{team})

            except Exception as exc:
                session.rollback()
                print(f'Error updating team details: {exc}')

        else:
            print(f'Team with id {team_id} not found')

    def delete_team(team_id):
        if team := Team.get_team_by_id(team_id):
            try:
                session.delete(team)
                session.commit()
                print("Successfully deleted player:\n",{team})

            except Exception as exc:
                session.rollback()
                print(f'Error deleting team: {exc}')

        else:
            print(f'Team with id {team_id} not found')