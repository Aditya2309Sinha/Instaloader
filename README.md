Instagram Story Downloader

A personal-use web application built with Flask and Instaloader to download Instagram stories. This tool is intended for individual use and should not be published or used commercially.

Features"
-Login: Authenticate with Instagram and save the session.
-Download Stories: Retrieve stories from any specified Instagram username.
-ZIP Archive: Stories are downloaded and compressed into a ZIP file.

Setup:
-Clone the repository and navigate to the directory.
-Install dependencies using pip (consider using a virtual environment).
-Dependecies include Flask.
-Run the application with python app.py and access it at http://localhost:5000.(here localhost is your ip address)

Usage:
-Login: Enter your Instagram credentials to start the session.
-Download: Input the username and download stories as a ZIP file.

Security Considerations:
-Handle Instagram credentials with care. Avoid exposing sensitive information and ensure the application is not publicly accessible.
-Use environment variables for credentials in production settings.

###Important Notes
-#This tool is for personal use only. Ensure compliance with Instagram's policies and terms of service.
-#The creators are not liable for any misuse or legal issues arising from the use of this application.

#License
            This project is licensed under the MIT License. See the LICENSE file for details.
