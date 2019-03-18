-- User sign up, add user authentication to database
INSERT INTO welcomehome.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$120000$BfmJVD105WeJ$4/8aES7lC4mld/KJQTz4afF7hZWF2LwobueDL6HpgoA=', '', 0, 'usernameX', '', '', '', 0, 0, '2019-03-16 00:40:02.905475');

-- User authentication update, email confirmation
UPDATE welcomehome.auth_user SET password = 'pbkdf2_sha256$120000$BfmJVD105WeJ$4/8aES7lC4mld/KJQTz4afF7hZWF2LwobueDL6HpgoA=', last_login = '2019-03-16 04:03:02.442649', is_superuser = 0, username = 'usernameX', first_name = '', last_name = '', email = '', is_staff = 0, is_active = 1, date_joined = '2019-03-16 00:40:02.905475' WHERE id = 1;

-- User profile creation
INSERT INTO welcomehome.global_listing_userprofile (id, email, phone_day, phone_alt, user_id) VALUES (1, 'oscar@chen.com', '40312345678', null, 1);

-- User profile update
UPDATE welcomehome.global_listing_userprofile SET email = 'oscar@chen.com', phone_day = '40312345678', phone_alt = null, user_id = 1 WHERE id = 1;

-- Property Posting creation
INSERT INTO welcomehome.global_listing_property (property_id, is_active, price, list_date, above_grade_sqft, lot_size, post_title, post_priority, description, is_commercial, business, num_of_buildings, is_residential, residence_type, user_id) VALUES (1, 1, 1000000, '2019-03-10', 1500, 2000, 'Introducing Beautiful Townhouse for a Small Family in Upper East Side', 0, 'This lovely 2 bedroom townhouse is only a few steps away from the Bow River pathway and is nestled among beautiful garden pathways and minutes to downtown, The University of Calgary, and Foothills Hospital.', 0, '', 1, 1, 'Townhouse', 1);

-- Property Posting update
UPDATE welcomehome.global_listing_property SET is_active = 1, price = 1000000, list_date = '2019-03-10', above_grade_sqft = 1500, lot_size = 2000, post_title = 'Introducing Beautiful Townhouse for a Small Family in Upper East Side', post_priority = 0, description = 'This lovely 2 bedroom townhouse is only a few steps away from the Bow River pathway and is nestled among beautiful garden pathways and minutes to downtown, The University of Calgary, and Foothills Hospital.', is_commercial = 0, business = '', num_of_buildings = 1, is_residential = 1, residence_type = 'Townhouse', user_id = 1 WHERE property_id = 1;

-- Property Address creation
INSERT INTO welcomehome.global_listing_propertyaddress (id, street, city, province, postal, property_id_id) VALUES (1, '123 Happy Lane', 'Calgary', 'AB', 'T3R2D4', 1);

-- Property Address update
UPDATE welcomehome.global_listing_propertyaddress SET street = '123 Happy Lane', city = 'Calgary', province = 'AB', postal = 'T3R2D4', property_id_id = 1 WHERE id = 1;

-- Property Image upload
INSERT INTO welcomehome.global_listing_propertyimages (id, image, title, property_id_id) VALUES (1, 'temp/1A.jpg', 'im1', 1);

-- Property Image update
UPDATE welcomehome.global_listing_propertyimages SET title = 'im1', image = 'temp/1A.jpg', property_id_id = 1 WHERE id = 1;

-- Property Room creation
INSERT INTO welcomehome.global_listing_roomspace (id, room_id, name, description, ceiling_heights, is_insulated, num_of_windows, fireplace, size, property_id_id) VALUES (1, 1, 'Kitchen', 'A place to cook', 12, 1, 2, 0, 400, 1);

-- Property Room update
UPDATE welcomehome.global_listing_roomspace SET room_id = 1, name = 'Kitchen', description = 'Kitchen', ceiling_heights = 12, is_insulated = 1, num_of_windows = 2, fireplace = 0, size = 400, property_id_id = 1 WHERE id = 1;

-- Custom room type creation
INSERT INTO welcomehome.global_listing_roomtype (id, room_type, property_id_id, room_id_id) VALUES (1, 'Kitchen2', 1, 2);

-- Room type update
UPDATE welcomehome.global_listing_roomtype SET room_type = 'Kitchen', property_id_id = 1, room_id_id = 1 WHERE id = 1;

-- Room flooring creation
INSERT INTO welcomehome.global_listing_roomflooring (id, flooring, property_id_id, room_id_id) VALUES (1, 'Hard wood', 1, 1);

-- Room flooring update
UPDATE welcomehome.global_listing_roomflooring SET flooring = 'Hard wood', property_id_id = 1, room_id_id = 1 WHERE id = 1;

-- Room dimensions creation
INSERT INTO welcomehome.global_listing_roomdimension (id, dimension, property_id_id, room_id_id) VALUES (1, 20, 1, 1);
INSERT INTO welcomehome.global_listing_roomdimension (id, dimension, property_id_id, room_id_id) VALUES (2, 15, 1, 1);

-- Room dimension update
UPDATE welcomehome.global_listing_roomdimension SET dimension = 20, property_id_id = 1, room_id_id = 1 WHERE id = 1;
UPDATE welcomehome.global_listing_roomdimension SET dimension = 15, property_id_id = 1, room_id_id = 1 WHERE id = 2;