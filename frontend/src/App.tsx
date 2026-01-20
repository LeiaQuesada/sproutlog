import { Routes, Route } from "react-router";
import Layout from "./Layout";
import TasksList from "./TasksList";
import PlantsList from "./PlantsList";
import PlantForm from "./PlantForm";
import PlantDetails from "./PlantDetails.tsx";
import TaskForm from "./TaskForm.tsx";

function App() {
	return (
		<Routes>
			<Route element={<Layout />}>
				<Route index element={<TasksList />} />
				<Route path="/plant/:id/tasks/new" element={<TaskForm />} />
				<Route path="/plant/:id" element={<PlantDetails />} />
				<Route path="/plant" element={<PlantForm />} />
				<Route path="/plants" element={<PlantsList />} />
			</Route>
		</Routes>
	);
}

export default App;
