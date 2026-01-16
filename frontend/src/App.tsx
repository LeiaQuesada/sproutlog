import { Routes, Route } from "react-router";
import Layout from "./Layout";
import PlantsList from "./PlantsList";
import PlantForm from "./PlantForm";

function App() {
	return (
		<Routes>
			<Route element={<Layout />}>
				<Route index element={<PlantsList />} />
				<Route path="/plant" element={<PlantForm />} />
				<Route path="/plants" element={<PlantsList />} />
			</Route>
		</Routes>
	);
}

export default App;
