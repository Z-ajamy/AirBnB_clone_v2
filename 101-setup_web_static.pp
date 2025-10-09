# Puppet manifest to set up web servers for web_static deployment.
#
# This Puppet manifest automates the complete configuration of Nginx web servers
# for serving static web content with a release-based deployment structure. It
# handles package installation, directory hierarchy creation, symbolic link
# management, Nginx configuration, and service management.
#
# Key Features:
#   - Automated Nginx installation and configuration
#   - Release-based directory structure for version management
#   - Symbolic link setup for zero-downtime deployments
#   - Custom Nginx server block with static content serving
#   - Automatic service restart on configuration changes
#   - Proper file ownership and permissions
#
# Directory Structure Created:
#   /data/web_static/releases/       - All release versions
#   /data/web_static/releases/test/  - Test release directory
#   /data/web_static/shared/         - Shared resources
#   /data/web_static/current         - Symlink to active release
#
# Nginx Configuration:
#   - Serves static content at /hbnb_static endpoint
#   - Adds X-Served-By header with hostname for tracking
#   - Includes redirect endpoint at /redirect_me
#   - Custom 404 error page handling
#
# Target Systems:
#   - Ubuntu/Debian-based Linux distributions
#   - Systems with apt package manager
#   - Requires 'ubuntu' user and group to exist
#
# Usage:
#   sudo puppet apply manifest.pp
#
# Dependencies:
#   - Puppet agent installed
#   - Internet connection for package installation
#   - Root/sudo privileges for execution
#
# Resource Ordering:
#   The manifest uses 'require' parameters to ensure proper dependency
#   ordering. Resources are applied in the correct sequence automatically.

# 1. Ensure the Nginx package is installed.
# This resource manages the Nginx web server package installation.
# Puppet will use the system's package manager (apt on Ubuntu/Debian)
# to install Nginx if it's not already present.
package { 'nginx':
  ensure => installed,
}

# 2. Create the required directory structure and set ownership.
# The following file resources create a hierarchical directory structure
# for managing web static content releases. Each directory is owned by
# the 'ubuntu' user and group, and 'require' parameters ensure parent
# directories are created before child directories.

# Create the base /data directory
# This is the root directory for all web static content
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create the /data/web_static directory
# This directory serves as the container for all web static content
# Requires /data to be created first
file { '/data/web_static':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data'],
}

# Create the releases directory for storing all deployment versions
# Each deployment will create a new timestamped subdirectory here
# Allows for version management and easy rollback
file { '/data/web_static/releases':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static'],
}

# Create the shared directory for resources common across releases
# Files here can be shared between different versions (configs, uploads, etc.)
file { '/data/web_static/shared':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static'],
}

# Create a test release directory for initial deployment validation
# This directory simulates a real release and is used for testing
file { '/data/web_static/releases/test':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases'],
}

# 3. Create a fake HTML file for testing.
# This resource creates a simple HTML file in the test release directory
# to validate that the deployment structure and Nginx configuration work correctly.
# The content is a minimal valid HTML document displaying "ALX".
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "<html>\n  <head>\n  </head>\n  <body>\n    ALX\n  </body>\n</html>\n",
  require => File['/data/web_static/releases/test'],
}

# 4. Create the symbolic link.
# The 'force => true' option ensures it's deleted and recreated if it already exists.
# This symbolic link points to the currently active release directory.
# By changing this link, deployments can switch between versions atomically
# without downtime. The 'force' parameter ensures any existing file or link
# is replaced, making this resource idempotent.
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  force   => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases/test'],
}

# 5. Update Nginx configuration to serve the static content.
# 'notify' will trigger a service restart only when this file's content changes.
# This resource manages the Nginx default site configuration file.
# The configuration includes:
#   - Default HTTP server listening on port 80 (IPv4 and IPv6)
#   - X-Served-By header with hostname for request tracking
#   - /hbnb_static location serving content from the 'current' symlink
#   - /redirect_me location for redirecting to an external URL
#   - Custom 404 error page handling
# The 'notify' parameter triggers an Nginx service restart only when
# the configuration content changes, ensuring changes take effect.
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$hostname;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}",
  notify  => Service['nginx'],
}

# 6. Ensure the Nginx service is running and enabled on boot.
# This resource manages the Nginx service state and boot configuration.
# 'ensure => running' ensures Nginx is actively running.
# 'enable => true' configures Nginx to start automatically on system boot.
# 'require' ensures this resource is applied only after the nginx package is installed.
# This resource will be automatically notified and restarted when the
# configuration file changes (via the 'notify' parameter in resource #5).
service { 'nginx':
  ensure    => running,
  enable    => true,
  # 'require' ensures this resource is applied only after the nginx package is installed.
  require   => Package['nginx'],
}
