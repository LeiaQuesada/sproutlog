import { Fragment } from "react/jsx-runtime";
import { useEffect, useState } from "react";
import { loadAllTasks } from "./sprout-api.ts";
import { Link } from "react-router";
import getTaskStatus from "./taskStatus.ts";

export default function TasksList() {
	const [tasks, setTasks] = useState<Task[]>([]);
	const [error, setError] = useState<string | null>(null);
	// const [overdueStatus, setOverdueStatus] = useState(null);
	// const [upcomingStatus, setUpcomingStatus] = useState(null);
	// const [completedStatus, setCompletedStatus] = useState(null);

	useEffect(() => {
		loadAllTasks().then((tasks) => {
			if (!tasks) {
				setError("Couldn't load the list of tasks. Try again later");
				return;
			}
			setTasks(tasks);
		});
	}, []);

	if (error) {
		return <p className="error">{error}</p>;
	}

	const overdueTasks = tasks.filter(
		(task) => getTaskStatus(task) === "overdue"
	);

	const upcomingTasks = tasks.filter(
		(task) => getTaskStatus(task) === "upcoming"
	);

	const completedTasks = tasks.filter(
		(task) => getTaskStatus(task) === "completed"
	);

	return (
		<>
			<h1>Overdue Tasks</h1>
			<div id="all-tasks">
				{overdueTasks.map((task) => (
					<Fragment key={task.id}>
						<Link to={`/tasks/${task.id}`} className="task" key={task.id}>
							<p className="task-title">{task.task_type}</p>
						</Link>
					</Fragment>
				))}
			</div>
			<h1>Upcoming Tasks</h1>
			<div id="all-tasks">
				{upcomingTasks ? (
					upcomingTasks.map((task) => (
						<Fragment key={task.id}>
							<Link to={`/tasks/${task.id}`} className="task" key={task.id}>
								<div className="task-title">{task.task_type}</div>
								<p>{task.task_type}</p>
							</Link>
						</Fragment>
					))
				) : (
					<p>There are no upcoming tasks</p>
				)}
			</div>
			<h1>Completed Tasks</h1>
			<div id="all-tasks">
				{completedTasks.map((task) => (
					<Fragment key={task.id}>
						<Link to={`/tasks/${task.id}`} className="task" key={task.id}>
							<div className="task-title">{task.task_type}</div>
							<p>{task.task_type}</p>
						</Link>
					</Fragment>
				))}
			</div>
		</>
	);
}
