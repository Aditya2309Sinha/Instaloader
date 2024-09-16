from flask import Flask, request, render_template, send_file
import instaloader
import os
import zipfile

app = Flask(__name__)

SESSION_FILE = 'instagram-session'

# Function to download Instagram stories
def download_stories(username):
    # Instantiate the Instaloader object
    L = instaloader.Instaloader()

    # Check if the session file exists and load the session
    if os.path.exists(SESSION_FILE):
        print("Loading session from file")
        L.load_session_from_file('your_instagram_username', SESSION_FILE)
    else:
        print("No session file found. Please login manually.")
        return "Session not found. Please login manually."

    # Ensure the 'stories' directory exists
    if not os.path.exists('stories'):
        os.mkdir('stories')

    # Download stories for the given username
    try:
        profile = instaloader.Profile.from_username(L.context, username.strip())
        print(f"Downloading stories for {username}")
        
        for story in L.get_stories(userids=[profile.userid]):
            for item in story.get_items():
                L.download_storyitem(item, f"stories/{username}")
    except Exception as e:
        print(f"Error downloading stories for {username}: {e}")
        return f"Error downloading stories for {username}: {e}"

    # Zip the stories folder
    zipf = zipfile.ZipFile(f'stories_{username}.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(f'stories/{username}'):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.close()

    return f'stories_{username}.zip'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    username = request.form['instagram_username']
    zip_path = download_stories(username)
    
    if "Error" in zip_path:
        return zip_path
    
    return send_file(zip_path, as_attachment=True)


@app.route('/login', methods=['POST'])
def login():
    instagram_username = request.form['instagram_username']
    instagram_password = request.form['instagram_password']
    
    # Instantiate the Instaloader object
    L = instaloader.Instaloader()

    # Log in to Instagram and save the session
    try:
        L.login(instagram_username, instagram_password)
        print("Login successful, saving session.")
        L.save_session_to_file(SESSION_FILE)
        return "Login successful, session saved."
    except instaloader.exceptions.BadCredentialsException:
        return "Invalid login credentials"
    except Exception as e:
        return f"Login failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
