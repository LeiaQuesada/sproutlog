const baseURL = "http://localhost:8000";

export async function createGardener(name: Gardener) {
	try {
		const response = await fetch(`${baseURL}/gardener}`, {
			method: "POST",
			body: JSON.stringify(name),
			headers: {
				"Content-Type": "application/json",
			},
		});
		if (!response.ok) {
			throw new Error(`${response.status}`);
		}
		const created_gardener = (await response.json()) as NewGardener;
		return created_gardener;
	} catch (error) {
		console.error("Error occurred while creating gardener", error);
	}
}

export async function loadAllPlants() {
	try {
		const response = await fetch(`${baseURL}/plants`);
		if (!response.ok) {
			throw new Error(`${response.status}`);
		}
		const plants = (await response.json()) as Plant[];
		return plants;
	} catch (error) {
		console.error("error occurred while loading all plants", error);
	}
}

export async function createPlant(plant: NewPlant) {
	try {
		const response = await fetch(`${baseURL}/plant`, {
			method: "POST",
			body: JSON.stringify(plant),
			headers: { "Content-Type": "application/json" },
		});
		if (!response.ok) {
			throw new Error(`${response.status}`);
		}
		const created_plant = await response.json();
		return created_plant;
	} catch (e) {
		console.error(e);
	}
}
