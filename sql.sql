create table user(
	user_id INT PRIMARY KEY AUTO_INCREMENT,
	user_name varchar(50),
    password varchar(50),
    email varchar(50),
    contact varchar(50)
    
);

create table owner(
	owner_id INT PRIMARY KEY AUTO_INCREMENT,
	owner_name varchar(50),
    password varchar(50),
    email varchar(50),
    contact varchar(50)
);

create table venue(
	venue_id INT PRIMARY KEY AUTO_INCREMENT,
    owner_id int,
    image varchar(150),
	venue_name varchar(50),
    email varchar(50),
    location varchar(50),
    contact varchar(50),
    price varchar(50),
    rating int,
    description varchar(100),
	FOREIGN KEY (owner_id) REFERENCES owner(owner_id)
);

create table booking(
	booking_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id int,
    venue_id int,
    booking_date datetime,
    booking_time datetime,
    payment_amount varchar(50),
    rating int,
	FOREIGN KEY (venue_id) REFERENCES venue(venue_id),
    FOREIGN KEY (user_id)REFERENCES user(user_id)
);

create table admin(
	admin_id INT PRIMARY KEY AUTO_INCREMENT,
    admin_name varchar(50),
    admin_password varchar(50)
);

create table news(
	news_id INT PRIMARY KEY AUTO_INCREMENT,
    title varchar(100),
    venue_id int,
    image varchar(150),
    date datetime,
    description varchar(150),
    FOREIGN KEY (venue_id)REFERENCES venue(venue_id)
    
);

create table payment(
	payment_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id int,
    user_id int,
    payment_date datetime,
    total_amt varchar(50),
    FOREIGN KEY (booking_id)REFERENCES booking(booking_id),
    FOREIGN KEY (user_id)REFERENCES user(user_id)
);

create table rating(
	rating_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id int,
    venue_id int,
    rating varchar(50),
    FOREIGN KEY (venue_id)REFERENCES venue(venue_id),
    FOREIGN KEY (user_id)REFERENCES user(user_id)
);

create table feedback(
	feedback_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id int,
	comment varchar(50)
);