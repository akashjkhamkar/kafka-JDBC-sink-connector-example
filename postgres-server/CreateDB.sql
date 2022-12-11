CREATE TABLE entry (
   ID SERIAL PRIMARY KEY,
   start_time TEXT,
   end_time TEXT,
   category TEXT,
   start_location TEXT,
   end_location TEXT,
   miles TEXT,
   purpose TEXT
);