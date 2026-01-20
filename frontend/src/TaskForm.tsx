import { createTask, loadPlant } from "./sprout-api.ts";
import { useState, useEffect } from "react";
import { useNavigate, Link, useParams } from "react-router";

export default function TaskForm() {
	const { id } = useParams();
	const [plant, setPlant] = useState<Plant | null>(null);
	const [error, setError] = useState<string | null>(null);
	const [validationError, setValidationError] = useState<string | null>(null);
	const navigate = useNavigate();

	useEffect(() => {
		if (!id) {
			setError("Invalid plant id");
			return;
		}

		loadPlant(id).then((loadedPlant) => {
			if (!loadedPlant) {
				setError("Unable to load plant");
				return;
			}
			setPlant(loadedPlant);
		});
	}, [id]);

	async function handleSubmit(formData: FormData) {
		const task_type = formData.get("task_type") as string;
		const due_at_raw = formData.get("due_at") as string;

		if (!task_type) {
			setValidationError("Task type required");
			return;
		}

		if (!due_at_raw) {
			setValidationError("Due date required");
			return;
		}

		const body = {
			task_type,
			due_at: new Date(due_at_raw).toISOString(),
			plant_id: Number(id),
		};

		const newTask = await createTask(body);

		if (!newTask) {
			setError("Failed to create task");
			return;
		}

		navigate(`/plant/${id}`);
	}

	if (error) return <p className="error">{error}</p>;
	if (!plant) return <p>Loading...</p>;

	return (
		<>
			<h1>Add Task for {plant.title}</h1>

			{validationError && <p className="error">{validationError}</p>}

			<form
				onSubmit={(e) => {
					e.preventDefault();
					handleSubmit(new FormData(e.currentTarget));
				}}
			>
				<div className="field">
					<label htmlFor="task_type">Task Type</label>
					<input type="text" name="task_type" id="task_type" />
				</div>

				<div className="field">
					<label htmlFor="due_at">Due on</label>
					<input type="datetime-local" name="due_at" id="due_at" />
				</div>

				<button className="button" type="submit">
					Add Task
				</button>
			</form>
		</>
	);
}
