import os
import uuid
from flask import current_app, send_file


def fileUpload(uploaded_files, fileDir):
    for file in uploaded_files:
        if file.filename == '':
            print('No selected file')
            return 'No selected file'
        if file and allowed_profile_file(file.filename):
            filename = str(uuid.uuid4()) + '.png'
            imageDirectoryPath = os.path.join(fileDir + '/' + filename)
            print('filename', filename)
            print('imageDirectoryPath', imageDirectoryPath)

            file.save(os.path.join(current_app.config['fileUploadPath'], imageDirectoryPath))
            return imageDirectoryPath


def sendFile(imagePath):
    try:
        return send_file(os.path.join(current_app.config['fileUploadPath'], imagePath))

    except Exception as e:
        print('Exception sendFile', e)
        return False


def allowed_profile_file(filename):
    allowedExtension = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedExtension
