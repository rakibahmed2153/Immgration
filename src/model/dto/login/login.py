from marshmallow import fields
from src.model.dto.dto import ma
import simplejson


class ImmigrantProfileDto(ma.Schema):
    id = fields.String()
    firstName = fields.String(required=True)
    lastName = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    age = fields.Number(required=True)
    countryResidence = fields.String(required=True)
    desireDestination = fields.String(required=True)
    maritalStatus = fields.String(required=True)
    selectedQuestions = fields.String(required=True)
    selectedAnswers = fields.String(required=True)
    familyMembers = fields.Number(allow_none=True)
    referralSource = fields.String(allow_none=True)
    userType = fields.String(required=True)
    profileAllow = fields.Boolean(allow_none=True)
    address = fields.String(allow_none=True)
    about = fields.String(allow_none=True)
    twitterProfile = fields.String(allow_none=True)
    facebookProfile = fields.String(allow_none=True)
    instagramProfile = fields.String(allow_none=True)
    linkedinProfile = fields.String(allow_none=True)


class ImmigrantProfileDtoList(ma.Schema):
    id = fields.String(attribute="id", allow_none=True)
    firstName = fields.String(attribute="first_name", required=True)
    lastName = fields.String(attribute="last_name", required=True)
    email = fields.String(attribute="email", required=True)
    phone = fields.String(attribute="phone", required=True)
    age = fields.Number(attribute="age", required=True)
    countryResidence = fields.String(attribute="country_residence", required=True)
    desireDestination = fields.String(attribute="desire_destination", required=True)
    maritalStatus = fields.String(attribute="marital_status", required=True)
    familyMembers = fields.Number(attribute="family_members", allow_none=True)
    selectedQuestions = fields.String(attribute="selected_questions", required=True)
    selectedAnswers = fields.String(attribute="selected_answers", required=True)
    referralSource = fields.String(attribute="referral_source", allow_none=True)
    userType = fields.String(attribute="user_type", required=True)
    profileAllow = fields.Boolean(attribute="profile_allow", required=True)
    address = fields.String(attribute="address", required=True)
    about = fields.String(attribute="about", required=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    twitterProfile = fields.String(attribute="twitter_profile", allow_none=True)
    facebookProfile = fields.String(attribute="facebook_profile", allow_none=True)
    instagramProfile = fields.String(attribute="instagram_profile", allow_none=True)
    linkedinProfile = fields.String(attribute="linkedin_profile", allow_none=True)

    class Meta:
        json_module = simplejson


class UsersLoginDto(ma.Schema):
    id = fields.String()
    email = fields.String(required=True)
    password = fields.String(required=True)
    userId = fields.String(required=True)
    userType = fields.String(required=True)
    isLooked = fields.Boolean(allow_none=True)
    isActive = fields.Boolean(allow_none=True)
    emailVerified = fields.Boolean(allow_none=True)
    lastLogin = fields.DateTime(allow_none=True)
    attemptTime = fields.DateTime(allow_none=True)
    loginStatus = fields.String(allow_none=True)
    token = fields.String(allow_none=True)
    expirationTime = fields.DateTime(allow_none=True)


class UsersLoginDtoList(ma.Schema):
    id = fields.String(attribute="id", allow_none=True)
    email = fields.String(attribute="email", required=True)
    password = fields.String(attribute="password", required=True)
    userId = fields.String(attribute="user_id", required=True)
    userType = fields.String(attribute="user_type", required=True)
    isLooked = fields.Boolean(attribute="is_looked", allow_none=True)
    isActive = fields.Boolean(attribute="is_active", allow_none=True)
    emailVerified = fields.Boolean(attribute="email_verified", allow_none=True)
    lastLogin = fields.DateTime(attribute="last_login", allow_none=True)
    attemptTime = fields.DateTime(attribute="attempt_time", allow_none=True)
    loginStatus = fields.String(attribute="login_status", allow_none=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    token = fields.String(attribute="token", allow_none=True)
    expirationTime = fields.DateTime(attribute="expiration_time", allow_none=True)

    class Meta:
        json_module = simplejson


class ProfessionalProfileDto(ma.Schema):
    id = fields.String()
    firstName = fields.String(required=True)
    lastName = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    companyLegalName = fields.String(required=True)
    selectedQuestions = fields.String(allow_none=True)
    selectedAnswers = fields.String(allow_none=True)
    userType = fields.String(required=True)
    about = fields.String(allow_none=True)
    jobPosition = fields.String(allow_none=True)
    country = fields.String(allow_none=True)
    address = fields.String(allow_none=True)
    twitterProfile = fields.String(allow_none=True)
    facebookProfile = fields.String(allow_none=True)
    instagramProfile = fields.String(allow_none=True)
    linkedinProfile = fields.String(allow_none=True)
    profileAllow = fields.Boolean(allow_none=True)
    accountChange = fields.Boolean(allow_none=True)
    newService = fields.Boolean(allow_none=True)
    promoOffer = fields.Boolean(allow_none=True)
    securityAlert = fields.Boolean(allow_none=True)
    imagePath = fields.String(allow_none=True)


class ProfessionalProfileDtoList(ma.Schema):
    id = fields.String(attribute="id", allow_none=True)
    firstName = fields.String(attribute="first_name", required=True)
    lastName = fields.String(attribute="last_name", required=True)
    email = fields.String(attribute="email", required=True)
    phone = fields.String(attribute="phone", required=True)
    companyLegalName = fields.String(attribute="company_legal_name", required=True)
    selectedQuestions = fields.String(attribute="selected_questions", required=True)
    selectedAnswers = fields.String(attribute="selected_answers", required=True)
    userType = fields.String(attribute="user_type", required=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    about = fields.String(attribute="about", allow_none=True)
    jobPosition = fields.String(attribute="job_position", allow_none=True)
    country = fields.String(attribute="country", allow_none=True)
    address = fields.String(attribute="address", allow_none=True)
    twitterProfile = fields.String(attribute="twitter_profile", allow_none=True)
    facebookProfile = fields.String(attribute="facebook_profile", allow_none=True)
    instagramProfile = fields.String(attribute="instagram_profile", allow_none=True)
    linkedinProfile = fields.String(attribute="linkedin_profile", allow_none=True)
    profileAllow = fields.Boolean(attribute="profile_allow", allow_none=True)
    accountChange = fields.Boolean(attribute="account_change", allow_none=True)
    newService = fields.Boolean(attribute="new_service", allow_none=True)
    promoOffer = fields.Boolean(attribute="promo_offer", allow_none=True)
    securityAlert = fields.Boolean(attribute="security_alert", allow_none=True)
    imagePath = fields.String(attribute="image_path", allow_none=True)

    class Meta:
        json_module = simplejson


class OrganizationProfileDto(ma.Schema):
    id = fields.String()
    email = fields.String(required=True)
    phone = fields.String(required=True)
    companyName = fields.String(required=True)
    userId = fields.String(required=True)
    about = fields.String(allow_none=True)
    country = fields.String(allow_none=True)
    address = fields.String(allow_none=True)
    twitterProfile = fields.String(allow_none=True)
    facebookProfile = fields.String(allow_none=True)
    instagramProfile = fields.String(allow_none=True)
    linkedinProfile = fields.String(allow_none=True)
    profileAllow = fields.Boolean(allow_none=True)


class OrganizationProfileDtoList(ma.Schema):
    id = fields.String(attribute="id", allow_none=True)
    email = fields.String(attribute="email", required=True)
    phone = fields.String(attribute="phone", required=True)
    companyName = fields.String(attribute="company_name", required=True)
    userId = fields.String(attribute="user_id", required=True)
    createdDate = fields.DateTime(attribute="created_date", allow_none=True)
    about = fields.String(attribute="about", allow_none=True)
    country = fields.String(attribute="country", allow_none=True)
    address = fields.String(attribute="address", allow_none=True)
    twitterProfile = fields.String(attribute="twitter_profile", allow_none=True)
    facebookProfile = fields.String(attribute="facebook_profile", allow_none=True)
    instagramProfile = fields.String(attribute="instagram_profile", allow_none=True)
    linkedinProfile = fields.String(attribute="linkedin_profile", allow_none=True)
    profileAllow = fields.Boolean(attribute="profile_allow", allow_none=True)

    class Meta:
        json_module = simplejson