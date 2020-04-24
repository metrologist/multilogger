# forms.py
from wtforms import Form, StringField, SelectField
from db_setup import db_session
from models import Type, Instrument


# class EleclogSearchForm(Form):
#     choices = [('Description', 'Description'), ('Protocol', 'Protocol')]
#     select = SelectField('Search for instrument type:', choices=choices)
#     search = StringField('')

class EleclogSearchForm(Form):
    choices = [('Description', 'Description'), ('Shortname', 'Shortname'),('instrument_id', 'instrument_id'), ('Status', 'Status')]
    select = SelectField('Search for location:', choices=choices)
    search = StringField('')

class TypeForm(Form):
    protocol_types = [('Ether1', 'Ether1'), ('Ether2', 'Ether2')]
    description = StringField('Description')
    protocol = SelectField('Protocol', choices=protocol_types)


class InstrumentForm(Form):
    qry = db_session.query(Type)
    type_options = []
    for record in qry:
        type_options.append((record.__dict__['id'], record.__dict__['description']))
    status_options = [('Available', 'Available'), ('Maintenance', 'Maintenance'), ('Retired', 'Retired')]
    description = StringField('Description')
    serial = StringField('Serial')
    type_id = SelectField('Type', choices=type_options, coerce=int)
    macaddress = StringField('Macaddress')
    ipaddress = StringField('Ipaddress')
    params = StringField('Params')
    status = SelectField('Status', choices=status_options)


class LocationForm(Form):
    qry = db_session.query(Instrument)
    instrument_options = []
    for record in qry:
        instrument_options.append(
            (record.__dict__['id'], record.__dict__['description'] + ' ' + record.__dict__['serial']))
    status_options = [('Available', 'Available'), ('Maintenance', 'Maintenance'), ('Retired', 'Retired')]
    description = StringField('Description')
    shortname = StringField('Shortname')
    instrument_id = SelectField('Instrument', choices=instrument_options, coerce=int)
    status = SelectField('Status', choices=status_options)
