#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers.

This module provides Fabric tasks for automating the deployment and distribution
of web static content archives to multiple remote web servers. It handles the
complete deployment workflow including file transfer, extraction, directory
management, and symbolic link updates for zero-downtime deployments.

The deployment process follows these steps:
    1. Validates the archive file exists locally
    2. Uploads the archive to remote servers' /tmp directory
    3. Creates a new release directory on remote servers
    4. Extracts the archive contents to the release directory
    5. Reorganizes the directory structure
    6. Updates the symbolic link to point to the new release
    7. Cleans up temporary files

This approach enables:
    - Multiple version management through separate release directories
    - Atomic deployments using symbolic link switching
    - Easy rollback by changing the symbolic link
    - Consistent deployment across multiple servers

Dependencies:
    - Fabric library (fabric.api: env, put, run, task)
    - Python os.path module for file validation

Target Servers:
    The script deploys to the servers defined in env.hosts list.
    
Typical usage example:
    $ fab do_deploy:archive_path=versions/web_static_20231215143022.tgz
    
Prerequisites:
    - SSH access to target web servers configured
    - Proper SSH keys or credentials set up for authentication
    - Target servers must have /data/web_static/ directory structure
    - Archive file must exist at the specified path
    - Remote servers need tar, mkdir, mv, rm, and ln utilities

Directory Structure on Remote Servers:
    /data/web_static/releases/          - All release versions
    /data/web_static/releases/{version}/ - Specific release directory
    /data/web_static/current            - Symlink to active release
"""

from fabric.api import env, put, run, task
import os.path

# Define the hosts to deploy to
# List of IP addresses or hostnames of the target web servers
# Fabric will execute deployment commands on each host sequentially
env.hosts = ['54.160.106.64', '35.175.132.153']

@task
def do_deploy(archive_path):
    """Distributes an archive to the web servers.
    
    This Fabric task handles the complete deployment workflow for distributing
    a web static content archive to all configured web servers. It performs
    validation, file transfer, extraction, and directory management to ensure
    the new version is properly deployed and activated.
    
    The deployment uses a release directory strategy where each deployment
    creates a new timestamped directory, allowing for easy rollback and
    version management. The 'current' symbolic link is updated atomically
    to point to the new release.

    Args:
        archive_path (str): The path to the archive file to deploy. Must be
            a valid path to a .tgz compressed archive file containing the
            web_static directory. Example: "versions/web_static_20231215143022.tgz"

    Returns:
        bool: True if all operations were successful on all servers, 
            False if the archive doesn't exist or any operation fails.
            
    Deployment Process:
        1. Validates archive file exists locally
        2. Extracts filename and creates release directory name
        3. Uploads archive to /tmp/ on remote servers
        4. Creates release directory structure
        5. Extracts archive contents to release directory
        6. Removes temporary archive file from /tmp/
        7. Moves web_static contents up one level
        8. Removes empty web_static subdirectory
        9. Removes old 'current' symbolic link
        10. Creates new symbolic link pointing to new release
        
    Side Effects:
        - Creates new directory in /data/web_static/releases/ on remote servers
        - Modifies /data/web_static/current symbolic link
        - Uploads and then deletes files in /tmp/ directory
        - Prints "New version deployed!" message on success
        
    Example:
        # Deploy a specific archive
        $ fab do_deploy:archive_path=versions/web_static_20231215143022.tgz
        
        # Expected output on success:
        # [54.160.106.64] Executing task 'do_deploy'
        # [54.160.106.64] put: versions/web_static_20231215143022.tgz -> /tmp/web_static_20231215143022.tgz
        # ...
        # New version deployed!
        # Done.
        
    Error Handling:
        Returns False immediately if:
        - Archive file doesn't exist locally
        - Any remote command execution fails
        - Any exception occurs during the process
        
    Note:
        All remote operations are checked for failure. If any step fails,
        the function returns False without completing remaining steps.
        The function does not perform automatic rollback on failure.
    """
    # Validate that the archive file exists locally before attempting deployment
    # Returns False immediately if file is not found to prevent unnecessary operations
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the filename from the full archive path
        # Example: "versions/web_static_20231215143022.tgz" -> "web_static_20231215143022.tgz"
        file_name = archive_path.split("/")[-1]
        
        # Extract the folder name by removing the file extension
        # Example: "web_static_20231215143022.tgz" -> "web_static_20231215143022"
        # This will be used as the release directory name
        folder_name = file_name.split(".")[0]
        
        # Construct the full path to the release directory on remote servers
        # Each release gets its own timestamped directory for version management
        release_path = f"/data/web_static/releases/{folder_name}"

        # Upload the archive file to the /tmp/ directory on remote servers
        # Check if the put operation failed and return False if so
        if put(archive_path, f'/tmp/{file_name}').failed:
            return False

        # Create the release directory on remote servers with parent directories
        # -p flag creates intermediate directories as needed
        if run(f'mkdir -p {release_path}').failed:
            return False

        # Extract the tar.gz archive to the release directory
        # -x: extract, -z: decompress gzip, -f: specify file, -C: change to directory
        if run(f'tar -xzf /tmp/{file_name} -C {release_path}').failed:
            return False

        # Remove the temporary archive file from /tmp/ to free up space
        # Archive is no longer needed after successful extraction
        if run(f'rm /tmp/{file_name}').failed:
            return False

        # Move all contents from the extracted web_static subdirectory up one level
        # This normalizes the directory structure to match expected layout
        if run(f'mv {release_path}/web_static/* {release_path}/').failed:
            return False
        
        # Remove the now-empty web_static subdirectory
        # -rf flags: recursive force removal without prompting
        if run(f'rm -rf {release_path}/web_static').failed:
            return False

        # Remove the existing 'current' symbolic link
        # -rf ensures removal even if it's a directory or doesn't exist
        if run('rm -rf /data/web_static/current').failed:
            return False

        # Create a new symbolic link named 'current' pointing to the new release
        # This atomically switches the active version with zero downtime
        # -s flag creates a symbolic (soft) link
        if run(f'ln -s {release_path} /data/web_static/current').failed:
            return False

        # Print success message to indicate deployment completed successfully
        print("New version deployed!")
        return True

    except Exception:
        # Catch any unexpected exceptions during the deployment process
        # Return False to indicate deployment failure without exposing error details
        return False
