CREATE DATABASE  IF NOT EXISTS `electronaladka`;
USE `electronaladka`;

 CREATE TABLE `employee` (
  `id_employee` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(30) NOT NULL,
  `login` char(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `department_department_id` int(11) NOT NULL,
  `post_id_post` int(11) NOT NULL,
  PRIMARY KEY (`id_employee`,`department_department_id`,`post_id_post`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

 CREATE TABLE `document` (
  `id_doc` int(11) NOT NULL AUTO_INCREMENT,
  `doc_access` int(11) NOT NULL,
  `doc_name` varchar(100) NOT NULL,
  `doc_type` varchar(100) NOT NULL,
  `agreement_date` date ,
  `date_create` date NOT NULL,
  `is_confirmed` int(11) NOT NULL,
  `path` varchar(200) NOT NULL,
  PRIMARY KEY (`id_doc`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

 CREATE TABLE `agreement` (
  `agreement` int(11) NOT NULL AUTO_INCREMENT,
  `agreement_date` date ,
  `document_id_doc` int(11) NOT NULL,
  `employee_id_employee` int(11) NOT NULL ,
  PRIMARY KEY (`agreement`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

 
INSERT INTO  employee(id_employee, name, login, password, department_department_id, post_id_post) VALUES ( DEFAULT, 'Иванов Игорь Степанович', 'dir', 'qwerty', 1, 1);
INSERT INTO  employee(id_employee, name, login, password, department_department_id, post_id_post) VALUES ( DEFAULT, 'Борисова Татьяна Анатольевна', 'cadr', 'qwerty12', 2, 2);
INSERT INTO  employee(id_employee, name, login, password, department_department_id, post_id_post) VALUES ( DEFAULT, 'Жэков Анатолий Геннадиевич', 'secr', 'qwerty123', 1, 3);
INSERT INTO  employee(id_employee, name, login, password, department_department_id, post_id_post) VALUES ( DEFAULT, 'Доманская Анастасия Юрьевна', 'electro', 'qwerty1234', 3, 4);

INSERT INTO  document(id_doc, doc_access, doc_name, doc_type, agreement_date, date_create, is_confirmed, path) VALUES ( DEFAULT, 0, 'Prikaz prikazov', 'prikaz', null, '2018-01-15', 0, 'C:\\Users\\tokens\\Desktop\\new\\Documents');

