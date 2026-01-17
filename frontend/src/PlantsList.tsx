import { Fragment, useEffect, useState } from "react";
import { loadAllPlants } from "./sprout-api.ts";
import { Link } from "react-router";

export default function PlantsList() {
	const [plants, setPlants] = useState<Plant[]>([]);
	const [error, setError] = useState<string | null>(null);

	useEffect(() => {
		loadAllPlants().then((plants) => {
			if (!plants) {
				setError("Couldn't load the list of plants. Try again later");
				return;
			}
			setPlants(plants);
		});
	}, []);
	if (error) {
		return <p className="error">{error}</p>;
	}

	return (
		<>
			<h1>All Plants</h1>
			<div id="all-plants">
				{plants.map((plant) => (
					<Fragment key={plant.id}>
						<Link to={`/plant/${plant.id}`} className="plant" key={plant.id}>
							<div className="plant-title" key={plant.id}>
								{plant.title}
							</div>
							{/* TODO placeholder image needed */}
							<img src={plant.image_url}></img>
							<p>{plant.description}</p>
							<p>{plant.is_edible ? "Edible" : "Not Edible"}</p>
						</Link>
					</Fragment>
				))}
			</div>
		</>
	);
}
