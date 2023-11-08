# Postmortem Report

## 500 Internal Server Error
<img src="meme.jpg" />
### Summary
On Novemeber 8th, 2023 at 16:00 the server went down, returning 500 Internal Server Error when accessing any endpoint.

### Timeline
- **16:00 PST** - 500 Internal Server Error
- **16:05 PST** - Check if Apache server is up and running
- **16:10 PST** - Check if 80 PORT is open
- **16:15 PST** - Attach strace to Apache (strace -p "apache pid") and try accessing the web server
- **16:16 PST** - Access server, and look into strace log
- **16:30 PST** - Locate the file which lead to the error (typo in /var/www/html/wp-settings.php)
- **16:35 PST** - Fix the typo
- **16:36 PST** - Server is up and running

### Root Cause and Resolution
- The issue was caused by a typo in the /var/www/html/wp-settings.php file, when the server tries to load a file /var/www/html/wp-includes/class-wp-locale.phpp the error "No such file or directory" is raised beause of the typo seen in the extension of the file "class-wp-locale.phpp".
- To resolve the issue, a puppet script was create to search for the file name ending with .phpp and replace the extention with .php.

### Corrective and Preventive Measures
- Always test before deployment