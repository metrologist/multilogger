# main.py
from app import app
from db_setup import init_db, db_session
from forms import EleclogSearchForm, TypeForm, InstrumentForm, LocationForm
from flask import flash, render_template, request, redirect
from models import Type, Instrument, Location
from tables import Results

init_db()


def save_changes(table_name, base_table, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    if table_name == 'type':
        base_table.description = form.description.data
        base_table.protocol = form.protocol.data
    elif table_name == 'instrument':
        base_table.description = form.description.data
        base_table.serial = form.serial.data
        base_table.type_id = form.type_id.data
        base_table.macaddress = form.macaddress.data
        base_table.ipaddress = form.ipaddress.data
        base_table.params = form.params.data
        base_table.status = form.status.data
    elif table_name == 'location':
        base_table.description = form.description.data
        base_table.shortname = form.shortname.data
        base_table.instrument_id = form.instrument_id.data
        base_table.status = form.status.data

    if new:
        # Add the new type to the database
        db_session.add(base_table)

    # commit the data to the database
    db_session.commit()


#    db_session.close()  # KJ


@app.route('/', methods=['GET', 'POST'])
def index():
    search = EleclogSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


# @app.route('/results')
# def search_results(search):
#     results = []
#     search_string = search.data['search']
#
#     if search_string:
#         if search.data['select'] == 'Description':
#             qry = db_session.query(Type).filter(
#                 Type.description.contains(search_string))
#             results = qry.all()
#         elif search.data['select'] == 'Protocol':
#             qry = db_session.query(Type).filter(
#                 Type.protocol.contains(search_string))
#             results = qry.all()
#         else:
#             qry = db_session.query(Type)
#             results = qry.all()
#     else:
#         qry = db_session.query(Type)
#         results = qry.all()
#
#     if not results:
#         flash('No results found!')
#         return redirect('/')
#     else:
#         # display results
#         table = Results(results)
#         table.border = True
#         return render_template('results.html', table=table)


@app.route('/results')
def search_results(search):
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Description':
            qry = db_session.query(Location).filter(
                Location.description.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Shortname':
            qry = db_session.query(Location).filter(
                Location.shortname.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Instrument_id':
            qry = db_session.query(Location).filter(
                Location.instrument_id.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Status':
            qry = db_session.query(Location).filter(
                Location.status.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Location)
            results = qry.all()
    else:
        qry = db_session.query(Location)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


@app.route('/new_type', methods=['GET', 'POST'])
def new_type():
    """
    Add a new instrument type
    """
    form = TypeForm(request.form)
    if request.method == 'POST' and form.validate():
        # save the type
        save_changes('type', Type(), form, new=True)
        flash('Instrument type created successfully!')
        return redirect('/')

    return render_template('new_type.html', form=form)


@app.route('/new_instrument', methods=['GET', 'POST'])
def new_instrument():
    """
    Add a new instrument
    """
    form = InstrumentForm(request.form)
    if request.method == 'POST' and form.validate():
        # save the instrument
        save_changes('instrument', Instrument(), form, new=True)
        flash('Instrument created successfully!')
        return redirect('/')

    return render_template('new_instrument.html', form=form)

@app.route('/new_location', methods=['GET', 'POST'])
def new_location():
    """
    Add a new location
    """
    form = LocationForm(request.form)
    if request.method == 'POST' and form.validate():
        # save the location
        save_changes('location', Location(), form, new=True)
        flash('Location created successfully!')
        return redirect('/')

    return render_template('new_location.html', form=form)

@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Location).filter(
                Location.id==id)
    location = qry.first()

    if location:
        form = LocationForm(formdata=request.form, obj=location)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes('location', location, form)
            flash('Location updated successfully!')
            return redirect('/')
        return render_template('edit_location.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
#     """
#     Delete the item in the database that matches the specified
#     id in the URL
#     """
#     qry = db_session.query(Album).filter(
#         Album.id==id)
#     album = qry.first()
#
#     if album:
#         form = AlbumForm(formdata=request.form, obj=album)
#         if request.method == 'POST' and form.validate():
#             # delete the item from the database
#             db_session.delete(album)
#             db_session.commit()
#
#             flash('Album deleted successfully!')
# #            db_session.close()  # KJ
#             return redirect('/')
# #        db_session.close()  # KJ
#         return render_template('delete_album.html', form=form)
#     else:
#         db_session.close()  # KJ
        return 'Error deleting #{id}'.format(id=id)

if __name__ == '__main__':
    app.run()
