CREATE TABLE tb_config (
    seq_id SERIAL PRIMARY KEY,
    id_type VARCHAR(70) DEFAULT NULL,
    id_params TEXT DEFAULT NULL,
    status CHAR(1) DEFAULT 'A',
    created_by INTEGER DEFAULT 0,
    created_date TIMESTAMP DEFAULT NULL,
    updated_by INTEGER DEFAULT 0,
    updated_date TIMESTAMP DEFAULT NULL
);

INSERT INTO tb_config (id_type,id_params,created_by,created_date) VALUES ('pan','{"dept_gov_dist":406.1773,"per_pan_dist":73.9256,"father_date_dist":86.885,"date_dob_dist":219.0183,"dept_ratio":4.8421,"govt_ratio":3.0513,"per_ratio":3.2432,"pan_number_ratio":7.0909,"father_ratio":4.96,"date_ratio":1.1132,"dob_ratio":5.3714}',0, NOW());

CREATE TABLE tb_documents (
    document_id SERIAL PRIMARY KEY,
    document_name VARCHAR(70) DEFAULT NULL,
    config_seq_id INTEGER NOT NULL,
    score INTEGER DEFAULT NULL,
    status CHAR(1) DEFAULT 'A',
    created_by INTEGER DEFAULT 0,
    created_date TIMESTAMP DEFAULT NULL,
    updated_by INTEGER DEFAULT 0,
    updated_date TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (config_seq_id) REFERENCES tb_config (seq_id)
);
