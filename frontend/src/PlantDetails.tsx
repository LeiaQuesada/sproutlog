import { useEffect, useState } from "react";
import { loadPlant } from "./sprout-api.ts";
import { Link, useParams } from "react-router";

export default function PlantDetails() {
	const { id } = useParams();
	const [plant, setPlant] = useState<Plant>();
	const [error, setError] = useState<string | null>(null);

	useEffect(() => {
		if (!id) {
			console.error(`${id} is an invalid plant id`);
			setError("Could not load the plant info");
			return;
		}
		loadPlant(id).then((plant) => {
			if (!plant) {
				setError("Couldn't load the plant. Try again later");
				return;
			}
			setPlant(plant);
		});
	}, []);

	if (error) {
		return <p className="error">{error}</p>;
	}

	if (!plant) {
		return <p>Loading...</p>;
	}

	return (
		<div className="plant-details" key={plant.id}>
			<h1>{plant.title}</h1>
			<p>
				{plant.is_edible ? "Edible" : "Not Edible"} | {plant.description}
			</p>
			<span className="plant-info-card">
				{/* TODO placeholder image needed */}
				<img src={plant.image_url}></img>
				<span className="plant-info-value plant-title-display">
					<Link to={`/plant/${plant.id}/edit`} className="button">
						Edit Plant
					</Link>
					<br />
					<br />
					<Link to={`/plant/${plant.id}/tasks/new`} className="button">
						Add Task
					</Link>
				</span>
			</span>
		</div>
	);
}
