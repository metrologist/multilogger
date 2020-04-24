# models.py

from app import db

class Type(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    protocol = db.Column(db.String)

    # def __repr__(self):
    #     return "{}".format(self.name)


class Instrument(db.Model):
    __tablename__ = 'instrument'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    serial = db.Column(db.String)
    type_id = db.Column(db.Integer, db.ForeignKey("type.id"))
    type = db.relationship("Type", backref=db.backref(
        "instrument", order_by=id), lazy=True)
    macaddress = db.Column(db.String)
    ipaddress = db.Column(db.String)
    params = db.Column(db.String)
    status = db.Column(db.String)


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    shortname = db.Column(db.String)
    instrument_id = db.Column(db.Integer, db.ForeignKey("instrument.id"))
    instrument = db.relationship("Instrument", backref=db.backref(
        "location", order_by=id), lazy=True)
    status = db.Column(db.String)
