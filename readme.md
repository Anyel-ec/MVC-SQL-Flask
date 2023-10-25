
# Python MVC Project with SQL Server

This project is a simple example of an MVC (Model-View-Controller) application in Python that utilizes SQL Server as the database. The application displays a list of users stored in the database.

## Requirements

Make sure you have the following packages installed:

- `pyodbc`: For connecting to SQL Server.
- `flask`: For the view layer.

You can install these packages using `pip`:

```bash
pip install pyodbc flask
```

## Database Configuration

1. Create a database in SQL Server.
2. Configure the connection to the database in the `db_config.py` file. Replace the values of `DRIVER`, `SERVER`, `DATABASE`, `UID`, and `PWD` with your server and database information.

## Project Structure

- `db_config.py`: Configuration for connecting to SQL Server.
- `model.py`: Definition of the data model.
- `controller.py`: Controller that interacts with the model and provides data to the view.
- `app.py`: Configuration of the Flask application and route definitions.
- `templates/index.html`: HTML template for displaying the list of users.

## Running the Application

1. Ensure you have configured the database and installed the requirements as mentioned above.
2. Run the Flask application with the following command:

```bash
python app.py
```

The application will be available at `http://localhost:5000/` in your web browser.

## Customization

You can customize this project according to your needs. Add new views, models, or controllers to extend the application's functionality.

## Contributions

If you wish to contribute to this project, feel free to do so! Open a pull request (PR) with your improvements.

## License

This project is distributed under the [MIT License](LICENSE).
