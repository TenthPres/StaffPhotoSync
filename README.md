Staff Photo Sync
================

This is a set of scripts that we use to sync our staff user photos across Active Directory and G Suite (formerly Google Apps for Business).  The scripts in this directory do the following things:

 1.  Scrape [the staff webpage](http://www.tenth.org/about/staff), downloading the photos of each staff member and interpreting a username from the person's first and last name.
 2.  Crop the staff photo to an area just around the face.  (Using OpenCV)
 3.  Use PowerShell and GAM to push the images to Active Directory and Google Cloud respectively.

## Prerequisites

In order for these scripts to work, you must have [GAM](https://github.com/jay0lee/GAM) installed, and PowerShell enabled.

Also, the user running the scripts must have permission to edit user photos in Active Directory.

Although the scripts are written in Python, they're compiled such that Python does *not* need to be installed 

## Installation & Running

To install, grab [the latest release](https://github.com/TenthPres/StaffPhotoSync/releases) and unzip it wherever you want it to live.  

If you haven't already installed and configured GAM with credentials, you'll also need to do that. 

To run, just kick off `run.cmd`.  

## Info for Contributors

This collection of scripts is meant to be simple.  While you'll probably need to adapt things to make them work for you, we hope you'll consider contributing any improvements you make. 

### Testing

To test the system without compiling the Python scripts, run `run-test.cmd`.

### Building

You can build by running the `build.cmd` script.  This will compile the Python scripts, and create a release-ready zip file, called `StaffPhotos.zip`.  The contents of this zip file are identical to the `dist` directory that's created as part of the build process. 
