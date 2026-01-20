export default function getTaskStatus(task: Task) {
	if (task.completed_at) return "completed";
	if (new Date(task.due_at) < new Date()) return "overdue";
	return "upcoming";
}
