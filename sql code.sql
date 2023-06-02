create table customer(
	customer_id int primary key,
	customer_name varchar(50),
    password varchar(50),
    email varchar(50),
    address varchar(50),
    contact varchar(50)
    
);

create table owner(
	owner_id int primary key,
	owner_name varchar(50),
    password varchar(50),
    email varchar(50),
    address varchar(50),
    contact varchar(50)
);

create table venue(
	venue_id int primary key,
    owner_id int,
	venue_name varchar(50),
    email varchar(50),
    address varchar(50),
    contact varchar(50),
    price varchar(50),
    rating varchar(50),
	FOREIGN KEY (owner_id)
    REFERENCES owner(owner_id)
);

create table booking(
	booking_id int primary key,
    customer_id int,
    venue_id int,
    booking_date datetime,
    booking_time datetime,
    checking_date datetime,
    checking_time datetime,
    payment_amount varchar(50),
	FOREIGN KEY (venue_id)
    REFERENCES venue(venue_id),
    FOREIGN KEY (customer_id)
    REFERENCES customer(customer_id)
);

create table admin(
	admin_id int primary key,
    admin_name varchar(50),
    admin_password varchar(50)
);

create table news(
	news_id int primary key,
    title varchar(100),
    venue_id int,
    FOREIGN KEY (venue_id)
    REFERENCES venue(venue_id)
    
);

create table payment(
	payment_id int primary key,
    booking_id int,
    customer_id int,
    payment_date datetime,
    total_amt varchar(50),
    FOREIGN KEY (booking_id)
    REFERENCES booking(booking_id),
    FOREIGN KEY (customer_id)
    REFERENCES customer(customer_id)
);

create table rating(
	rating_id int primary key,
    customer_id int,
    venue_id int,
    rate varchar(50),
    FOREIGN KEY (venue_id)
    REFERENCES venue(venue_id),
    FOREIGN KEY (customer_id)
    REFERENCES customer(customer_id)
);

create table feedback(
	feedback_id int not null primary key auto_increment,
    customer_id int,
	comment varchar(50)
);