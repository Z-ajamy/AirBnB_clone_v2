#!/usr/bin/python3
"""Fabric deployment script for packaging web static content.

This module provides Fabric tasks for automating the deployment process of
static web content. It creates compressed archive files (tgz format) of the
web_static directory with timestamped filenames for version control and
deployment tracking.

The script uses Fabric's task decorator to define deployment operations that
can be executed from the command line using the fab command.

Key Features:
    - Automatic directory creation for storing archive versions
    - Timestamped archive naming for tracking deployments
    - Compressed tar.gz format for efficient storage and transfer
    - Error handling with graceful failure returns
    - File size reporting after successful archive creation

Dependencies:
    - Fabric library (fabric.api, fabric.contrib.files)
    - Python os module for file operations
    - Python datetime module for timestamp generation

Typical usage example:
    $ fab do_pack
    
Prerequisites:
    - web_static directory must exist in the current working directory
    - Write permissions for creating versions directory and archive files
    
Archive Format:
    Filename: web_static_YYYYMMDDHHMMSS.tgz
    Location: versions/web_static_YYYYMMDDHHMMSS.tgz
"""
from fabric.api import *

import os

from datetime import datetime


@task
def do_pack():
    """Create a compressed archive of the web_static directory.
    
    This Fabric task generates a timestamped tar.gz archive of the web_static
    directory and stores it in the versions directory. The archive filename
    includes the current date and time to ensure unique version identification.
    
    The function performs the following operations:
        1. Creates the versions directory if it doesn't exist
        2. Generates a timestamp-based archive filename
        3. Compresses the web_static directory using tar with gzip
        4. Verifies the operation success
        5. Reports the archive path and file size on success
    
    Returns:
        str: The path to the created archive file on success.
        None: If the archive creation fails or an exception occurs.
        
    Raises:
        Exception: Catches all exceptions during archive creation and returns None.
        
    Archive Naming Convention:
        Format: web_static_YYYYMMDDHHMMSS.tgz
        Example: web_static_20231215143022.tgz
        
    Side Effects:
        - Creates 'versions' directory in current working directory
        - Creates compressed archive file in versions directory
        - Prints success message with archive path and file size
        
    Example:
        # Execute from command line
        $ fab do_pack
        
        # Output on success:
        # web_static packed: versions/web_static_20231215143022.tgz -> 2048576Bytes
        
    Note:
        The function uses Fabric's local() command to execute shell commands
        on the local machine. The tar command uses -czvf flags for:
        -c: create archive
        -z: compress with gzip
        -v: verbose output
        -f: specify filename
    """
    try:
        # Create the versions directory if it doesn't exist
        # -p flag ensures no error if directory already exists
        local("mkdir -p versions")
        
        # Generate archive filename with current timestamp
        # Format: web_static_YYYYMMDDHHMMSS.tgz
        archive_name = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))
        
        # Construct the full path to the archive file
        archive_path = f"versions/{archive_name}"

        # Execute tar command to create compressed archive of web_static directory
        # Stores the result object to check for command execution success
        res = local("tar -czvf {} web_static".format(archive_path))

        if res.failed:
            # Return None if the tar command failed
            return None
        else:
            # Get the size of the created archive file in bytes
            file_size = os.path.getsize(archive_path)
            
            # Print success message with archive path and file size
            print(f"web_static packed: {archive_path} -> {file_size}Bytes")
    except Exception as e:
        # Catch any exceptions during the archive creation process
        # Return None to indicate failure without crashing the script
        return None
