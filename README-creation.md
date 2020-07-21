# README-creation.md

Repo to reorganize current content on groja.com and convert to Material Design Bootstrap (MDB).

# About `README-creation.md`

This file contains steps used to create this site from the old one.

This file is mostly obsolete, but at this time I see no need to delete it.

# References

- Downloaded Free version from https://mdbootstrap.com/getting-started/ on 2018-10-01
- MDB Nav bar docs: https://mdbootstrap.com/components/navbar/

# Plan

## Overview

- Add the new legal pages and shorten the top-level menu
  - Replace Galleries menu option with Privacy and Terms option
  - Consolidate portions of Home page and Books and Sites under About menu option
- Convert from Bootstrap MDB, using code from the `always_learning_google_products` repo, as follows:
  - For Home page use code from `material_design/05-material_design_bootstrap/02-landing_page/Site/`
  - For All other pages use code from `material_design/05-material_design_bootstrap/03-corporate_website/Site/`

## Steps - Outline

- [x] 1. Create new repo, `groja.com-mdb` , and populate it with the existing code in the `groja.com` repo

- [x] 2. Replace Bootstrap 3 static files with freshly downloaded MDB static files
  - [x] 2.1. Delete old and commit
  - [x] 2.2. Download latest MDB code from the site
  - [x] 2.3. Add new and commit
  - [x] 2.4. Update head element in base.html with code from the latest downloaded version of index.html
  - [x] 2.5. Use local files rather than CDN - my connection sucks

- [x] 3. Replace Galleries option with drop-down menu for Privacy & Terms pages
  - [x] 3.1. Starting point: code from `material_design/05-material_design_bootstrap/03-corporate_website/Site/`
  - [x] 3.2. Update `base.html` template
  - [x] 3.3. Get all four pages integrated and looking nice.

- [x] 4. Consolidate existing menu options
  - [x] 4.1. Remove Home menu option
  - [x] 4.2. Consolidate Books and Sites under "About" - or "History of Groja.com" , or "About Grojas" or ...?
  - [x] 4.3. But consolidate all text into a single page
  - [x] 4.4. Make menu drop-down with options to take visitor to the desired part of the page
  - [x] 4.5. Submenu option suggestions:
    - About
    - Books
    - Sites
    - History of Groja.com
    - Your portrait

- [x] 5. Move social icons to right side of nav bar
  - [x] 5.1. Example code is in `/material_design/05-material_design_bootstrap/02-landing_page/Site/index.html`
  - [x] 5.2. Update `base.html` template
  - [x] 5.3. Code for existing icons is in a sidebar in the `base_with_nav.html` template

- [x] 6. Copy content from legal pages on SeeOurMinds.com to the new Legal pages
- [x] 7. Update new About page, creating sections as appropriate
- [x] 8. Update existing Your Portrait page
- [x] 9. Revamp existing Home page
- [x] 10. Update existing conversion pages as appropriate

## Steps - Notes

### 1. Create new repo, `groja.com-mdb` , and populate it with the existing code in the `groja.com` repo

- Got it to work ok on port 5001, so we can see both sites locally

### 2. Replace Bootstrap 3 static files with freshly downloaded MDB static files

#### 2.1. Delete old and commit - but do not push quite yet

- NOT deleting `favicon.ico` , `css/README.md` , `css/groja.css` or `images/*` files

#### 2.2. Download latest MDB code from the site

- Downloaded Free version from https://mdbootstrap.com/getting-started/ on 2018-10-01
- Compare to what we have in the `always_learning_google_products` repo, in `material_design/05-material_design_bootstrap/00-downloaded/Site/`
  - Downloaded the code in `always_learning_...` on Aug 26, 2018 - little over a month ago
  - Compare briefly - just curious how much it may have changed, if at all
  - 3 new files - 95 vs. 93
     - New files: `js/modules/velocity.js` and `scss/free/_switch.scss`
  - Running `lf | xargs wc -l`
     - 79022 total lines vs. 80300 total lines in older version
     - `scss/free/_animations*` files smaller
- Has changed a bit, but not hugely

#### 2.3. Add new and commit

- Adding files from the css, font, img, js, scss, and parent directories

#### 2.4. Update head element in base.html with code from the latest downloaded version of index.html

- Decided to use `groja.css` instead of `style.css` for customizations, for consistency with my other python sites
- Using local copy of font-awesome.min.css, downloaded from https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css

### 3. Replace Galleries option with drop-down menu for Privacy & Terms pages

- MDB Nav bar docs: https://mdbootstrap.com/components/navbar/

#### 3.1. Starting point: code from `material_design/05-material_design_bootstrap/03-corporate_website/Site/`

- Actually used code from the file `02-landing_page/Site/index-footer_1.html`

#### 3.2. Get all four pages integrated and looking nice.

- Focusing on navigation for now, will add in the actual text later

### 4. Consolidate existing menu options

#### 4.1. Remove Home menu option

- Replaced it with Site Name

#### 4.2. Consolidate Books and Sites under "About" - or "History of Groja.com" , or "About Grojas" or ...?

#### 4.3. But consolidate all text into a single page

- Focusing on navigation for now
- Will actually add the text in a later step

#### 4.4. Make menu drop-down with options to take visitor to the desired part of the page

#### 4.5. Submenu option suggestions: About, Books, Sites, History (of Groja.com)

- This took some playing around and experimenting with the various section titles, but I am very happy with the result.

### 5. Move social icons to right side of nav bar

- May want to adjust the colors - later

### 6. Copy content from legal pages on SeeOurMinds.com to the new Legal pages

### 7. Update new About page, creating sections as appropriate

- Leaving the affiliate marketing buttons on this page alone for now
- Finish artsyvisions, and add the links there, then come back to this - then deploy
- This took some effort, but I am very happy with the result.

### 8. Update existing Your Portrait page

- This took some effort, but I am very happy with the result.

### 9. Revamp existing Home page

- This took some effort, but I am very happy with the result.

### 10. Update existing conversion pages as appropriate

- This took some effort, but I am very happy with the result.

### 11. Deployment

- Changed the name of this repo!
- See details in the `README.md` file for the `artsyvisions.com` repo

### 11.1. Deployment Issue - Solved!

**Symptoms:**

- All conversions failed with Internal Server Error

**The Problem:**

- Apache unable to write to DB due to permissions on file system.
- Error Message:
  - "sqlite3.OperationalError: attempt to write a readonly database"

**Researching how to fix:**

```
cd /var/www/groja.com/htdocs/groja.com/gitignored
groups                  # groups I am in:
# tomh adm cdrom sudo dip plugdev lpadmin sambashare libvirtd
groups www-data         # groups www-data is in
# www-data : www-data
getent group  www-data  # who is in www-data's group
# www-data:x:33:
getent group  tomh      # who is in my group
# tomh:x:1000:
```

**Solution**

[x] 1. change group on db directory and files to www-data
[x] 2. change permissions on db directory to 775
[x] 3. change permissions on db files to 664


```
 $ ls -al db/
total 20
drwxr-xr-x 2 tomh tomh 4096 Nov 24 17:51 .
drwxr-xr-x 4 tomh tomh 4096 Nov 24 17:51 ..
-rw-r--r-- 1 tomh tomh    0 Nov 24 17:51 .this_dir_intentionally_left_empty
-rw-r--r-- 1 tomh tomh 5120 Oct  3 10:38 NameEmail.db
-rw-r--r-- 1 tomh tomh  669 Oct  3 10:38 NameEmailSchema.sql
 $ sudo chgrp -R www-data db
[sudo] password for tomh:
 $ ls -al db/
total 20
drwxr-xr-x 2 tomh www-data 4096 Nov 24 17:51 .
drwxr-xr-x 4 tomh tomh     4096 Nov 24 17:51 ..
-rw-r--r-- 1 tomh www-data    0 Nov 24 17:51 .this_dir_intentionally_left_empty
-rw-r--r-- 1 tomh www-data 5120 Oct  3 10:38 NameEmail.db
-rw-r--r-- 1 tomh www-data  669 Oct  3 10:38 NameEmailSchema.sql
 $ chmod 775 db
 $ ls -al db/
total 20
drwxrwxr-x 2 tomh www-data 4096 Nov 24 17:51 .
drwxr-xr-x 4 tomh tomh     4096 Nov 24 17:51 ..
-rw-r--r-- 1 tomh www-data    0 Nov 24 17:51 .this_dir_intentionally_left_empty
-rw-r--r-- 1 tomh www-data 5120 Oct  3 10:38 NameEmail.db
-rw-r--r-- 1 tomh www-data  669 Oct  3 10:38 NameEmailSchema.sql
 $ chmod 664 db/NameEmail*
 $ ls -al db/
total 20
drwxrwxr-x 2 tomh www-data 4096 Nov 24 17:51 .
drwxr-xr-x 4 tomh tomh     4096 Nov 24 17:51 ..
-rw-r--r-- 1 tomh www-data    0 Nov 24 17:51 .this_dir_intentionally_left_empty
-rw-rw-r-- 1 tomh www-data 5120 Oct  3 10:38 NameEmail.db
-rw-rw-r-- 1 tomh www-data  669 Oct  3 10:38 NameEmailSchema.sql
 $
```

