/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{html,js}'],
	theme: {
		fontFamily: {
			custom: ['Raleway', 'sans-serif'],
		},
		extend: {
			colors: {
				blue: 'rgb(2,31,64)',
				red: 'rgb(194, 0, 50)',
				white: 'rgb(240,248,255)',
			},
		},
	},
};
