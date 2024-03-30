--------------------------------------------- create
CREATE TABLE person(
  person_id INTEGER     NOT NULL,
  name      VARCHAR(20) NOT NULL,
  surname   VARCHAR(20) NOT NULL,
  CONSTRAINT pk_per_pid PRIMARY KEY (person_id)
);
 
--------------------------------------------- auto increment person_id on INSERT INTO person
CREATE SEQUENCE seq_person_pid
  START WITH 1
  MINVALUE 1
  INCREMENT BY 1
  CACHE 100;
 
CREATE OR REPLACE TRIGGER tri_person_pid
  BEFORE INSERT
  ON person
  FOR EACH ROW
  BEGIN
    SELECT seq_person_pid.nextval
    INTO :new.person_id
    FROM dual;
  END;
/
--------------------------------------------- procedure
CREATE OR REPLACE PROCEDURE p_delete_person(
   p_person_id  IN  person.person_id%TYPE,
   p_error_code OUT NUMBER
)
AS
  BEGIN
    DELETE
    FROM person
    WHERE p_person_id = person.person_id;
 
    p_error_code := SQL%ROWCOUNT;
    IF (p_error_code = 1)
    THEN
      COMMIT;
    ELSE
      ROLLBACK;
    END IF;
    EXCEPTION
    WHEN OTHERS
    THEN
      p_error_code := SQLCODE;
  END p_delete_person;
/