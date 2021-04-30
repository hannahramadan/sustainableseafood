-- --
-- -- PostgreSQL database dump
-- --

-- -- Dumped from database version 9.5.1
-- -- Dumped by pg_dump version 9.5.1

-- SET statement_timeout = 0;
-- SET lock_timeout = 0;
-- SET client_encoding = 'UTF8';
-- SET standard_conforming_strings = on;
-- SET check_function_bodies = false;
-- SET client_min_messages = warning;
-- SET row_security = off;

-- --
-- -- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
-- --

-- CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


-- --
-- -- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
-- --

-- COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


-- SET search_path = public, pg_catalog;

-- SET default_tablespace = '';

-- SET default_with_oids = false;

-- --
-- -- Name: animals; Type: TABLE; Schema: public; Owner: vagrant
-- --

-- CREATE TABLE animals (
--     animal_id integer NOT NULL,
--     human_id integer NOT NULL,
--     name character varying(50) NOT NULL,
--     animal_species character varying(25) NOT NULL,
--     birth_year integer
-- );


-- ALTER TABLE animals OWNER TO "vagrant";

-- --
-- -- Name: animals_animal_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
-- --

-- CREATE SEQUENCE animals_animal_id_seq
--     START WITH 1
--     INCREMENT BY 1
--     NO MINVALUE
--     NO MAXVALUE
--     CACHE 1;


-- ALTER TABLE animals_animal_id_seq OWNER TO "vagrant";

-- --
-- -- Name: animals_animal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
-- --

-- ALTER SEQUENCE animals_animal_id_seq OWNED BY animals.animal_id;


-- --
-- -- Name: humans; Type: TABLE; Schema: public; Owner: vagrant
-- --

-- CREATE TABLE humans (
--     human_id integer NOT NULL,
--     fname character varying(25) NOT NULL,
--     lname character varying(25) NOT NULL,
--     email character varying(100) NOT NULL
-- );


-- ALTER TABLE humans OWNER TO "vagrant";

-- --
-- -- Name: humans_human_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
-- --

-- CREATE SEQUENCE humans_human_id_seq
--     START WITH 1
--     INCREMENT BY 1
--     NO MINVALUE
--     NO MAXVALUE
--     CACHE 1;


-- ALTER TABLE humans_human_id_seq OWNER TO "vagrant";

-- --
-- -- Name: humans_human_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
-- --

-- ALTER SEQUENCE humans_human_id_seq OWNED BY humans.human_id;


-- --
-- -- Name: animal_id; Type: DEFAULT; Schema: public; Owner: vagrant
-- --

-- ALTER TABLE ONLY animals ALTER COLUMN animal_id SET DEFAULT nextval('animals_animal_id_seq'::regclass);


-- --
-- -- Name: human_id; Type: DEFAULT; Schema: public; Owner: vagrant
-- --

-- ALTER TABLE ONLY humans ALTER COLUMN human_id SET DEFAULT nextval('humans_human_id_seq'::regclass);


-- --
-- -- Data for Name: animals; Type: TABLE DATA; Schema: public; Owner: vagrant
-- --

-- COPY animals (animal_id, human_id, name, animal_species, birth_year) FROM stdin;
-- 1	1	Fluffy	cat	2010
-- 2	2	Squiggles	snake	2016
-- 3	3	Fido	dog	2015
-- 4	2	Birdy	bird	2017
-- 5	4	Bubbles	fish	\N
-- 6	2	Mr. Hops	rabbit	\N
-- 7	5	Bugs	rabbit	2016
-- 8	1	Cuddles	cat	\N
-- 9	5	Buster	dog	2011
-- 10	5	Twinkie	dog	2014
-- 11	4	Fluffster	dog	2013
-- 12	1	Twinkles	cat	2014
-- \.


-- --
-- -- Name: animals_animal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
-- --

-- SELECT pg_catalog.setval('animals_animal_id_seq', 12, true);


-- --
-- -- Data for Name: humans; Type: TABLE DATA; Schema: public; Owner: vagrant
-- --

-- COPY humans (human_id, fname, lname, email) FROM stdin;
-- 1	Bob	Personne	bpersonne@yahoo.com
-- 2	Jane	Doe	jdoe@gmail.com
-- 3	Jasmine	Debugger	jdebugs@hotmail.com
-- 4	John	Doer	john_doe@gmail.com
-- 5	Jane	Hacks	jhacks@gmail.com
-- \.


-- --
-- -- Name: humans_human_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
-- --

-- SELECT pg_catalog.setval('humans_human_id_seq', 5, true);


-- --
-- -- Name: animals_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
-- --

-- ALTER TABLE ONLY animals
--     ADD CONSTRAINT animals_pkey PRIMARY KEY (animal_id);


-- --
-- -- Name: humans_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
-- --

-- ALTER TABLE ONLY humans
--     ADD CONSTRAINT humans_pkey PRIMARY KEY (human_id);


-- --
-- -- Name: animals_human_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
-- --

-- ALTER TABLE ONLY animals
--     ADD CONSTRAINT animals_human_id_fkey FOREIGN KEY (human_id) REFERENCES humans(human_id);


-- --
-- -- Name: public; Type: ACL; Schema: -; Owner: postgres
-- --

-- REVOKE ALL ON SCHEMA public FROM PUBLIC;
-- REVOKE ALL ON SCHEMA public FROM postgres;
-- GRANT ALL ON SCHEMA public TO postgres;
-- GRANT ALL ON SCHEMA public TO PUBLIC;


-- --
-- -- PostgreSQL database dump complete
-- --

