import { Outlet, NavLink, Link } from "react-router";

export default function Layout() {
	return (
		<>
			<nav className="navbar">
				<div className="nav-container">
					<Link to="/" className="nav-brand">
						SproutLog App
					</Link>
					<ul className="nav-menu">
						<li className="nav-item">
							<NavLink to="/" className="nav-link">
								All Tasks
							</NavLink>
						</li>
						<li className="nav-item">
							<NavLink to="/plants" className="nav-link">
								All plants
							</NavLink>
						</li>
						<li className="nav-item">
							<NavLink to="/create-plant" className="nav-link">
								Add plant
							</NavLink>
						</li>
					</ul>
				</div>
			</nav>
			<main>
				<Outlet />
			</main>
		</>
	);
}
