from github import Github
import requests
from typing import Tuple

from mySecrets import GITHUB_TOKEN

g = Github(GITHUB_TOKEN)

def get_repo_stats(owner, repo_name) -> Tuple[int, int]:
    try:
        repo = g.get_repo(f"{owner}/{repo_name}")
        
        # Fetch file and line counts
        total_files = 0
        total_lines = 0

        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "file":
                total_files += 1
                
                # Skip README and .gitignore files for line count
                if file_content.name.lower().startswith("readme") or file_content.name == ".gitignore" or file_content.name == 'rewards.json': 
                    continue
                if file_content.name == 'requirements.txt' or file_content.name == 'Procfile' or file_content.name == 'runtime.txt':
                    continue
                if file_content.name.endswith('.png'):
                    continue

                # Fetching file content to count lines
                file_url = file_content.download_url
                response = requests.get(file_url)
                if response.status_code == 200:
                    # Count non-whitespace lines only
                    lines = response.text.splitlines()
                    non_whitespace_lines = [line for line in lines if line.strip()]
                    total_lines += len(non_whitespace_lines)
            elif file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))

        return (total_files, total_lines)

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
owner = "DHMorse"  # Replace with the owner of the repository
repo_name = "oeTesting"  # Replace with the repository name
oeTestingTotalFiles, oeTestingTotalLines = get_repo_stats(owner, repo_name)
repo_name = 'flaskAppOE'
flaskAppOETotalFiles, flaskAppOETotalLines = get_repo_stats(owner, repo_name)
owner = 'Eli-Mason'
repo_name = 'Omniplexium-Eternal'
omniEternalTotalFiles, omniEternalTotalLines = get_repo_stats(owner, repo_name)

totalFiles = oeTestingTotalFiles + flaskAppOETotalFiles + omniEternalTotalFiles
totalLines = oeTestingTotalLines + flaskAppOETotalLines + omniEternalTotalLines

print(f"oeTesting: {oeTestingTotalFiles} files, {oeTestingTotalLines} lines")
print(f"flaskAppOE: {flaskAppOETotalFiles} files, {flaskAppOETotalLines} lines")
print(f"Omniplexium-Eternal: {omniEternalTotalFiles} files, {omniEternalTotalLines} lines")

print('')

print(f"Total Files: {totalFiles}")
print(f"Total Lines of Code: {totalLines}")