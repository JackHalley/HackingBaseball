# HackingBaseball Web App

HackingBaseball is a Flask-based web application for baseball analytics. It allows users to interact with and analyze baseball statistics.

## Features

- Browse baseball statistics by year.
- Filter data based on specific player metrics.
- Visualize player performance on a dashboard.
- Contact the admin team via an integrated contact form.

## Local Setup

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.10 or higher

### Installation

Follow these steps to get your development environment set up:

1. Clone the repository: `git clone https://github.com/<your-github-username>/HackingBaseball.git`
2. Navigate to project directory: `cd HAckingBaseball`
3. Create and activate a python virtual environment: https://realpython.com/python-virtual-environments-a-primer/
5. Install dependencies: `pip install -r requirements.txt`

### Configuration

Create a `.env` file in the root directory of the project with the following content:

  `SECRET_KEY=your_secret_key`
  
  `MAIL_USERNAME=your_email_username`
  
  `MAIL_PASSWORD=your_email_password`

  Replace `your_secret_key`, `your_email_username`, and `your_email_password` with your actual details.

### Running the Application

Run the application using Flask's built-in server: `flask run`
The app will be accessible at `http://127.0.0.1:5000`.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

If you have any questions or comments, please feel free to contact the project maintainers.

---

Remember to replace `<your-github-username>` with your actual GitHub username and fill in your actual email credentials in the `.env` file (but do not commit the `.env` file to your repository).




