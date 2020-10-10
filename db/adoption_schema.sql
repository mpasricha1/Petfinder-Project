DROP TABLE IF EXISTS animal;
DROP TABLE IF EXISTS breed;
DROP TABLE IF EXISTS color;
DROP TABLE IF EXISTS state;

CREATE TABLE "animal" (
    "id" serial  NOT NULL,
    "type" INT,
    "name" varchar,
    "age" INT,
    "breed1" INT,
    "breed2" INT,
    "gender" INT,
    "color1" INT,
    "color2" INT,
    "color3" INT,
    "maturity_size" INT,
    "furlength" INT,
    "vaccinated" INT,
    "dewormed" INT,
    "sterilized" INT,
    "health" INT,
    "quantity" INT,
    "fee" INT,
    "state_name" INT,
    "rescuer_id" varchar,
    "video_amt" INT,
    "description" varchar,
    "pet_id" varchar,
    "photo_amt" INT,
    "adoption_speed" INT,
	"test_train" varchar,
	"photo1_small" text,
	"photo1_med" text,
	"photo2_small" text,
	"photo2_med" text,
	"status" varchar,
	"housetrained" INT,
	"declawed" INT,
	"good_with_kids" INT,
	"good_with_cats" INT,
	"good_with_dogs" INT,
    CONSTRAINT "pk_animal" PRIMARY KEY (
        "id"
     )
);


CREATE TABLE "breed" (
    "breed_id" INT   NOT NULL,
    "type" INT   NOT NULL,
    "breed_name" varchar   NOT NULL,
	CONSTRAINT "pk_breed" PRIMARY KEY (
    "breed_id"
     )
);

CREATE TABLE "color" (
	"id" INT NOT NULL,
    "color_code" INT   NOT NULL,
    "color_name" varchar   NOT NULL,
	CONSTRAINT "pk_color" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "state" (
    "state_id" INT   NOT NULL,
    "state_name" varchar   NOT NULL,
	CONSTRAINT "pk_state" PRIMARY KEY (
        "state_id"
     )
);

ALTER TABLE "animal" ADD CONSTRAINT "fk_animal_type_breed1" FOREIGN KEY("breed1")
REFERENCES "breed" ("breed_id");

ALTER TABLE "animal" ADD CONSTRAINT "fk_animal_breed2" FOREIGN KEY("breed2")
REFERENCES "breed" ("breed_id");

ALTER TABLE "animal" ADD CONSTRAINT "fk_animal_color1" FOREIGN KEY("color1")
REFERENCES "color" ("id");

ALTER TABLE "animal" ADD CONSTRAINT "fk_animal_color2" FOREIGN KEY("color2")
REFERENCES "color" ("id");

ALTER TABLE "animal" ADD CONSTRAINT "fk_animal_color3" FOREIGN KEY("color3")
REFERENCES "color" ("id");

ALTER TABLE "animal" ADD CONSTRAINT "fk_animal_state" FOREIGN KEY("state_name")
REFERENCES "state" ("state_id");
