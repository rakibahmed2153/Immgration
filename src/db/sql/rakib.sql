---------------  Create Queries ---------------
CREATE TABLE lookup_configure
(
    id           VARCHAR (255) PRIMARY KEY,
    lookup_code  VARCHAR (255),
    lookup_name  VARCHAR (500),
    short_name   VARCHAR (500),
    lookup_level VARCHAR (500),
    lookup_note  VARCHAR (1000),
    is_active    BOOLEAN,
    created_date timestamp,
    created_by   VARCHAR (255)
);
alter table lookup_configure  add constraint lookup_configure_pk unique (lookup_code);

CREATE TABLE lookup_data
(
    id               VARCHAR (255) PRIMARY KEY,
    lookup_config_id VARCHAR (255),
    level_id         VARCHAR (500),
    level_data       VARCHAR (500),
    parent_id        VARCHAR (500),
    level_uii        VARCHAR (500),
    level_code       VARCHAR (500),
    lookup_code      VARCHAR (500),
    short_name       VARCHAR (500),
    created_date     timestamp,
    created_by       VARCHAR (255)
);
alter table lookup_data add constraint lookup_data_lookup_configure_id_fk
        foreign key (lookup_config_id) references lookup_configure;
alter table lookup_data add constraint lookup_data_lookup_id_fk
        foreign key (level_id) references lookup_level;

CREATE TABLE lookup_level
(
    id               VARCHAR (255) PRIMARY KEY,
    lookup_config_id VARCHAR (255),
    level_name       VARCHAR (500),
    level_code       VARCHAR (500),
    created_date     timestamp,
    created_by       VARCHAR (255)
);
alter table lookup_level add constraint lookup_data_lookup_configure_id_fk
        foreign key (lookup_config_id) references lookup_configure;

CREATE TABLE immigrant_profile
(
    id                  VARCHAR(255) PRIMARY KEY,
    first_name          VARCHAR(255),
    last_name           VARCHAR(255),
    email               VARCHAR(255),
    phone               VARCHAR(255),
    age                 NUMERIC,
    country_residence   VARCHAR(255),
    desired_destination VARCHAR(255),
    marital_status      VARCHAR(255),
    family_members      NUMERIC,
    referral_source     VARCHAR(255),
    user_type           VARCHAR(255),
    created_date        TIMESTAMP
);
alter table immigrant_profile add column selected_questions VARCHAR(255);
alter table immigrant_profile add column selected_answers VARCHAR(255);
alter table users_login add column email_verified BOOLEAN;
alter table users_login add column token VARCHAR(500);
alter table users_login add column expiration_time TIMESTAMP;

CREATE TABLE users_login
(
    id           VARCHAR(255) PRIMARY KEY,
    email        VARCHAR(255),
    password     VARCHAR(500),
    user_id      VARCHAR(255),
    user_type    VARCHAR(255),
    is_locked    BOOLEAN,
    is_active    BOOLEAN,
    email_verified BOOLEAN,
    last_login   TIMESTAMP,
    attempt_time TIMESTAMP,
    login_status VARCHAR (255),
    token        VARCHAR(500),
    expiration_time TIMESTAMP,
    created_date TIMESTAMP
);

CREATE TABLE error_log
(
    id            VARCHAR(255) PRIMARY KEY,
    functions     VARCHAR(255),
    error_message VARCHAR(255),
    url           VARCHAR(255),
    created_date  TIMESTAMP
);
CREATE TABLE mail_configuration
(
    id            VARCHAR(255) PRIMARY KEY,
    is_active     BOOLEAN,
    sender_email  VARCHAR(255),
    password      VARCHAR(500),
    subject       VARCHAR(255),
    body          TEXT,
    signature     TEXT,
    port          NUMERIC,
    server        VARCHAR(255),
    key           VARCHAR(500),
    mail_for      VARCHAR(255),
    created_by    VARCHAR(255),
    created_date  TIMESTAMP
);

CREATE TABLE professional_profile
(
    id                  VARCHAR(255) PRIMARY KEY,
    first_name          VARCHAR(255),
    last_name           VARCHAR(255),
    email               VARCHAR(255),
    phone               VARCHAR(255),
    company_legal_name   VARCHAR(255),
    selected_questions VARCHAR(255),
    selected_answers      VARCHAR(255),
    user_type           VARCHAR(255),
    created_date        TIMESTAMP
);

alter table professional_profile add column about TEXT;
alter table professional_profile add column job_position VARCHAR(255);
alter table professional_profile add column country VARCHAR(255);
alter table professional_profile add column address VARCHAR(255);
alter table professional_profile add column twitter_profile VARCHAR(255);
alter table professional_profile add column facebook_profile VARCHAR(255);
alter table professional_profile add column instagram_profile VARCHAR(255);
alter table professional_profile add column linkedin_profile VARCHAR(255);
alter table professional_profile add column profile_allow BOOLEAN;

alter table professional_profile add column account_change BOOLEAN;
alter table professional_profile add column new_service BOOLEAN;
alter table professional_profile add column promo_offer BOOLEAN;
alter table professional_profile add column security_alert BOOLEAN;
alter table professional_profile add column image_path VARCHAR(255);

alter table mail_configuration alter column port type integer using port::integer;

CREATE TABLE my_service
(
    id              VARCHAR(255) PRIMARY KEY,
    service         VARCHAR(255),
    category_id     VARCHAR(255),
    sub_category_id VARCHAR(255),
    version         VARCHAR(255),
    user_id         VARCHAR(255),
    created_date    TIMESTAMP
);

CREATE TABLE my_service_details
(
    id              VARCHAR(255) PRIMARY KEY,
    service_id      VARCHAR(255),
    label_name      VARCHAR(255),
    label_details   VARCHAR(255),
    created_date    TIMESTAMP
);
alter table my_service_details add column label_no integer;
alter table my_service_details alter column label_details type text using label_details::text;

-- 17-01-2024
---------------------
CREATE TABLE my_unimo_client_details
(
    id                 VARCHAR(255) PRIMARY KEY,
    my_unimo_no        SERIAL,
    user_id            VARCHAR(255),
    service_name       VARCHAR(255),
    service_id         VARCHAR(255),
    service_steps_id   VARCHAR(255),
    client_email       VARCHAR(255),
    client_portal_link VARCHAR(255),
    request_status     VARCHAR(255),
    customer_status    VARCHAR(255),
    discover_call_date TIMESTAMP,
    created_date       TIMESTAMP
);
alter table my_unimo_client_details add token varchar(500);
alter table mail_configuration add sender_title varchar(255);

-- 18-01-2024
---------------------
INSERT INTO mail_configuration(id, is_active, sender_email, password, subject, body, signature, port, server, created_by, created_date, key, mail_for, sender_title)
VALUES
('1', True,'noreply@immican.ai', 'gAAAAABlixVjrDxMDb3fQYBXgL2NXARn1eOZGFT_8iABdzbVHsmBvb1VFrr7LCHGDWjgSrD7hOdYs-x_RCiAgpZMWWKDwGgn1A==',
 'Registration Confirmation', '', '', 465, 'mail.immican.ai', '', null, 'RtqxhP2tr3VgDNCeiiS3rIu520MJexbYvGBK6rlC298=', 'Registration', 'immiCan');

CREATE TABLE organization_profile
(
    id                  VARCHAR(255) PRIMARY KEY,
    email               VARCHAR(255),
    phone               VARCHAR(255),
    company_name        VARCHAR(255),
    user_id             VARCHAR(255),
    country             VARCHAR(255),
    address             VARCHAR(255),
    about               TEXT,
    twitter_profile     VARCHAR(255),
    facebook_profile    VARCHAR(255),
    instagram_profile   VARCHAR(255),
    linkedin_profile    VARCHAR(255),
    profile_allow       BOOLEAN,
    created_date        TIMESTAMP
);

-- 23-01-2024
alter table my_unimo_client_details add phone varchar(255);
alter table my_unimo_client_details add first_name varchar(255);
alter table my_unimo_client_details add last_name varchar(255);
alter table immigrant_profile add profile_allow boolean;
alter table immigrant_profile add about varchar(500);
alter table immigrant_profile add address varchar(255);
alter table immigrant_profile add column twitter_profile VARCHAR(255);
alter table immigrant_profile add column facebook_profile VARCHAR(255);
alter table immigrant_profile add column instagram_profile VARCHAR(255);
alter table immigrant_profile add column linkedin_profile VARCHAR(255);

-- 24-01-2024
alter table my_unimo_client_details add step_no INTEGER;
alter table my_unimo_client_details add employee_name varchar(255);
-- 08.02.2024
alter table my_unimo_client_details add current_client boolean;
alter table my_unimo_client_details add current_client_status VARCHAR(255);

CREATE TABLE my_unimo_client_details_history
(
    id                 VARCHAR(255) PRIMARY KEY,
    my_unimo_no        SERIAL,
    user_id            VARCHAR(255),
    service_name       VARCHAR(255),
    service_id         VARCHAR(255),
    service_steps_id   VARCHAR(255),
    client_email       VARCHAR(255),
    client_portal_link VARCHAR(255),
    request_status     VARCHAR(255),
    customer_status    VARCHAR(255),
    discover_call_date TIMESTAMP,
    created_date       TIMESTAMP,
    current_client     BOOLEAN,
    current_client_status  VARCHAR(255),
    step_no        INTEGER,
    employee_name  VARCHAR(255),
    phone          VARCHAR(255),
    first_name     VARCHAR(255),
    last_name      VARCHAR(255)
);

-- 14.02.2024
CREATE TABLE policy_details
(
    id              VARCHAR(255) PRIMARY KEY,
    policy_details  TEXT,
    policy_type_id  VARCHAR(255),
    created_by      VARCHAR(255),
    created_date    TIMESTAMP,
    updated_date    TIMESTAMP,
    last_updated_by VARCHAR(255)
);
-- 04-03-2024
alter table my_unimo_client_details add column meeting_link varchar(255);
---------------- Look Up ------------------
-- Destination Country
INSERT INTO lookup_configure(id, lookup_code, lookup_name, short_name, lookup_level, lookup_note, is_active, created_date, created_by)
VALUES
('1','1','Desired Destination', 'Destination', '1', 'Immigrants wants to shift to the place as per our services', true, null, null);

INSERT INTO lookup_level(id, lookup_config_id, level_name, level_code, created_date, created_by)
VALUES
('1','1','Desired Destination', '1', null, null);

INSERT INTO lookup_data(id, lookup_config_id, level_id, level_data, parent_id, level_uii, level_code, lookup_code, short_name, created_date, created_by)
VALUES
('1','1','1', 'Canada', null, '1', '1', '1', '', null, null),
('2','1','1', 'USA (Coming Soon)', null, '2', '1', '1', '', null, null),
('3','1','1', 'UK (Coming Soon)', null, '3', '1', '1', '', null, null),
('4','1','1', 'Australia (Coming Soon)', null, '4', '1', '1', '', null, null);

-- Referral Source
INSERT INTO lookup_configure(id, lookup_code, lookup_name, short_name, lookup_level, lookup_note, is_active, created_date, created_by)
VALUES
('2','2','Referral Source', 'Referral', '1', 'From where you know about immiCan', true, null, null);

INSERT INTO lookup_level(id, lookup_config_id, level_name, level_code, created_date, created_by)
VALUES
('2','2','Source Name', '1', null, null);

INSERT INTO lookup_data(id, lookup_config_id, level_id, level_data, parent_id, level_uii, level_code, lookup_code, short_name, created_date, created_by)
VALUES
('5','2','2', 'LinkedIn', null, '1', '1', '2', '', null, null),
('6','2','2', 'Facebook', null, '2', '1', '2', '', null, null),
('7','2','2', 'Instagram', null, '3', '1', '2', '', null, null),
('8','2','2', 'TikTok', null, '4', '1', '2', '', null, null),
('9','2','2', 'Twitter', null, '5', '1', '2', '', null, null),
('10','2','2', 'Website', null, '6', '1', '2', '', null, null),
('11','2','2', 'Web', null, '7', '1', '2', '', null, null),
('12','2','2', 'Real Life Conversation', null, '8', '1', '2', '', null, null),
('13','2','2', 'Word to Mouth', null, '9', '1', '2', '', null, null),
('14','2','2', 'Other', null, '10', '1', '2', '', null, null);


-- Country Name
INSERT INTO lookup_configure(id, lookup_code, lookup_name, short_name, lookup_level, lookup_note, is_active, created_date, created_by)
VALUES
('3','3','Country Name', 'Country', '1', 'ANme of the countries', true, null, null);

INSERT INTO lookup_level(id, lookup_config_id, level_name, level_code, created_date, created_by)
VALUES
('3','3','Country Name', '1', null, null);

INSERT INTO lookup_data(id, lookup_config_id, level_id, level_data, parent_id, level_uii, level_code, lookup_code, short_name, created_date, created_by)
VALUES
-- ('15','3','3', 'Afghanistan', null, '1', '1', '3', '', null, null),
-- ('16','3','3', 'Albania', null, '2', '1', '3', '', null, null),
-- ('17','3','3', 'Algeria', null, '3', '1', '3', '', null, null),
-- ('18','3','3', 'Andorra', null, '4', '1', '3', '', null, null),
-- ('19','3','3', 'Angola', null, '5', '1', '3', '', null, null),
-- ('20','3','3', 'Antigua and Barbuda', null, '6', '1', '3', '', null, null),
-- ('21','3','3', 'Argentina', null, '7', '1', '3', '', null, null),
-- ('22','3','3', 'Armenia', null, '8', '1', '3', '', null, null),
-- ('23','3','3', 'Australia', null, '9', '1', '3', '', null, null),
-- ('24','3','3', 'Austria', null, '10', '1', '3', '', null, null),
-- ('25','3','3', 'Azerbaijan', null, '11', '1', '3', '', null, null),
-- ('26','3','3', 'Bahamas', null, '12', '1', '3', '', null, null),
-- ('27','3','3', 'Bahrain', null, '13', '1', '3', '', null, null),
-- ('28','3','3', 'Bangladesh', null, '14', '1', '3', '', null, null),
-- ('29','3','3', 'Barbados', null, '15', '1', '3', '', null, null),
-- ('30','3','3', 'Belarus', null, '16', '1', '3', '', null, null),
-- ('31','3','3', 'Belgium', null, '17', '1', '3', '', null, null),
-- ('32','3','3', 'Belize', null, '18', '1', '3', '', null, null),
-- ('33','3','3', 'Benin', null, '19', '1', '3', '', null, null),
-- ('34','3','3', 'Bhutan', null, '20', '1', '3', '', null, null),
-- ('35','3','3', 'Bosnia and Herzegovina', null, '21', '1', '3', '', null, null),
-- ('36','3','3', 'Botswana', null, '22', '1', '3', '', null, null),
-- ('37','3','3', 'Brazil', null, '23', '1', '3', '', null, null),
-- ('38','3','3', 'Brunei', null, '24', '1', '3', '', null, null),
-- ('39','3','3', 'Bulgaria', null, '25', '1', '3', '', null, null),
-- ('40','3','3', 'Burkina Faso', null, '26', '1', '3', '', null, null),
-- ('41','3','3', 'Burundi', null, '27', '1', '3', '', null, null),
-- ('42','3','3', 'Cabo Verde', null, '28', '1', '3', '', null, null),
-- ('43','3','3', 'Cambodia', null, '29', '1', '3', '', null, null),
-- ('44','3','3', 'Cameroon', null, '30', '1', '3', '', null, null),
-- ('45','3','3', 'Canada', null, '31', '1', '3', '', null, null),
-- ('46','3','3', 'Central African Republic', null, '32', '1', '3', '', null, null),
-- ('47','3','3', 'Chad', null, '33', '1', '3', '', null, null),
-- ('48','3','3', 'Chile', null, '34', '1', '3', '', null, null),
-- ('49','3','3', 'Colombia', null, '35', '1', '3', '', null, null),
-- ('50','3','3', 'Comoros', null, '36', '1', '3', '', null, null),
-- ('51','3','3', 'Congo (Congo-Brazzaville)', null, '37', '1', '3', '', null, null),
-- ('52','3','3', 'Costa Rica', null, '38', '1', '3', '', null, null),
-- ('53','3','3', 'Croatia', null, '39', '1', '3', '', null, null),
-- ('54','3','3', 'Cuba', null, '40', '1', '3', '', null, null),
-- ('55','3','3', 'Cyprus', null, '41', '1', '3', '', null, null),
-- ('56','3','3', 'Czechia (Czech Republic)', null, '42', '1', '3', '', null, null);
('57','3','3', 'Democratic Republic of the Congo', null, '43', '1', '3', '', null, null),
('58','3','3', 'Denmark', null, '44', '1', '3', '', null, null),
('59','3','3', 'Djibouti', null, '45', '1', '3', '', null, null),
('60','3','3', 'Dominica', null, '46', '1', '3', '', null, null),
('61','3','3', 'Dominican Republic', null, '47', '1', '3', '', null, null),
('62','3','3', 'Duchy of Parma', null, '48', '1', '3', '', null, null),
('63','3','3', 'Ecuador', null, '49', '1', '3', '', null, null),
('64','3','3', 'Egypt', null, '50', '1', '3', '', null, null),
('65','3','3', 'El Salvador', null, '51', '1', '3', '', null, null),
('66','3','3', 'Equatorial Guinea', null, '52', '1', '3', '', null, null),
('67','3','3', 'Eritrea', null, '53', '1', '3', '', null, null),
('68','3','3', 'Ethiopia', null, '54', '1', '3', '', null, null),
('69','3','3', 'Fiji', null, '55', '1', '3', '', null, null),
('70','3','3', 'Finland', null, '56', '1', '3', '', null, null),
('71','3','3', 'France', null, '57', '1', '3', '', null, null),
('72','3','3', 'Gabon', null, '58', '1', '3', '', null, null),
('73','3','3', 'Gambia', null, '59', '1', '3', '', null, null),
('74','3','3', 'Georgia', null, '60', '1', '3', '', null, null),
('75','3','3', 'Germany', null, '61', '1', '3', '', null, null),
('76','3','3', 'Ghana', null, '62', '1', '3', '', null, null),
('77','3','3', 'Greece', null, '63', '1', '3', '', null, null),
('78','3','3', 'Grenada', null, '64', '1', '3', '', null, null),
('79','3','3', 'Guatemala', null, '65', '1', '3', '', null, null),
('80','3','3', 'Guinea-Bissau', null, '66', '1', '3', '', null, null),
('81','3','3', 'Guyana', null, '67', '1', '3', '', null, null),
('82','3','3', 'Haiti', null, '68', '1', '3', '', null, null),
('83','3','3', 'Hanover', null, '69', '1', '3', '', null, null),
('84','3','3', 'Hanseatic Republics', null, '70', '1', '3', '', null, null),
('85','3','3', 'Hawaii', null, '71', '1', '3', '', null, null),
('86','3','3', 'Hesse', null, '72', '1', '3', '', null, null),
('87','3','3', 'Holy See', null, '73', '1', '3', '', null, null),
('88','3','3', 'Honduras', null, '74', '1', '3', '', null, null),
('89','3','3', 'Hungary', null, '75', '1', '3', '', null, null),
('90','3','3', 'Iceland', null, '76', '1', '3', '', null, null),
('91','3','3', 'India', null, '77', '1', '3', '', null, null),
('92','3','3', 'Indonesia', null, '78', '1', '3', '', null, null),
('93','3','3', 'Iran', null, '79', '1', '3', '', null, null),
('94','3','3', 'Italy', null, '80', '1', '3', '', null, null),
('95','3','3', 'Ireland', null, '81', '1', '3', '', null, null),
('96','3','3', 'Jamaica', null, '82', '1', '3', '', null, null),
('97','3','3', 'Japan', null, '83', '1', '3', '', null, null),
('98','3','3', 'Jordan', null, '84', '1', '3', '', null, null),
('99','3','3', 'Kenya', null, '85', '1', '3', '', null, null),
('100','3','3', 'Korea', null, '86', '1', '3', '', null, null),
('174','3','3', 'Kosovo', null, '87', '1', '3', '', null, null),
('175','3','3', 'Kuwait', null, '88', '1', '3', '', null, null),
('176','3','3', 'Kyrgyzstan', null, '89', '1', '3', '', null, null),
('177','3','3', 'Lebanon', null, '90', '1', '3', '', null, null),
('178','3','3', 'Liberia', null, '91', '1', '3', '', null, null),
('179','3','3', 'Libya', null, '92', '1', '3', '', null, null),
('180','3','3', 'Luxembourg', null, '93', '1', '3', '', null, null),
('181','3','3', 'Malaysia', null, '94', '1', '3', '', null, null),
('182','3','3', 'Maldives', null, '95', '1', '3', '', null, null),
('183','3','3', 'Mexico', null, '96', '1', '3', '', null, null),
('184','3','3', 'Micronesia', null, '97', '1', '3', '', null, null),
('185','3','3', 'Monaco', null, '98', '1', '3', '', null, null),
('186','3','3', 'Mongolia', null, '99', '1', '3', '', null, null),
('187','3','3', 'Morocco', null, '100', '1', '3', '', null, null),
('188','3','3', 'Mozambique', null, '101', '1', '3', '', null, null),
('189','3','3', 'Namibia', null, '102', '1', '3', '', null, null),
('190','3','3', 'Nauru', null, '103', '1', '3', '', null, null),
('191','3','3', 'Nepal', null, '104', '1', '3', '', null, null),
('192','3','3', 'Netherlands', null, '105', '1', '3', '', null, null),
('193','3','3', 'New Zealand', null, '106', '1', '3', '', null, null),
('194','3','3', 'Nigeria', null, '107', '1', '3', '', null, null),
('195','3','3', 'Norway', null, '108', '1', '3', '', null, null),
('196','3','3', 'Oman', null, '109', '1', '3', '', null, null),
('197','3','3', 'Pakistan', null, '110', '1', '3', '', null, null),
('198','3','3', 'Palau', null, '111', '1', '3', '', null, null),
('199','3','3', 'Panama', null, '112', '1', '3', '', null, null),
('200','3','3', 'Paraguay', null, '113', '1', '3', '', null, null),
('201','3','3', 'Peru', null, '114', '1', '3', '', null, null),
('202','3','3', 'Philippines', null, '115', '1', '3', '', null, null),
('203','3','3', 'Poland', null, '116', '1', '3', '', null, null),
('204','3','3', 'Portugal', null, '117', '1', '3', '', null, null),
('205','3','3', 'Qatar', null, '118', '1', '3', '', null, null),
('206','3','3', 'Romania', null, '119', '1', '3', '', null, null),
('207','3','3', 'Russia', null, '120', '1', '3', '', null, null),
('208','3','3', 'Rwanda', null, '121', '1', '3', '', null, null),
('209','3','3', 'Samoa', null, '122', '1', '3', '', null, null),
('210','3','3', 'Saudi Arabia', null, '123', '1', '3', '', null, null),
('211','3','3', 'Serbia', null, '124', '1', '3', '', null, null),
('212','3','3', 'Senegal', null, '125', '1', '3', '', null, null),
('213','3','3', 'Singapore', null, '126', '1', '3', '', null, null),
('214','3','3', 'Somalia', null, '127', '1', '3', '', null, null),
('215','3','3', 'South Africa', null, '128', '1', '3', '', null, null),
('216','3','3', 'Spain', null, '129', '1', '3', '', null, null),
('217','3','3', 'Sri Lanka', null, '130', '1', '3', '', null, null),
('218','3','3', 'Sudan', null, '131', '1', '3', '', null, null),
('219','3','3', 'Sweden', null, '132', '1', '3', '', null, null),
('220','3','3', 'Switzerland', null, '133', '1', '3', '', null, null),
('221','3','3', 'Syria', null, '134', '1', '3', '', null, null),
('222','3','3', 'Texas', null, '135', '1', '3', '', null, null),
('223','3','3', 'Thailand', null, '136', '1', '3', '', null, null),
('224','3','3', 'Togo', null, '137', '1', '3', '', null, null),
('225','3','3', 'Tunisia', null, '138', '1', '3', '', null, null),
('226','3','3', 'Turkey', null, '139', '1', '3', '', null, null),
('227','3','3', 'Tuvalu', null, '140', '1', '3', '', null, null),
('228','3','3', 'Uganda', null, '141', '1', '3', '', null, null),
('229','3','3', 'Ukraine', null, '142', '1', '3', '', null, null),
('230','3','3', 'United Kingdom', null, '143', '1', '3', '', null, null),
('231','3','3', 'Uruguay', null, '144', '1', '3', '', null, null),
('232','3','3', 'Uzbekistan', null, '145', '1', '3', '', null, null),
('233','3','3', 'Vanuatu', null, '146', '1', '3', '', null, null),
('234','3','3', 'Venezuela', null, '147', '1', '3', '', null, null),
('235','3','3', 'Vietnam', null, '148', '1', '3', '', null, null),
('236','3','3', 'Württemberg', null, '149', '1', '3', '', null, null),
('237','3','3', 'Yemen', null, '150', '1', '3', '', null, null),
('238','3','3', 'Zambia', null, '151', '1', '3', '', null, null),
('239','3','3', 'Zimbabwe', null, '152', '1', '3', '', null, null);



-- Registration Type
INSERT INTO lookup_configure(id, lookup_code, lookup_name, short_name, lookup_level, lookup_note, is_active, created_date, created_by)
VALUES
('4','4','Registration Type', 'Regi Type', '1', 'Which type of users are want to register', true, null, null);

INSERT INTO lookup_level(id, lookup_config_id, level_name, level_code, created_date, created_by)
VALUES
('4','4','Registration Type', '1', null, null);

INSERT INTO lookup_data(id, lookup_config_id, level_id, level_data, parent_id, level_uii, level_code, lookup_code, short_name, created_date, created_by)
VALUES
('101','4','4', 'Immigrant', null, '1', '1', '4', '', null, null),
('102','4','4', 'Professional', null, '2', '1', '4', '', null, null);

-- Marital Status
INSERT INTO lookup_configure(id, lookup_code, lookup_name, short_name, lookup_level, lookup_note, is_active, created_date, created_by)
VALUES
('5','5','Marital Status', 'Marital Status', '1', 'Marital Status', true, null, null);

INSERT INTO lookup_level(id, lookup_config_id, level_name, level_code, created_date, created_by)
VALUES
('5','5','Registration Type', '1', null, null);

INSERT INTO lookup_data(id, lookup_config_id, level_id, level_data, parent_id, level_uii, level_code, lookup_code, short_name, created_date, created_by)
VALUES
('103','5','5', 'Single', null, '1', '1', '5', '', null, null),
('104','5','5', 'Married', null, '2', '1', '5', '', null, null);

-- Mail For
INSERT INTO lookup_configure(id, lookup_code, lookup_name, short_name, lookup_level, lookup_note, is_active, created_date, created_by)
VALUES
('7','7','Mail For', 'Mail For', '1', 'For which product this mail is going to configure', true, null, null);

INSERT INTO lookup_level(id, lookup_config_id, level_name, level_code, created_date, created_by)
VALUES
('7','7','Mail For', '1', null, null);

INSERT INTO lookup_data(id, lookup_config_id, level_id, level_data, parent_id, level_uii, level_code, lookup_code, short_name, created_date, created_by)
VALUES
('108','7','7', 'Registration', null, '1', '1', '7', '', null, null);


-- Service Category
INSERT INTO lookup_configure(id, lookup_code, lookup_name, short_name, lookup_level, lookup_note, is_active, created_date, created_by)
VALUES
('8','8','Service Category', 'Service Category', '2', 'For which type of service need to provide', true, null, null);

INSERT INTO lookup_level(id, lookup_config_id, level_name, level_code, created_date, created_by)
VALUES
('8','8','Service Category', '1', null, null),
('9','8','Service Sub Category', '2', null, null);

INSERT INTO lookup_data(id, lookup_config_id, level_id, level_data, parent_id, level_uii, level_code, lookup_code, short_name, created_date, created_by)
VALUES
('109','8','8', 'Visit', null, '1', '1', '8', '', null, null),
('110','8','8', 'Immigrate', null, '2', '1', '8', '', null, null),
('111','8','8', 'Work', null, '3', '1', '8', '', null, null),
('139','8','8', 'Start-up Visa', null, '4', '1', '8', '', null, null),
('112','8','8', 'Study', null, '5', '1', '8', '', null, null),
('113','8','8', 'Citizenship', null, '6', '1', '8', '', null, null),
('114','8','8', 'Sponsorship', null, '7', '1', '8', '', null, null),
('116','8','8', 'Refugees and Asylum', null, '9', '1', '8', '', null, null),
('117','8','8', 'Enforcement and Violations', null, '10', '1', '8', '', null, null),
('118','8','9', 'Visitor Visa', '109', '1', '2', '8', '', null, null),
('119','8','9', 'Business Visa', '109', '2', '2', '8', '', null, null),
('120','8','9', 'Transit Visa', '109', '3', '2', '8', '', null, null),
('121','8','9', 'Visa Extension', '109', '4', '2', '8', '', null, null),
('122','8','9', 'Economic Mobility Pathways', '110', '1', '2', '8', '', null, null),
('123','8','9', 'Francophone', '110', '2', '2', '8', '', null, null),
('129','8','9', 'Express Entry', '110', '3', '2', '8', '', null, null),
('130','8','9', 'Provincial Nominee Program (PNP)', '110', '4', '2', '8', '', null, null),
('131','8','9', 'Quebec-selected skilled workers', '110', '5', '2', '8', '', null, null),
('132','8','9', 'Atlantic Immigration Program', '110', '6', '2', '8', '', null, null),
('133','8','9', 'Rural and Northern Immigration Pilot', '110', '7', '2', '8', '', null, null),
('134','8','9', 'Self-employed', '110', '8', '2', '8', '', null, null),
('135','8','9', 'Agri-Food Pilot', '110', '9', '2', '8', '', null, null),
('136','8','9', 'TR to PR Pathway', '110', '9', '2', '8', '', null, null),
('124','8','9', 'Work Permits', '111', '1', '2', '8', '', null, null),
('125','8','9', 'International Experience Canada', '111', '2', '2', '8', '', null, null),
('126','8','9', 'Caregiver Programs', '111', '3', '2', '8', '', null, null),
('127','8','9', 'Credential Recognition', '111', '4', '2', '8', '', null, null),
('128','8','9', 'Foreign Workers (LMIA)', '111', '5', '2', '8', '', null, null),
('137','8','9', 'Foreign Workers (LMIA Exempt)', '111', '6', '2', '8', '', null, null),
('138','8','9', 'Employer Portal Assistance', '111', '7', '2', '8', '', null, null),
('140','8','9', 'SUV Application', '111', '1', '2', '8', '', null, null),
('141','8','9', 'Support a Business', '139', '2', '2', '8', '', null, null),
('142','8','9', 'Study Permits', '112', '1', '2', '8', '', null, null),
('143','8','9', 'Student Work Permits (PGWP)', '112', '2', '2', '8', '', null, null),
('144','8','9', 'Study Permit Extension', '112', '3', '2', '8', '', null, null),
('145','8','9', 'Applying for Citizenship', '113', '1', '2', '8', '', null, null),
('146','8','9', 'Resuming Citizenship', '113', '2', '2', '8', '', null, null),
('147','8','9', 'Giving up Citizenship', '113', '3', '2', '8', '', null, null),
('148','8','9', 'Permanent Resident Card', '113', '4', '2', '8', '', null, null),
('149','8','9', 'Family Sponsorship', '114', '1', '2', '8', '', null, null),
('150','8','9', 'Refugee Sponsorship', '114', '2', '2', '8', '', null, null),
('151','8','9', 'Travel and Work Abroad', '114', '3', '2', '8', '', null, null),
('152','8','9', 'Adopting a Child from Abroad', '114', '4', '2', '8', '', null, null),
('153','8','9', 'Claiming Refugee Protection', '116', '1', '2', '8', '', null, null),
('154','8','9', 'Sponsoring a Refugee', '116', '2', '2', '8', '', null, null),
('155','8','9', 'Services for Refugees in Canada', '116', '3', '2', '8', '', null, null),
('156','8','9', 'Appealing a Refugee Claim', '116', '4', '2', '8', '', null, null),
('157','8','9', 'Immigration Violations', '117', '1', '2', '8', '', null, null),
('158','8','9', 'Detention Review Process', '117', '2', '2', '8', '', null, null),
('159','8','9', 'Immigration Admissibility Hearings', '117', '3', '2', '8', '', null, null),
('160','8','9', 'Appeal Decision', '117', '4', '2', '8', '', null, null);

-- Policy Type
INSERT INTO lookup_configure(id, lookup_code, lookup_name, short_name, lookup_level, lookup_note, is_active, created_date, created_by)
VALUES
('9','9','Policy Type', 'Policy Type', '1', 'For adding policies', true, null, null);

INSERT INTO lookup_level(id, lookup_config_id, level_name, level_code, created_date, created_by)
VALUES
('10','9','Policy Type', '1', null, null);

INSERT INTO lookup_data(id, lookup_config_id, level_id, level_data, parent_id, level_uii, level_code, lookup_code, short_name, created_date, created_by)
VALUES
('170','9','9', 'Data Processing Addendum (DPA)', null, '1', '1', '9', 'DPA', null, null),
('171','9','9', 'Privacy Policy - EEA, Switzerland and UK', null, '2', '1', '9', 'PP', null, null),
('172','9','9', 'Privacy Policy - Non EEA, Switzerland and UK', null, '3', '1', '9', 'PP-Non EU', null, null),
('173','9','9', 'Terms of use', null, '4', '1', '9', 'TU', null, null);