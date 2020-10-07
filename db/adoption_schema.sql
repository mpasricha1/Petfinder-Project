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
    "sterlized" INT,
    "health" INT,
    "quantity" INT,
    "fee" INT,
    "state" INT,
    "rescuer_id" varchar,
    "video_amt" INT,
    "description" varchar,
    "pet_id" varchar,
    "photo_amt" INT,
    "adoption_speed" INT,
	"test_train" varchar,
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
    "color_id" INT   NOT NULL,
    "color_name" varchar   NOT NULL,
	CONSTRAINT "pk_color" PRIMARY KEY (
        "color_id"
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
REFERENCES "color" ("color_id");

ALTER TABLE "animal" ADD CONSTRAINT "fk_animal_color2" FOREIGN KEY("color2")
REFERENCES "color" ("color_id");

ALTER TABLE "animal" ADD CONSTRAINT "fk_animal_color3" FOREIGN KEY("color3")
REFERENCES "color" ("color_id");

ALTER TABLE "animal" ADD CONSTRAINT "fk_animal_state" FOREIGN KEY("state")
REFERENCES "state" ("state_id");