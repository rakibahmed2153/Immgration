from flask import request, current_app
from urllib.parse import urlparse
from src.model.entity.entity import db
import os
import uuid
from datetime import datetime

# ======== Import Dto, Entity ===========
from src.model.entity.login.login import ProfessionalProfile, UsersLoginInformation, OrganizationProfile
from src.model.entity.uploadDocuments.uploadDocuments import UploadDocuments
from src.model.dto.uploadDocuments.uploadDocuments import UploadDocumentsDto, UploadDocumentsDtoList
from src.model.dto.login.login import (ProfessionalProfileDto, ProfessionalProfileDtoList, OrganizationProfileDto,
                                       OrganizationProfileDtoList)
from src.services.sql.queryExecute import dataFetch

professionalProfileDto = ProfessionalProfileDto()
professionalProfileDtoList = ProfessionalProfileDtoList()
professionalProfileDtoListAll = ProfessionalProfileDtoList(many=True)

uploadDocumentsDto = UploadDocumentsDto()
uploadDocumentsDtoList = UploadDocumentsDtoList()
uploadDocumentsDtoListAll = UploadDocumentsDtoList(many=True)

organizationProfileDto = OrganizationProfileDto()
organizationProfileDtoList = OrganizationProfileDtoList()
organizationProfileDtoListAll = OrganizationProfileDtoList(many=True)


def professionDetails(userId):
    try:
        # print('userId', userId)
        and_clause = ["%s = '%s'" % ('ul.id', userId)]
        tableDetails = ("pp.id, pp.first_name, pp.last_name, pp.email, pp.phone, pp.company_legal_name,"
                        " pp.user_type, pp.about, pp.job_position, pp.country, pp.address, pp.twitter_profile,"
                        " pp.facebook_profile, pp.instagram_profile, pp.linkedin_profile, pp.profile_allow"
                        " from professional_profile pp left join users_login ul on ul.user_id=pp.id")
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
        details = dataFetch(sql_query, 'one')
        return details

    except Exception as e:
        print('Immigrant Get Profile', e)


def employeeDetails(userId):
    try:
        # print('userId', userId)
        and_clause = ["%s = '%s'" % ('ul.id', userId)]
        tableDetails = ("pp.id, pp.first_name, pp.last_name, pp.email, pp.phone, pp.company_legal_name,"
                        " pp.user_type, pp.about, pp.job_position, pp.country, pp.address, pp.twitter_profile,"
                        " pp.facebook_profile, pp.instagram_profile, pp.linkedin_profile, pp.profile_allow"
                        " from professional_profile pp left join users_login ul on ul.user_id=pp.id")
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
        details = dataFetch(sql_query, 'all')
        return details

    except Exception as e:
        print('Immigrant Get Profile', e)


def professionDetailsUpdate(data, userId):
    try:
        print('data', userId)
        userId = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', userId)
        db.session.query(ProfessionalProfile).filter_by(id=userId.userId).update({
            'firstName': data['firstName'],
            'lastName': data['lastName'],
            'email': data['email'],
            'phone': data['phone'],
            'companyLegalName': data['companyLegalName'],
            'about': data['about'],
            'jobPosition': data['jobPosition'],
            'country': data['country'],
            'address': data['address'],
            'twitterProfile': data['twitterProfile'],
            'facebookProfile': data['facebookProfile'],
            'instagramProfile': data['instagramProfile'],
            'linkedinProfile': data['linkedinProfile'],
        })
        db.session.commit()
        return {"type": True, "message": "Professional details update successful", "status": "success", "statusCode": 200}

    except Exception as e:
        print('Immigrant Get Profile', e)
        return {"type": False, "message": "Professional details update failed", "status": "failed", "statusCode": 201}


def professionPermissionUpdate(data, userId):
    try:
        print('professionPermissionUpdate', data)
        userId = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', userId)
        db.session.query(ProfessionalProfile).filter_by(id=userId.userId).update({
            'accountChange': data['accountChange'],
            'newService': data['newService'],
            'promoOffer': data['promoOffer'],
        })
        db.session.commit()
        return {"type": True, "message": "Permission update successful", "status": "success", "statusCode": 200}

    except Exception as e:
        print('Immigrant Get Profile', e)
        return {"type": False, "message": "Professional details update failed", "status": "failed", "statusCode": 201}


def allowViewUpdate(data, userId):
    try:
        print('allowViewUpdate', data)
        userId = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', userId)
        db.session.query(ProfessionalProfile).filter_by(id=userId.userId).update({
            'profileAllow': data['profileAllow'],
        })
        db.session.commit()
        return {"type": True, "message": "Allow profile view update successful", "status": "success", "statusCode": 200}

    except Exception as e:
        print('Immigrant Get Profile', e)
        return {"type": False, "message": "Professional details update failed", "status": "failed", "statusCode": 201}


def allowOrgViewUpdate(data, userId):
    try:
        print('allowViewUpdate', data)
        # print('userId ==>', userId)
        userId = UsersLoginInformation.query.filter_by(id=userId).first()
        # print('userId ==>', userId.userId)
        db.session.query(OrganizationProfile).filter_by(userId=userId.userId).update({
            'profileAllow': data['profileAllow'],
        })
        db.session.commit()
        return {"type": True, "message": "Allow profile view update successful", "status": "success", "statusCode": 200}

    except Exception as e:
        print('Immigrant Get Profile', e)
        return {"type": False, "message": "Professional details update failed", "status": "failed", "statusCode": 201}


def uploadDocuments(files, user_id):
    try:
        for file in files:
            document_name = file.filename
            document_type = request.form['document_type']
            document_sub_type = request.form.get('document_sub_type', None)
            content_type = file.content_type or None
            file_url = None
            # print("ContentType", content_type)
            
            # Save the document to the database
            details = saveDocumentToDatabase(user_id, document_name, document_type, document_sub_type, content_type, file_url)

            if not details['type']:
                # If saving to the database fails, return the details immediately
                return details

        return {"type": True, "message": "Document Upload Successful", "status": "success", "statusCode": 200}

    except Exception as e:
        print('uploadDocuments', e)
        return {"type": False, "message": "Document Upload Failed", "status": "failed", "statusCode": 201}



def saveDocumentToDatabase(user_id, document_name, document_type, document_sub_type, content_type, file_url):
    try:
        existing_document = UploadDocuments.query.filter_by(userId=user_id, documentType=document_type).first()

        current_time = datetime.now()

        if existing_document:
            # Delete the existing file before updating the document
            delete_existing_file(existing_document)

            # Update the existing document
            existing_document.documentName = generate_unique_filename(document_name)
            existing_document.documentSubType = document_sub_type if document_sub_type else None
            existing_document.contentType = content_type
            existing_document.fileUrl = file_url if file_url else None
            existing_document.uploadDate = current_time
        else:
            # Save the document to the database
            new_document = UploadDocuments(
                userId=user_id,
                documentName=generate_unique_filename(document_name),
                documentType=document_type,
                documentSubType=document_sub_type,
                contentType=content_type,
                fileUrl=file_url if file_url else None,
                uploadDate=current_time
            )
            db.session.add(new_document)

        db.session.commit()

        return {"type": True, "message": "Document saved to the database", "status": "success", "statusCode": 200}

    except Exception as e:
        print('saveDocumentToDatabase', e)
        return {"type": False, "message": "Error saving document to the database", "status": "failed", "statusCode": 500}

def generate_unique_filename(original_filename):
    # Remove spaces and generate a unique filename using a combination of timestamp and UUID
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4().hex)[:6]  # Use the first 6 characters of the UUID
    filename, extension = os.path.splitext(original_filename)
    filename_without_spaces = filename.replace(' ', '_')
    return f"{filename_without_spaces}_{timestamp}_{unique_id}{extension}"


def delete_existing_file(existing_document):
    try:
        # Extract the filename from the URL in fileUrl
        url_path = urlparse(existing_document.fileUrl).path
        filename = os.path.basename(url_path)

        # Obtain the server base URL dynamically from the request context
        server_base_url = request.url_root.rstrip('/')

        # Remove unwanted prefix from fileUrl
        prefix_to_remove = f'{server_base_url}/api/v1/user/'
        relative_path = existing_document.fileUrl.replace(prefix_to_remove, '')

        # Construct the full file path based on fileUploadPath and the modified fileUrl
        file_path = os.path.join(current_app.config.get('fileUploadPath'), relative_path.lstrip('/'))

        # Check if the file exists before attempting to remove it
        if os.path.exists(file_path):
            # Attempt to remove the file
            try:
                os.remove(file_path)
                print("Existing file deleted from the local folder.")
            except Exception as e:
                print(f"Error deleting existing file: {e}")
        else:
            print("Existing file does not exist.")
    except Exception as e:
        print(f'delete_existing_file: {e}')

def uploadDocumentsDetails(userId):
    try:
        # print('userId', userId)
        details = db.session.query(UploadDocuments).filter_by(userId=userId).all()
        # print("uploadDocumentsDetails", details)
        return details

    except Exception as e:
        print('uploadDocumentsDetails', e)


def save_document_and_get_url(user_id, file, document_type, document_sub_type):
    try:
        # Get the file upload directory from the Flask app configuration
        file_upload_path = current_app.config.get('fileUploadPath')

        if not file_upload_path:
            raise ValueError("File upload path is not configured.")

        # Create the user's folder based on user_id
        user_folder = os.path.join(file_upload_path, str(user_id))
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        # Check if the document type is 'profile_picture' or 'your_story'
        if document_type in ['profile_picture', 'your_story']:
            document_subfolder = document_type
        else:
            document_subfolder = 'other_documents'

        # Create the document type folder within the user's folder
        document_type_folder = os.path.join(user_folder, document_subfolder)
        if not os.path.exists(document_type_folder):
            os.makedirs(document_type_folder)

        # Generate a secure filename based on the original filename
        filename = generate_unique_filename(file.filename)

        # Construct the full path to save the file
        file_path = os.path.join(document_type_folder, filename)

        # Save the file to the specified path
        file.save(file_path)

        # Construct a URL using the Flask route for serving static files
        url = f"{request.url_root}api/v1/user/{user_id}/{document_subfolder}/{filename}"
        print(f"{document_type} for user {user_id} saved successfully at {url}")

        # Call the function to save the document details to the database
        saveDocumentToDatabase(
            user_id=user_id,
            document_name=filename,
            document_type=document_type,
            document_sub_type= document_sub_type if document_sub_type else '', 
            content_type=file.content_type,
            file_url=url
        )

        return {"type": True, "message": f"{document_type} saved successfully", "status": "success", "statusCode": 200}

    except Exception as e:
        print(f'save_document_and_get_url: {e}')
        return {"type": False, "message": f"Error saving {document_type}", "status": "failed", "statusCode": 500}


def deleteFile(id):
    try:
        print('deleteFileId ---->', id)

        # Fetch the file details to delete
        file_to_delete = db.session.query(UploadDocuments).filter_by(id=id).first()

        if file_to_delete:
            # Print the file_to_delete object for inspection
            print("File to delete:", file_to_delete)

            # Extract the filename from the URL in fileUrl
            url_path = urlparse(file_to_delete.fileUrl).path
            filename = os.path.basename(url_path)

            # Obtain the server base URL dynamically from the request context
            server_base_url = request.url_root.rstrip('/')

            # Remove unwanted prefix from fileUrl
            prefix_to_remove = f'{server_base_url}/api/v1/user/'
            relative_path = file_to_delete.fileUrl.replace(prefix_to_remove, '')

            # Construct the full file path based on fileUploadPath and the modified fileUrl
            file_path = os.path.join(current_app.config.get('fileUploadPath'), relative_path.lstrip('/'))

            # Print the file path for debugging
            print("File Path to delete:", file_path)

            # Check if the file exists before attempting to remove it
            if os.path.exists(file_path):
                print("File exists. Deleting...")

                # Attempt to remove the file
                try:
                    os.remove(file_path)
                    print("File deleted from the local folder.")
                except Exception as e:
                    print(f"Error deleting file: {e}")
            else:
                print("File does not exist.")

            # Delete the file object from the session
            db.session.delete(file_to_delete)

            # Commit the changes
            db.session.commit()

            print("File record deleted successfully.")

            return {"statusCode": 200, "message": "File deleted successfully.", "status": "success"}
        else:
            print('File Record not found')
            return {"statusCode": 404, "message": "File record not found.", "status": "failed"}

    except Exception as e:
        print(f'deleteFile: {e}')
        return {"statusCode": 500, "message": "Internal Server Error.", "status": "failed"}
    

def organizationProfileDetails(data, userId):
    try:
        print('data, userId', data, userId)
        userId = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', userId)
        if data['update']:
            db.session.query(OrganizationProfile).filter_by(userId=userId.userId).update({
                'email': data['email'],
                'phone': data['phone'],
                'companyName': data['companyName'],
                'about': data['about'],
                'country': data['country'],
                'address': data['address'],
                'twitterProfile': data['twitterProfile'],
                'facebookProfile': data['facebookProfile'],
                'instagramProfile': data['instagramProfile'],
                'linkedinProfile': data['linkedinProfile'],
            })
            db.session.commit()
            return {"type": True, "message": "Organization details update successfully", "status": "success",
                    "statusCode": 200}
        else:
            myUnimo = OrganizationProfile(
                email=data['email'],
                phone=data['phone'],
                companyName=data['companyName'],
                about=data['about'],
                country=data['country'],
                address=data['address'],
                userId=userId.userId,
                twitterProfile=data['twitterProfile'],
                facebookProfile=data['facebookProfile'],
                instagramProfile=data['instagramProfile'],
                linkedinProfile=data['linkedinProfile'],
            )
            db.session.add(myUnimo)
            db.session.commit()
            result = organizationProfileDto.dump(myUnimo)
            print('Organization details save', result['id'])
            return {"type": True, "message": "Organization details save successfully", "status": "success",
                    "statusCode": 200}

    except Exception as e:
        print('Exception', e)
        return {"type": False, "message": "Organization details save failed. Fill up all the fields",
                "status": "failed", "statusCode": 200}


def organizationDetails(userId):
    try:
        userId = UsersLoginInformation.query.filter_by(id=userId).first()
        print('userId', userId)
        # print('userId', userId)
        and_clause = ["%s = '%s'" % ('user_id', userId.userId)]
        tableDetails = " * from organization_profile "
        and_clause_str = ' AND '.join(and_clause)
        sql_query = 'select ' + tableDetails + ' where ' + and_clause_str
        details = dataFetch(sql_query, 'one')
        return details

    except Exception as e:
        print('Organization Get Profile', e)