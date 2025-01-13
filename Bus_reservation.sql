USE busps;
create table bus(
name varchar(50),
bus_no varchar(10) primary key
);
insert into bus
values  ('PRANYA',1),
('LOVELY' ,2),
('VIJESHWAR(green)',3),
('VIJESHWAR(green(s))',4),
('LUCKY',5),
('BLUE LINE',6),
('ANAYA',7),
('VIJESHWAR(blue)',8);

create table timings (
time time,
t_no varchar(30) primary key, 
bus_no varchar(10),
foreign key (bus_no) references bus(bus_no)
);
insert into timings 
values ('07:45:00', 't1', '1'),
('08:10:00', 't2', '2'),
('08:35:00', 't3', '3'),
('08:50:00', 't4', '4'),
('08:50:00', 't5', '5'),
('09:50:00', 't6', '6'),
('10:20:00', 't7', '2'),
('10:40:00', 't8', '7'),
('12:00:00', 't9', '4'),
('12:50:00', 't10', '5');
UPDATE timings
SET t_no = 't10'
WHERE t_no = 't9' AND bus_no = '4';
update timings set t_no='t11' where t_no='t10' and bus_no='5';

INSERT INTO timings (time, t_no, bus_no)
VALUES ('11:00:00', 't9', '8');

SELECT b.bus_no, b.name, t.time
FROM bus b
JOIN timings t ON b.bus_no = t.bus_no
ORDER BY t.time ASC;

create table timings2 (
time_s time,
t_no_s int auto_increment primary key, 
bus_no varchar(10),
foreign key (bus_no) references bus(bus_no)
);
INSERT INTO timings2 (time_s, bus_no)
VALUES 
('08:30:00', '1'),
('08:50:00', '2'),
('09:20:00', '4'),
('10:00:00', '3'),
('10:55:00', '6'),
('11:20:00', '2'),
('11:30:00', '7'),
('12:30:00', '8'),
('01:00:00', '3'),
('01:20:00', '7'),
('01:30:00', '5'),
('02:00:00', '5'),
('02:45:00', '4'),
('03:30:00', '1'),
('04:00:00', '2'),
('04:30:00', '6'),
('05:30:00', '3'),
('05:50:00', '1'),
('06:00:00', '2');

SELECT b.bus_no, b.name, t.time_s
FROM bus b
JOIN timings2 t ON b.bus_no = t.bus_no
ORDER BY t.t_no_s ASC;

create table cond_details (
cond_phone varchar(15) primary key, 
cond_name varchar(64),
d_name varchar(64),
foreign key (bus_no) references bus(bus_no)
);

create table  (
cond_phone varchar(15) primary key, 
cond_name varchar(64),
d_name varchar(64),
foreign key (bus_no) references bus(bus_no)
);

create table destination2 (         #solan to shoolini 
location varchar(64) primary key,
fee varchar(15) 
);
insert into destination2 values
('ZERO POINT', 20),
('LR INSTITUTE', 20),
('JATOLI', 15),
('SHAMTI', 10),
('KIYAR', 20),
('SURYA VIHAR', 10),
('SHOOLINI', 30);

create table destination (
fee varchar(15) primary key, 
locaxn varchar(64)
);
insert into destination values (30,'SOLAN'),  #shoolini to solan
(15,'ZERO POINT'),
(10,'LR INSTITUTE'),
(20,'JATOLI'),
(20,'SHAMTI'),
(10,'KIYAR'),
(25,'SURYA VIHAR');

create table b_status(
seat_status varchar(30) primary key
);
insert into b_status values 
('booked'),
('empty');
select * from b_status;

create table seat_existance(
exist_status varchar(30)
);
insert into seat_existance value ('available'),('not available');
select * from seat_existance;

create table seats(
seat_no varchar(7) primary key
);
insert into seats values
(30), (35),(40);