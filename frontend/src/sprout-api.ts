const baseURL = "http://localhost:8000/api";

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
