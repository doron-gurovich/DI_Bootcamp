from app import app

if __name__ == "__main__":  # Protect this code to be ran if he is imported
	app.run(port=3000, debug=True)
