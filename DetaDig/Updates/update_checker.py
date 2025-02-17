import subprocess

def check_for_updates():
    """
    Check if the local repository is up to date with the remote repository.
    If not, update it using git pull.
    """
    print("Checking for updates...")
    try:
        # Check the status of the git repo
        result = subprocess.run(['git', 'status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if "Your branch is up to date" not in result.stdout:
            print("The repository is not up to date. Pulling the latest changes...")
            # If the repo is outdated, pull the latest changes
            update_result = subprocess.run(['git', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if update_result.returncode == 0:
                print("Repository updated successfully.")
            else:
                print(f"Failed to update the repository: {update_result.stderr}")
                return False
        else:
            print("The repository is already up to date.")
        return True
    except Exception as e:
        print(f"Error checking for updates: {str(e)}")
        return False
