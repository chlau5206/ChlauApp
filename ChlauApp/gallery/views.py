""" apps/gallery/views.py
"""
import os
from flask import render_template, redirect, url_for, request, flash, current_app
from werkzeug.utils import secure_filename
from .. import db
from . import gallery_bp, UPLOAD_FOLDER
from .models import Photo, Library
from .forms import DeleteForm, UploadForm

# UPLOAD_FOLDER = os.path.join(gallery_bp.static_folder, 'uploads')

def allowed_file(filename):
    if filename: 
        root, ext = os.path.splitext(filename)
    return ext.casefold() in ('png','jpg', 'jpeg', 'gif', 'img' )

@gallery_bp.route('/')
@gallery_bp.route('/gallery', methods=['GET'])
def index():
    photos = Photo.query.all()
    delete_form = DeleteForm()
    print (gallery_bp.template_folder)
    print (gallery_bp.static_folder)
    return render_template('gallery.html', photos=photos, delete_form=delete_form)

@gallery_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    libraries = Library.query.all()
    form = UploadForm(libraries)
    if form.validate_on_submit():
        photo = form.photo.data
        if photo:
            filename = secure_filename(photo.filename)
            if  allowed_file(filename):
                try: 
                    photo.save(os.path.join(UPLOAD_FOLDER, filename))
                    new_photo = Photo(filename=filename, 
                                      library_id=form.library.data, 
                                      title=form.title.data, 
                                      description=form.description.data)
                    db.session.add(new_photo)
                    db.session.commit()
                    flash(f'File, {filename}, successfully uploaded.', 'success')
                except Exception as e:
                    flash(f'An error occurred during upload: {e}', 'danger')
            else: 
                flash(f'Invalid file, {filename}. \nAllowed image types are -> png, jpg, jpeg, gif', 'warning')
            return redirect(url_for('gallery_bp.index'))
    
    return render_template('upload.html', form=form)


@gallery_bp.route('/delete/<int:photo_id>', methods=['POST'])
def delete(photo_id):
    # removes the Photo record, the file from the filesystem,
    # and update the Library relationship
    photo = Photo.query.get_or_404(photo_id)
    library = photo.library #get the library object

    try:
        os.remove(os.path.join(UPLOAD_FOLDER, photo.filename))
        db.session.delete(photo)
        db.session.commit()
        flash('Photo deleted successfully', 'success')
    except FileNotFoundError:
        db.session.delete(photo)
        db.session.commit()
        flash('Photo database entry deleted, file not found', 'warning')
    except Exception as e:
        flash(f'File upload fail:{e}', 'error')
    return redirect(url_for('gallery_bp.index'))    