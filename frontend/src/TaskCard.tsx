import { Link } from "react-router";

export default function TaskCard({ task }: { task: Task }) {
	return (
		<Link to={`/tasks/${task.id}`} className="task">
			<p className="task-title">{task.task_type}</p>
			<p className="task-plant">🌱 {task.plant?.title ?? "Unknown plant"}</p>
		</Link>
	);
}
