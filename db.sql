-- CREATE TABLE tb_config (
--     seq_id SERIAL PRIMARY KEY,
--     id_type VARCHAR(70) DEFAULT NULL,
--     id_params TEXT DEFAULT NULL,
--     status CHAR(1) DEFAULT 'A',
--     created_by INTEGER DEFAULT 0,
--     created_date TIMESTAMP DEFAULT NULL,
--     updated_by INTEGER DEFAULT 0,
--     updated_date TIMESTAMP DEFAULT NULL
-- );

-- INSERT INTO tb_config (id_type,id_params,created_by,created_date) VALUES
--  ('pan','{"dept_gov_dist":406.1773,"per_pan_dist":73.9256,"father_date_dist":86.885,
--  "date_dob_dist":219.0183,"dept_ratio":4.8421,"govt_ratio":3.0513,"per_ratio":3.2432,
--  "pan_number_ratio":7.0909,"father_ratio":4.96,"date_ratio":1.1132,"dob_ratio":5.3714}',0, NOW());

-- CREATE TABLE tb_documents (
--     document_id SERIAL PRIMARY KEY,
--     document_name VARCHAR(70) DEFAULT NULL,
--     config_seq_id INTEGER NOT NULL,
--     score INTEGER DEFAULT NULL,
--     status CHAR(1) DEFAULT 'A',
--     created_by INTEGER DEFAULT 0,
--     created_date TIMESTAMP DEFAULT NULL,
--     updated_by INTEGER DEFAULT 0,
--     updated_date TIMESTAMP DEFAULT NULL,
--     FOREIGN KEY (config_seq_id) REFERENCES tb_config (seq_id)
-- );

CREATE TABLE tb_config(
    seq_id SERIAL PRIMARY KEY,
    id_type VARCHAR(70) DEFAULT NULL,
    id_version INTEGER DEFAULT 1,
    config_id INTEGER DEFAULT NULL,
    params VARCHAR(1000) DEFAULT NULL,
    params_type VARCHAR(50) DEFAULT 'OCR',
    params_dist NUMERIC(10,4) NOT NULL DEFAULT 0.00,
    params_ratio NUMERIC(10,4) NOT NULL DEFAULT 0.00,
    image_breath NUMERIC(10,4) NOT NULL DEFAULT 0.00,
    image_length NUMERIC(10,4) NOT NULL DEFAULT 0.00, -- 0.4378 b/l 300
    status CHAR(1) DEFAULT 'A',
    created_by INTEGER DEFAULT 0,
    created_date TIMESTAMP DEFAULT NULL,
    updated_by INTEGER DEFAULT 0,
    updated_date TIMESTAMP DEFAULT NULL
);


--- PAN id-version :1
INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio,image_breath,image_length) 
VALUES('PAN',1, 1,'DEPARTMENT',406.1773,4.8421,306,699);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio,image_breath,image_length) 
VALUES('PAN',1, 1,'GOVT.',406.1773,3.0513,306,699);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio,image_breath,image_length) 
VALUES('PAN',1, 1,'Father''s',86.885,4.96,306,699);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio,image_breath,image_length) 
VALUES('PAN',1, 1,'Date',86.885,1.1132,306,699);

--- PAN id-version :2
INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,image_breath,image_length) 
VALUES('PAN',2, 2,'DEPARTMENT',306.1773,316,619);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,image_breath,image_length) 
VALUES('PAN',2, 2,'GOVT.',306.1773,316,619);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,image_breath,image_length) 
VALUES('PAN',2, 2,'Father''s',82.1773,316,619);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,image_breath,image_length) 
VALUES('PAN',2, 2,'Date',84.1773,316,619);

--- AADHAR id-version :1
INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio,image_breath,image_length) 
VALUES('AADHAR',1, 1,'DO',110.0227,1.8148,86,-83);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio,image_breath,image_length) 
VALUES('AADHAR',1, 1,'MALE',110.0227,3.2963,86,-83);

--- AADHAR id-version :2
INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio,image_breath,image_length) 
VALUES('AADHAR',2, 2,'DO',108.0227,2.8148,86,-83);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio,image_breath,image_length) 
VALUES('AADHAR',2, 2,'MALE',108.0227,4.2963,86,-83);


--- Driving id-version :1
INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',1, 1,'issue',534.0459,3.3846);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',1, 1,'Validity',534.0459,3.4615);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',1, 1,'Nationality',257.6354,4.7778);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',1, 1,'Birth',257.6354,2.5455);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',1, 1,'Group',1371.6209,2.7857);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',1, 1,'Fathers',1371.6209,4.5909);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',1, 1,'Endorsement',1300.0215,7.2609);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',1, 1,'Signature',1300.0215,4.6154);

--- Driving id-version :2
INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',2, 2,'issue',530.0459,4.3846);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',2, 2,'Validity',530.0459,4.4615);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',2, 2,'Nationality',250.6354,5.7778);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',2, 2,'Birth',250.6354,5.5455);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',2, 2,'Group',1370.6209,3.7857);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',2, 2,'Fathers',1370.6209,5.5909);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',2, 2,'Endorsement',1301.0215,8.2609);

INSERT INTO tb_config (id_type,id_version,config_id,params,params_dist,params_ratio) 
VALUES('DRIVING',2, 2,'Signature',1300.0215,4.6154);