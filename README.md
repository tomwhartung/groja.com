# groja.com-mdb

Repo to reorganize current content on groja.com and convert to Material Design Bootstrap (MDB).

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

- [ ] 2. Replace Bootstrap 3 static files with freshly downloaded MDB static files
  - [ ] 2.1. Delete old and commit
  - [ ] 2.2. Download latest MDB code from the site
  - [ ] 2.3. Add new and commit
  - [ ] 2.4. Update head element in base.html with code from the latest downloaded version of index.html

- [ ] 3. Replace Galleries option with drop-down menu for Privacy & Terms pages
  - [ ] 3.1. Starting point: code from `material_design/05-material_design_bootstrap/03-corporate_website/Site/`
  - [ ] 3.2. Get all four pages integrated and looking nice.

- [ ] 4. Consolidate existing menu options
  - [ ] 4.1. Remove Home menu option
  - [ ] 4.2. Consolidate Books and Sites under "About" - or "History of Groja.com" , or "About Grojas" or ...?
  - [ ] 4.3. But consolidate all text into a single page
  - [ ] 4.4. Make menu drop-down with options to take visitor to the desired part of the page
  - [ ] 4.5. Submenu option suggestions: About, Books, Sites, History (of Groja.com)

- [ ] 5. Revamp existing home page
  - [ ] 5.1. Use code from `material_design/05-material_design_bootstrap/02-landing_page/Site/` in the `always_learning_google_products` repo
  - [ ] 5.2. Update `base.html` template
  - [ ] 5.3. Replace static files as necessary
  - [ ] 5.4. Use local files rather than CDN - my connection sucks
  - [ ] 5.5. Don't care about what the other pages look like right now

## Steps - Notes

### 1. Create new repo, `groja.com-mdb` , and populate it with the existing code in the `groja.com` repo

- Got it to work ok on port 5001, so we can see both sites locally

### 2. Replace Bootstrap 3 static files with freshly downloaded MDB static files

#### 2.1. Delete old and commit

- Commit but do not push quite yet

#### 2.2. Download latest MDB code from the site

- Compare to what we have in the `always_learning_google_products` repo, in `material_design/05-material_design_bootstrap/00-downloaded/Site/`
  - Just curious how much it may have changed, if at all

#### 2.3. Add new and commit

#### 2.4. Update head element in base.html with code from the latest downloaded version of index.html

### 3. Replace Galleries option with drop-down menu for Privacy & Terms pages

#### 3.1. Starting point: code from `material_design/05-material_design_bootstrap/03-corporate_website/Site/`

#### 3.2. Get all four pages integrated and looking nice.

### 4. Consolidate existing menu options

#### 4.1. Remove Home menu option

#### 4.2. Consolidate Books and Sites under "About" - or "History of Groja.com" , or "About Grojas" or ...?

#### 4.3. But consolidate all text into a single page

#### 4.4. Make menu drop-down with options to take visitor to the desired part of the page

#### 4.5. Submenu option suggestions: About, Books, Sites, History (of Groja.com)

### 5. Revamp existing home page

#### 5.1. Use code from `material_design/05-material_design_bootstrap/02-landing_page/Site/` in the `always_learning_google_products` repo

#### 5.2. Update `base.html` template

#### 5.3. Replace static files as necessary

#### 5.4. Use local files rather than CDN - my connection sucks

#### 5.5. Don't care about what the other pages look like right now


