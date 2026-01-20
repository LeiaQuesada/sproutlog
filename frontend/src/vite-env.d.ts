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

export interface Task {
	id?: number;
	task_type: string;
	due_at: string;
	completed_at?: string | null;
	plant_id: number;
}

type NewTask = {
	task_type: string;
	due_at: string;
	completed_at: string;
	created_at: string | null;
	plant_id: number;
};

type Gardener = {
	name: string;
};

type NewGardener = {
	id: number;
	name: string;
};

type TaskStatus = "upcoming" | "overdue" | "completed";
