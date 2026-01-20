DROP TABLE IF EXISTS plant_care_tasks;
DROP TABLE IF EXISTS plants;
DROP TABLE IF EXISTS gardeners;

CREATE TABLE gardeners (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE plants (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    image_url TEXT,
    is_edible BOOLEAN NOT NULL DEFAULT false,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    gardener_id INTEGER NOT NULL REFERENCES gardeners(id)
);

CREATE TABLE plant_care_tasks (
    id SERIAL PRIMARY KEY,
    task_type TEXT NOT NULL,
    due_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    plant_id INTEGER NOT NULL REFERENCES plants(id) ON DELETE CASCADE
);

INSERT INTO gardeners (name) VALUES ('Leia');

INSERT INTO plants (title, description, image_url, is_edible, gardener_id)
VALUES
    ('Snake Plant', 'Snake Plant', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJ0_U3Ft7kVbmczpA6HiXtXcedCuokk4u6UPQXjiolWWI&s', false, 1), ('Chinese Money Plant', 'Pilea', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdqbboq14Qj5BXeaQNx6ybpFalYmwEGwXPN2igsfW-fztO4kGqONdSJ2_tKCgFf6PIt9dDlwI30x293iHDzCIUQcvYdRdXaCzKWbDmPrOc&s=10', false, 1),
    ('Lavender', 'Apothecary', 'https://www.americanmeadows.com/cdn/shop/files/lavendula-hidcote-lavender_1.jpg?v=1761078910&width=823', true, 1);

INSERT INTO plant_care_tasks (task_type, due_at, completed_at, created_at, plant_id)
VALUES
    ('water', NULL, NULL, DEFAULT, 1), ('water', NULL, NULL, DEFAULT, 2);
