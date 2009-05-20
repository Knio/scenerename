`scenerename`
=============

Python script to automatically rename scene filenames to a more
user-friendly format.


Usage
=====

Command line arguments:

*   `-s` / `--samples`
    
    Test out the parsing on a variety of samples which were designed to
    challenge the script.

*   `-d` / `--dict`
    
    Displays a verbose dictionary of all the matched elements in the name.

*   `-o` / `--output`
    
    Specifies an alternate output format. Use the python string format
    notation coupled with the names from `-d`.
    (i.e. `-o %(show)s %(season)sx%(episode)2s - %(title)s.%(ext)s`)

*   `-n` / `--none`
    
    Alternate string to use for unknown titles. (Default: "None")

*   `-f1` / `--filter-before`
    
    Apply pre-parsing rules to difficult names to aid in proper parsing.
    (i.e. `-f1 '[{group|name]}'='groupname'`)

*   `-f2` / `--filter-after`
    
    Apply post-parsing replacements to difficult names to aid in proper
    parsing. Works exactly like `-f1` except the replacement is done on
    the new filename.

*   `--confirm`
    
    Be default the script only display how it would rename the files but
    will not perform the action. Append this to perform the renaming.


Developed By
============
* Tom Flanagan - <theknio@gmail.com>
* Jake Wharton - <jakewharton@gmail.com>

Git repository located at
[github.com/Knio/scenerename](http://github.com/Knio/scenerename)


License
=======
    Copyright 2009 Tom Flanagan, Jake Wharton
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
       http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
