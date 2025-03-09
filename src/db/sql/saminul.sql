---------------  Create Queries ---------------

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

CREATE TABLE user_documents (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255),
    document_name VARCHAR(255) NOT NULL,
    document_type VARCHAR(255) NOT NULL,
    document_sub_type VARCHAR(255) NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content_type VARCHAR(255) NULL,
    file_url VARCHAR(255) NULL
);

ALTER TABLE "user_documents" ADD COLUMN "file_url" VARCHAR(255) ;

DELETE FROM user_documents;


-- Security Questions
INSERT INTO lookup_configure(id, lookup_code, lookup_name, short_name, lookup_level, lookup_note, is_active, created_date, created_by)
VALUES
('6','6','Security Questions', 'Security Questions', '1', 'Select a security question', true, null, null);

INSERT INTO lookup_level(id, lookup_config_id, level_name, level_code, created_date, created_by)
VALUES
('6','6','Security Questions', '1', null, null);

INSERT INTO lookup_data(id, lookup_config_id, level_id, level_data, parent_id, level_uii, level_code, lookup_code, short_name, created_date, created_by)
VALUES
('105','6','6', 'What is your first name?', null, '1', '1', '6', '', null, null),
('106','6','6', 'What is your last name?', null, '2', '1', '6', '', null, null),
('107','6','6', 'What is your favourite movie?', null, '3', '1', '6', '', null, null);

UPDATE lookup_data
SET level_data = 'What is the name of your beloved pet?'
WHERE id = '105';

UPDATE lookup_data
SET level_data = 'Write down the city where your parents met?'
WHERE id = '106';

