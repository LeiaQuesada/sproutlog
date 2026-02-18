import { Link } from "react-router";

export default function TaskCard({ task }: { task: Task }) {
	let formattedDueAt = "";
	if (task.due_at) {
		const date = new Date(task.due_at);
		if (!isNaN(date.getTime())) {
			formattedDueAt = date.toLocaleString(undefined, {
				year: "numeric",
				month: "short",
				day: "numeric",
				hour: "2-digit",
				minute: "2-digit",
			});
		} else {
			formattedDueAt = task.due_at;
		}
	}
	return (
		<Link to={`/tasks/${task.id}`} className="task">
			<p className="task-title">{task.task_type}</p>
			<p className="task-plant">🌱 {task.plant?.title ?? "Unknown plant"}</p>
			<p className="task-date">{formattedDueAt}</p>
		</Link>
	);
}
