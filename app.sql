drop table if exists employee;
create table employee (
	id_employee text,
	employee_name text,
	gender text,
	date_of_birth date,
	position text,
	handphone text,
	address text,
	start_and_finish_time text,
	total_working_hours time,
	salary text
);

insert into employee (id_employee, employee_name, gender, date_of_birth, position, handphone, address, start_and_finish_time, total_working_hours, salary) 
values
	('1015', 'Givangkara Ozora Ilhamsah', 'Male', '2023-10-01', 'Waiter', 6285780, '["09:00", "17:00"]', '08:00', 'Rp400.000'),
	('1014', 'Naia Diti Sabrina Aurelia','Female', '2023-10-01', 'Waiter', 6285779, '["06:00", "17:00"]', '08:00', 'Rp550,000'),
	('1013', 'Tatia Widya Ningrum', 'Female', '2023-10-01', 'Waiter', 6285778, '["06:00", "17:00"]', '11:00', 'Rp550,000'),
	('1012', 'Ananda Masayu Firda', 'Female', '2023-10-01', 'Waiter', 6285777,	'["07:00", "17:00"]', '10:00', 'Rp500,000'),
	('1011', 'M Aqullah Dana', 'Male', '2023-10-01', 'Waiter', 6285776, '["09:00", "17:00"]', '08:00', 'Rp400,000'),
	('1010', 'Vina Alfita Sari', 'Female', '2023-10-01', 'Waiter', 6285775, '["08:00", "17:00"]', '09:00', 'Rp450,000'),
	('1009', 'Farhan Rasyid Ramadhan', 'Male', '2023-10-01', 'Waiter', 6285774, '["07:00", "17:00"]', '10:00', 'Rp500,000'),
	('1004', 'Jorell Ramos Sinaga', 'Male', '2023-10-01', 'Cashier', 6285769, '["06:00", "17:00"]', '11:00', 'Rp550,000'),
	('1003', 'Ara Dina Mumtaza', 'Female', '2023-10-01', 'Cashier', 6285768, '["07:00", "17:00"]', '10:00', 'Rp500,000'),
	('1002', 'Azzahra Ayungga Sukma', 'Female', '2023-10-01', 'Cheff', 6285767, '["06:00", "17:00"]', '11:00', 'Rp550,000'),
	('1001', 'Aisyah Zayyan Putri', 'Female', '2023-10-01', 'Cheff', 6285766, '["06:00", "17:00"]', '11:00', 'Rp550,000')
	;