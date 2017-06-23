Staff Photo Sync
================

This is a set of scripts that we use to sync our staff user photos.  The scripts in this directory do tha following things:

 1.  Scrape the staff webpage, downloading the staff images, and interpreting a username from the person's first and last name
 2.  Crop the staff images to an area just around the face.  (Using OpenCV)
 3.  Use PowerShell and GAM to push the images to Active Directory and Google Cloud respectively.

## Prerequisites

In order for these scripts to work, you must have [GAM](https://github.com/jay0lee/GAM) installed, and PowerShell enabled.
Also, the user running the scripts must have permission to edit user photos in Active Directory.

