#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers.

This module provides a high-level deployment orchestration task that combines
the archive creation and distribution processes into a single automated workflow.
It imports and coordinates functionality from separate modules to achieve a
complete end-to-end deployment pipeline.

The deployment orchestration performs two main operations:
    1. Creates a timestamped compressed archive of the web_static directory
    2. Distributes the created archive to all configured web servers

This unified approach provides:
    - Single-command deployment from source to production
    - Automatic archive creation with timestamp versioning
    - Multi-server distribution in one operation
    - Integrated error handling across the entire pipeline
    - Consistent deployment workflow

Architecture:
    The script uses dynamic module importing to load deployment functions from
    separate module files. This modular design allows for:
    - Separation of concerns (packing vs deploying)
    - Independent testing of each deployment stage
    - Reusability of individual components
    - Flexibility in module organization

Module Dependencies:
    - 1-pack_web_static: Provides do_pack() function for archive creation
    - 2-do_deploy_web_static: Provides do_deploy() function for distribution
    - fabric.api: Provides env and task decorators
    - importlib: Enables dynamic module importing

Target Servers:
    Defined in env.hosts, the script deploys to multiple web servers.

Typical usage example:
    $ fab deploy
    
    # This single command will:
    # 1. Create versions/web_static_YYYYMMDDHHMMSS.tgz
    # 2. Upload and deploy to all configured servers
    # 3. Update symbolic links to activate the new version

Prerequisites:
    - Both 1-pack_web_static.py and 2-do_deploy_web_static.py must exist
    - web_static directory must exist in current working directory
    - SSH access configured for all target servers
    - Proper permissions on local and remote directories

Workflow:
    deploy() -> do_pack() -> creates archive -> do_deploy(archive_path) -> deploys to servers

Error Handling:
    Returns False if either archive creation or deployment fails, otherwise True.
"""

import importlib
from fabric.api import env, task

# Dynamically import the pack module containing archive creation functionality
# Module name: '1-pack_web_static' (hyphenated filename)
# This imports the entire module to access its do_pack function
pack_module = importlib.import_module('1-pack_web_static')

# Dynamically import the deploy module containing distribution functionality
# Module name: '2-do_deploy_web_static' (hyphenated filename)
# This imports the entire module to access its do_deploy function
deploy_module = importlib.import_module('2-do_deploy_web_static')

# Extract the do_pack function from the imported pack module
# This function creates a timestamped .tgz archive of web_static directory
do_pack = pack_module.do_pack

# Extract the do_deploy function from the imported deploy module
# This function distributes an archive to all configured web servers
do_deploy = deploy_module.do_deploy

# Define the target web servers for deployment
# List of IP addresses where the archive will be distributed
# Fabric will execute deployment operations on each host
env.hosts = ['54.160.106.64', '35.175.132.153']

@task
def deploy():
    """Creates and distributes an archive to the web servers.
    
    This high-level orchestration task automates the complete deployment pipeline
    by combining archive creation and distribution into a single operation. It
    first creates a compressed archive of the web_static directory, then
    distributes that archive to all configured web servers if creation succeeds.
    
    The function acts as a workflow coordinator, calling do_pack() to create
    the archive and do_deploy() to distribute it. This provides a single
    entry point for complete deployments without requiring manual coordination
    of the individual steps.
    
    Returns:
        bool: True if both archive creation and deployment to all servers succeed.
            False if archive creation fails or deployment to any server fails.
            
    Deployment Workflow:
        1. Calls do_pack() to create timestamped archive in versions/ directory
        2. Validates that archive was created successfully (not None/False)
        3. If archive creation fails, returns False immediately
        4. Calls do_deploy(archive_path) to distribute archive to all servers
        5. Returns the result of do_deploy (True on success, False on failure)
        
    Side Effects:
        - Creates new archive file in versions/ directory (via do_pack)
        - Creates new release directory on all remote servers (via do_deploy)
        - Updates 'current' symbolic link on all remote servers (via do_deploy)
        - Prints deployment status messages from both functions
        
    Example:
        # Execute complete deployment workflow
        $ fab deploy
        
        # Expected output on success:
        # web_static packed: versions/web_static_20231215143022.tgz -> 2048576Bytes
        # [54.160.106.64] Executing task 'deploy'
        # [54.160.106.64] put: versions/web_static_20231215143022.tgz -> /tmp/...
        # ...
        # New version deployed!
        # Done.
        
    Error Handling:
        - Returns False immediately if do_pack() fails (returns None/False)
        - Returns False if do_deploy() fails on any server
        - Does not perform rollback on failure
        - Partial deployments may occur if some servers succeed and others fail
        
    Note:
        This function delegates all actual work to the imported do_pack and
        do_deploy functions. It serves as a convenience wrapper for the complete
        deployment pipeline. The archive_path returned by do_pack() is passed
        directly to do_deploy() without modification or validation beyond
        truthiness checking.
        
    Dependencies:
        Requires successful import of:
        - do_pack from 1-pack_web_static module
        - do_deploy from 2-do_deploy_web_static module
    """
    
    # Execute the do_pack function to create a compressed archive
    # Returns the path to the created archive file, or None if creation fails
    archive_path = do_pack()
    
    # Check if archive creation failed (returned None or False)
    # If so, return False immediately without attempting deployment
    if not archive_path:
        return False
    
    # Execute the do_deploy function with the created archive path
    # Distributes the archive to all servers defined in env.hosts
    # Returns True if deployment succeeds on all servers, False otherwise
    return do_deploy(archive_path)
