import subprocess

def check_for_updates():
    """
    Check if the local master branch is up to date with the remote repository.
    If not, update it using git pull.
    """
    print("Checking for updates...")
    try:
        # Check the status of the git repo on the master branch
        result = subprocess.run(['git', 'fetch'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the local master is behind the remote master
        result = subprocess.run(['git', 'rev-parse', 'origin/master'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        remote_master_sha = result.stdout.strip()

        result = subprocess.run(['git', 'rev-parse', 'master'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        local_master_sha = result.stdout.strip()

        if local_master_sha != remote_master_sha:
            print("The repository is not up to date. Pulling the latest changes from the master branch...")
            # If the local master branch is behind, pull the latest changes
            update_result = subprocess.run(['git', 'pull', 'origin', 'master'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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
