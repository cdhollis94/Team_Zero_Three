"""
List of all the association tables in the database, references within the 
classes they belong to in the association object
"""

# pylint: disable=maybe-no-member

from main_app import db

ing_att_assc = db.Table('ing_att_assc', db.metadata, 
    db.Column('ing_id', db.Integer, db.ForeignKey('ingredients.ing_id')), 
    db.Column('att_id', db.Integer, db.ForeignKey('attributes.att_id')))

ing_rec_assc = db.Table('ing_rec_assc', db.metadata,
    db.Column('ing_id', db.Integer, db.ForeignKey('ingredients.ing_id')),
    db.Column('rec_id', db.Integer, db.ForeignKey('recipes.id'))
)