import { Routes, Route } from "react-router";
import Layout from "./Layout";
import PlantsList from "./PlantsList";

function App() {
	return (
		<Routes>
			<Route element={<Layout />}>
				<Route index element={<PlantsList />} />
			</Route>
		</Routes>
	);
}

export default App;
