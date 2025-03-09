import uuid
from src.model.entity.entity import db


def generate_uuid():
    return str(uuid.uuid4())


class ImmigrantProfile(db.Model):

    __tablename__ = 'immigrant_profile'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    firstName = db.Column('first_name', db.String)
    lastName = db.Column('last_name', db.String)
    email = db.Column('email', db.String)
    phone = db.Column('phone', db.String)
    age = db.Column('age', db.Numeric)
    address = db.Column('address', db.String)
    countryResidence = db.Column('country_residence', db.String)
    desiredDestination = db.Column('desired_destination', db.String)
    maritalStatus = db.Column('marital_status', db.String)
    familyMembers = db.Column('family_members', db.Numeric)
    referralSource = db.Column('referral_source', db.String)
    userType = db.Column('user_type', db.String)
    selectedQuestions = db.Column('selected_questions', db.String)
    selectedAnswers = db.Column('selected_answers', db.String)
    profileAllow = db.Column('profile_allow', db.Boolean)
    about = db.Column('about', db.String)
    twitterProfile = db.Column('twitter_profile', db.String)
    facebookProfile = db.Column('facebook_profile', db.String)
    instagramProfile = db.Column('instagram_profile', db.String)
    linkedinProfile = db.Column('linkedin_profile', db.String)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, firstName, lastName, email, phone, age, countryResidence, desiredDestination, maritalStatus,
                 referralSource, userType, selectedQuestions, selectedAnswers, about=None, address=None,
                 familyMembers=False, profileAllow=True, twitterProfile=None, facebookProfile=None,
                 instagramProfile=None, linkedinProfile=None):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.profileAllow = profileAllow
        self.age = age
        self.about = about
        self.address = address
        self.countryResidence = countryResidence
        self.desiredDestination = desiredDestination
        self.maritalStatus = maritalStatus
        self.referralSource = referralSource
        self.userType = userType
        self.selectedQuestions = selectedQuestions
        self.selectedAnswers = selectedAnswers
        self.familyMembers = familyMembers
        self.twitterProfile = twitterProfile
        self.facebookProfile = facebookProfile
        self.instagramProfile = instagramProfile
        self.linkedinProfile = linkedinProfile
        self.createdDate = db.func.current_timestamp()


class UsersLoginInformation(db.Model):

    __tablename__ = 'users_login'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    email = db.Column('email', db.String)
    password = db.Column('password', db.String)
    userId = db.Column('user_id', db.String)
    userType = db.Column('user_type', db.String)
    isLocked = db.Column('is_locked', db.Boolean)
    isActive = db.Column('is_active', db.Boolean)
    lastLogin = db.Column('last_login', db.TIMESTAMP)
    attemptTime = db.Column('attempt_time', db.TIMESTAMP)
    emailVerified = db.Column('email_verified', db.Boolean)
    loginStatus = db.Column('login_status', db.String)
    token = db.Column('token', db.String)
    expirationTime = db.Column('expiration_time', db.TIMESTAMP)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, email, password, userId, userType, isLocked=False, isActive=False, lastLogin=None,
                 attemptTime=None, loginStatus=None, emailVerified=False, token=None, expirationTime=None):
        self.email = email
        self.password = password
        self.userId = userId
        self.userType = userType
        self.isLocked = isLocked
        self.isActive = isActive
        self.lastLogin = lastLogin
        self.attemptTime = attemptTime
        self.emailVerified = emailVerified
        self.token = token
        self.expirationTime = expirationTime
        self.createdDate = db.func.current_timestamp()
        self.loginStatus = loginStatus


class ProfessionalProfile(db.Model):

    __tablename__ = 'professional_profile'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    firstName = db.Column('first_name', db.String)
    lastName = db.Column('last_name', db.String)
    email = db.Column('email', db.String)
    phone = db.Column('phone', db.String)
    companyLegalName = db.Column('company_legal_name', db.String)
    selectedQuestions = db.Column('selected_questions', db.String)
    selectedAnswers = db.Column('selected_answers', db.String)
    userType = db.Column('user_type', db.String)
    about = db.Column('about', db.String)
    jobPosition = db.Column('job_position', db.String)
    country = db.Column('country', db.String)
    address = db.Column('address', db.String)
    twitterProfile = db.Column('twitter_profile', db.String)
    facebookProfile = db.Column('facebook_profile', db.String)
    instagramProfile = db.Column('instagram_profile', db.String)
    linkedinProfile = db.Column('linkedin_profile', db.String)
    profileAllow = db.Column('profile_allow', db.Boolean)
    accountChange = db.Column('account_change', db.Boolean)
    newService = db.Column('new_service', db.Boolean)
    promoOffer = db.Column('promo_offer', db.Boolean)
    securityAlert = db.Column('security_alert', db.Boolean)
    imagePath = db.Column('image_path', db.String)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, firstName, lastName, email, phone, companyLegalName, userType, selectedQuestions=None,
                 selectedAnswers=None, about=None, jobPosition=None, country=None, address=None, profileAllow=True,
                 twitterProfile=None, facebookProfile=None, instagramProfile=None, linkedinProfile=None,
                 accountChange=False, newService=False, promoOffer=False, securityAlert=True, imagePath=None):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.profileAllow = profileAllow
        self.selectedQuestions = selectedQuestions
        self.selectedAnswers = selectedAnswers
        self.companyLegalName = companyLegalName
        self.userType = userType
        self.about = about
        self.jobPosition = jobPosition
        self.country = country
        self.address = address
        self.twitterProfile = twitterProfile
        self.facebookProfile = facebookProfile
        self.instagramProfile = instagramProfile
        self.linkedinProfile = linkedinProfile
        self.accountChange = accountChange
        self.newService = newService
        self.promoOffer = promoOffer
        self.securityAlert = securityAlert
        self.imagePath = imagePath
        self.createdDate = db.func.current_timestamp()


class OrganizationProfile(db.Model):

    __tablename__ = 'organization_profile'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    email = db.Column('email', db.String)
    phone = db.Column('phone', db.String)
    companyName = db.Column('company_name', db.String)
    about = db.Column('about', db.String)
    country = db.Column('country', db.String)
    address = db.Column('address', db.String)
    userId = db.Column('user_id', db.String)
    twitterProfile = db.Column('twitter_profile', db.String)
    facebookProfile = db.Column('facebook_profile', db.String)
    instagramProfile = db.Column('instagram_profile', db.String)
    linkedinProfile = db.Column('linkedin_profile', db.String)
    profileAllow = db.Column('profile_allow', db.Boolean)
    createdDate = db.Column('created_date', db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, email, phone, companyName, userId, about=None, country=None, address=None, profileAllow=True,
                 twitterProfile=None, facebookProfile=None, instagramProfile=None, linkedinProfile=None):
        self.email = email
        self.phone = phone
        self.profileAllow = profileAllow
        self.userId = userId
        self.companyName = companyName
        self.about = about
        self.country = country
        self.address = address
        self.twitterProfile = twitterProfile
        self.facebookProfile = facebookProfile
        self.instagramProfile = instagramProfile
        self.linkedinProfile = linkedinProfile
        self.createdDate = db.func.current_timestamp()

