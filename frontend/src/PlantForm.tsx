import { useState } from "react";
import { createPlant } from "./sprout-api";
import { Link, useNavigate } from "react-router";

export default function PlantForm() {
	const [error, setError] = useState<string | null>(null);
	const [validationError, setValidationError] = useState<string | null>(null);
	const navigate = useNavigate();

	async function handleSubmit(formData: FormData) {
		const title = formData.get("title") as string | null;
		const description = formData.get("description") as string | null;
		const image_url = formData.get("image_url") as string | null;
		const is_edible = formData.get("is_edible");

		if (!title) {
			setValidationError("Plant title is required");
			return;
		}
		const body = {
			title,
			description,
			image_url,
			is_edible,
			// TODO user creation
			gardener_id: 1,
		};
		const new_plant = await createPlant(body);

		if (!new_plant) {
			setError("Couldn't create a new plant. Try again later");
			return;
		}

		navigate("/");
	}
	if (error) {
		return <p className="error">{error}</p>;
	}
	return (
		<>
			<h1>Add Plant</h1>
			{validationError ? <p>{validationError}</p> : ""}
			<form id="form-create" action={handleSubmit}>
				<div className="field">
					<label htmlFor="title">Title</label>
					<input type="text" name="title" id="title" />
				</div>
				<div className="field">
					<label htmlFor="description">Description</label>
					<input type="text" name="description" id="description" />
				</div>
				<div className="field">
					<label htmlFor="image_link">Image link</label>
					<input type="text" name="image_link" id="image_link" />
				</div>
				<div className="field select">
					<label htmlFor="is_edible">Edible?</label>
					<input type="checkbox" name="is_edible" id="is_edible" />
				</div>
				<div className="form-actions">
					<Link
						to="/plants"
						className="button button-secondary"
						type="reset"
						id="button-cancel"
					>
						Cancel
					</Link>
					<button className="button" type="submit">
						Add new plant
					</button>
				</div>
			</form>
		</>
	);
}

// title: str
// description: str | None = None
// image_url: str | None
// is_edible: bool = False
// gardener_id: int
