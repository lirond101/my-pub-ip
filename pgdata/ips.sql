----------------------------------------------------------
-- EMPTY THE DATABASE IN CASE IT CONTAINS CONTENT
----------------------------------------------------------
DROP TRIGGER IF EXISTS audit_trigger ON my_pub_ip.ips;
DROP FUNCTION IF EXISTS auditlogfunc();
DROP TABLE IF EXISTS my_pub_ip.ips_log;
DROP TABLE IF EXISTS my_pub_ip.ips;
DROP SCHEMA IF EXISTS my_pub_ip;

-----------------------------------
-- CREATE THE TABLE STRUCTURE
-----------------------------------

-- Create the database schemas
CREATE SCHEMA my_pub_ip;
SET SCHEMA 'my_pub_ip';
-- On psql:
-- SET search_path TO my_pub_ip;

-- Create a table for the Two Trees category data
-- CREATE TABLE my_pub_ip.ips (
--     ip_id         VARCHAR(100) PRIMARY KEY,
--     read_time     TIME,
--     ip_address    VARCHAR(15) NOT NULL
-- );

CREATE TABLE my_pub_ip.ips_read_log(
    read_id              INT PRIMARY KEY,
    read_time            TIMESTAMP,
    ip_address           VARCHAR(100)
    -- CONSTRAINT FK_log_ips FOREIGN KEY(ip_id)
        -- REFERENCES ips(ip_id)
);
CREATE SEQUENCE read_id_seq OWNED BY my_pub_ip.ips_read_log.read_id;
ALTER TABLE my_pub_ip.ips_read_log ALTER COLUMN read_id SET DEFAULT nextval('read_id_seq');

-- CREATE OR REPLACE FUNCTION auditlogfunc() RETURNS TRIGGER AS $example_table$
--    BEGIN
--       INSERT INTO my_pub_ip.ips_log(run_time, ip_id) VALUES (NOW(), new.ip_id);
--       RETURN NEW;
--    END;
-- $example_table$ LANGUAGE plpgsql;

-- CREATE TRIGGER audit_trigger AFTER INSERT ON my_pub_ip.ips FOR EACH ROW EXECUTE PROCEDURE auditlogfunc();

-- INSERT INTO my_pub_ip.ips (ip_id, read_time, ip_address) VALUES ('test_id', NOW(), '123.123.123.123');
-- select * from my_pub_ip.ips_log;
-- select * from my_pub_ip.ips;
