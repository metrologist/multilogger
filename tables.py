from flask_table import Table, Col, LinkCol

# class Results(Table):
#     id = Col('Id', show=False)
#     description = Col('Description')
#     protocol = Col('Protocol')
    # edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    # delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))

class Results(Table):
    id = Col('Id', show=False)
    description = Col('Description')
    shortname = Col('Shortname')
    instrument_id = Col('Instrument_id')
    status = Col('Status')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))