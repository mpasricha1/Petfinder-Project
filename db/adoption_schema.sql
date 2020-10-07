drop table if exists animal;
drop table if exists breed;
drop table if exists color;
drop table if exists state;


CREATE TABLE "animal" (
    "id" serial  NOT NULL,
    "type" INT   NOT NULL,
    "name" varchar NOT NULL,
    "age" INT   NOT NULL,
    "breed1" INT   NOT NULL,
    "breed2" INT   NOT NULL,
    "gender" INT   NOT NULL,
    "color1" INT   NOT NULL,
    "color2" INT   NOT NULL,
    "color3" INT   NOT NULL,
    "maturity_size" INT   NOT NULL,
    "furlength" INT   NOT NULL,
    "vaccinated" INT   NOT NULL,
    "dewormed" INT   NOT NULL,
    "sterlized" INT   NOT NULL,
    "health" INT   NOT NULL,
    "quantity" INT   NOT NULL,
    "fee" INT   NOT NULL,
    "state" INT   NOT NULL,
    "rescuer_id" varchar   NOT NULL,
    "video_amt" INT   NOT NULL,
    "description" varchar   NOT NULL,
    "pet_id" varchar  NOT NULL,
    "photo_amt" INT   NOT NULL,
    "adoption_speed" INT,
	"test_train" varchar NOT NULL,
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

