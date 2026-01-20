import { useEffect, useState } from "react";
import { loadAllTasks } from "./sprout-api";
import getTaskStatus from "./taskStatus";
import TaskCard from "./TaskCard";

export default function TasksList() {
	const [tasks, setTasks] = useState<Task[]>([]);
	const [error, setError] = useState<string | null>(null);

	useEffect(() => {
		loadAllTasks().then((tasks) => {
			if (!tasks) {
				setError("Couldn't load tasks");
				return;
			}
			setTasks(tasks);
		});
	}, []);

	if (error) return <p className="error">{error}</p>;

	const overdueTasks = tasks.filter((t) => getTaskStatus(t) === "overdue");
	const upcomingTasks = tasks.filter((t) => getTaskStatus(t) === "upcoming");
	const completedTasks = tasks.filter((t) => getTaskStatus(t) === "completed");

	return (
		<>
			<h1>Overdue Tasks</h1>
			<div id="all-tasks">
				{overdueTasks.length > 0 ? (
					overdueTasks.map((task) => <TaskCard key={task.id} task={task} />)
				) : (
					<p>No overdue tasks 🎉</p>
				)}
			</div>

			<h1>Upcoming Tasks</h1>
			<div id="all-tasks">
				{upcomingTasks.length > 0 ? (
					upcomingTasks.map((task) => <TaskCard key={task.id} task={task} />)
				) : (
					<p>No upcoming tasks</p>
				)}
			</div>

			<h1>Completed Tasks</h1>
			<div id="all-tasks">
				{completedTasks.length > 0 ? (
					completedTasks.map((task) => <TaskCard key={task.id} task={task} />)
				) : (
					<p>No completed tasks yet</p>
				)}
			</div>
		</>
	);
}
