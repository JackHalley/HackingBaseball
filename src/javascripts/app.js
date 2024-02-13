// Select the hamburger button and the navigation menu
const hamburgerBtn = document.querySelector(
	'[data-collapse-toggle="navbar-default"]'
);
const navMenu = document.getElementById('navbar-default');

// Add event listener to the hamburger button
hamburgerBtn.addEventListener('click', () => {
	// Toggle the "hidden" class on the navigation menu
	navMenu.classList.toggle('hidden');
});

// footer
document.getElementById('currentYear').innerText = new Date().getFullYear();
