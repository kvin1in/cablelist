-- Database: cablelist

-- DROP DATABASE cablelist;

CREATE DATABASE cablelist
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'ru_RU.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE cablelist
    IS 'Кабельный журнал';
