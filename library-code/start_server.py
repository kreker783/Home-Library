import subprocess

# Run migrations
subprocess.run(["python", "manage.py", "makemigrations"])

# Apply migrations
subprocess.run(["python", "manage.py", "migrate"])

# Start the server
subprocess.run(["python", "manage.py", "runserver", "0.0.0.0:8000"])