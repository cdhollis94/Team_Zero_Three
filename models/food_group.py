import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from TEAM_ZERO_THREE.app import db

class Food_Group(db.Model):
    __tablename__ = 'food_groups'
    fg_id = db.Column(db.Integer, primary_key=True)
    fg_name = db.Column(db.String(12), unique=True, nullable=False)

    def __repr__(self):
        return '<Food_group %r>' % self.name