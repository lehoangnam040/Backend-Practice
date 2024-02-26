CREATE TABLE flight (
	id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
	dept_airport_id BIGINT,
	dest_airport_id BIGINT,
	total_seat int,
	avail_seat int,
	"version" int DEFAULT 0
);

CREATE TABLE ticket (
	id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
	flight_id UUID
);


insert into flight(dept_airport_id, dest_airport_id, total_seat, avail_seat) values (1, 2, 10000, 10000);