-- create table for recipe items
CREATE TABLE recipe (
	recipe_name varchar(50),
	description varchar(50),
	serving_size int,
	recipe_type varchar(50),
	time int,
	-- create primary key: ensures no two rows in the table have the same value (the column cannot be NULL for primary key)
	CONSTRAINT recipe_pkey PRIMARY KEY (recipe_name)
);

CREATE TABLE ingredient (
	-- surrogate ID: for more complex systems
	id int GENERATED ALWAYS AS IDENTITY, -- IDENTITY: creates primary key constraint (number value)
	ingredient_name varchar(50),
	amount varchar(50),
	ingredient_type varchar(50),
	recipe varchar(50),
	-- foreign key created to link two tables together; also acts as a constraint, ensuring the values in ingredient have a corresponding value in recipe (not unique)
    CONSTRAINT ingredient_recipe_fkey FOREIGN KEY (recipe) REFERENCES recipe (recipe_name)
);

INSERT INTO Recipe (recipe_name,description,serving_size,recipe_type,time) values ('tomato_pasta', 'italian', 4, 'lunch', 40);
INSERT INTO Recipe (recipe_name,description,serving_size,recipe_type,time) values ('tteokbokki', 'korean', 2, 'dinner', 20);
INSERT INTO Recipe (recipe_name,description,serving_size,recipe_type,time) values ('yaki_udon', 'japanese', 2, 'lunch', 15);
INSERT INTO Recipe (recipe_name,description,serving_size,recipe_type,time) values ('cheese', 'japanese', 2, 'lunch', 15);

INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('pasta', '200g', 'starch', 'tomato_pasta');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('tomato_sauce', '14 ounces', 'sauce', 'tomato_pasta');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('onion', '0.5', 'vegetable', 'tomato_pasta');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('beef', '250g', 'meat', 'tomato_pasta');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('rice_cake', '350g', 'starch', 'tteokbokki');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('fish_cake', '150g', 'protein', 'tteokbokki');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('soup_stock', '2 cups', 'soup', 'tteokbokki');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('gochujang', '3 tbsp', 'sauce', 'tteokbokki');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('onion', '60g', 'vegetable', 'tteokbokki');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('udon', '500g', 'starch', 'yaki_udon');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('cabbage', '1 cup', 'vegetable', 'yaki_udon');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('shrimp', '200g', 'protein', 'yaki_udon');
INSERT INTO Ingredient (ingredient_name,amount,ingredient_type,recipe) values ('mushroom', '60g', 'vegetable', 'yaki_udon');


SELECT
  recipe.*,
  ingredient.*
FROM recipe
FULL OUTER JOIN ingredient ON ingredient.recipe=Recipe.recipe_name;

SELECT COUNT(*), recipe_type
FROM recipe
GROUP BY recipe_type;

-- check how many recipes have the same ingredient type
-- distinct: if a recipe has 2 vegetable ingredients the recipe will only be counted as 1
SELECT ingredient.ingredient_type, COUNT(distinct recipe.recipe_name)
FROM recipe 
JOIN ingredient ON ingredient.recipe=Recipe.recipe_name
GROUP BY ingredient_type; 
