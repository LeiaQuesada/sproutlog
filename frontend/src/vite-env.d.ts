// global types

type NewPlant = {
	title: string;
	description: string;
	image_url: string;
	is_edible: boolean;
	gardener_id: string;
};

type Plant = {
	id: number;
	title: string;
	description: string;
	image_url: string;
	is_edible: boolean;
	created_at: Date;
	gardener_id: string;
};

type Task = {
	id: number;
	task_type: string;
	due_at: Date;
	completed_at: Date;
	created_at: Date;
	plant_id: number;
};

type Gardener = {
	name: string;
};

type NewGardener = {
	id: number;
	name: string;
};
