import subprocess

def check_for_updates():
    """
    Check if the local master branch is up to date with the remote repository.
    If not, update it using git pull.
    """
    print("Checking for updates...")
    try:
        # Fetch the latest references from the remote repository
        result = subprocess.run(['git', 'fetch'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Get the default branch name from the remote repository (e.g., 'main' instead of 'master')
        result = subprocess.run(['git', 'remote', 'show', 'origin'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error fetching remote details: {result.stderr}")
            return False
        
        # Extract the default branch name from the output
        for line in result.stdout.splitlines():
            if "HEAD branch" in line:
                remote_default_branch = line.split(":")[1].strip()
                break
        else:
            print("Could not determine the default branch name.")
            return False

        # Compare local and remote branch SHAs
        result = subprocess.run(['git', 'rev-parse', f'origin/{remote_default_branch}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        remote_sha = result.stdout.strip()

        result = subprocess.run(['git', 'rev-parse', remote_default_branch], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        local_sha = result.stdout.strip()

        if local_sha != remote_sha:
            print(f"The repository is not up to date. Pulling the latest changes from the {remote_default_branch} branch...")
            # If the local branch is behind, pull the latest changes
            update_result = subprocess.run(['git', 'pull', 'origin', remote_default_branch], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if update_result.returncode == 0:
                print("Repository updated successfully.")
            else:
                print(f"Failed to update the repository: {update_result.stderr}")
                return False
        else:
            print(f"The repository is already up to date with the {remote_default_branch} branch.")
        return True
    except Exception as e:
        print(f"Error checking for updates: {str(e)}")
        return False
