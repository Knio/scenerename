`scenerename`
=============

Python script to automatically rename scene filenames to a more
user-friendly format.


Usage
=====

Individual Files
----------------
Pass individual file names as arguments to rename specific files.

    /mnt/media/.Downloads/Scrubs.S08.720p.HDTV.x264$ python ~/projects/scenerename/scenerename.py e7-scrubs.s08e09.720p-x264.mkv Scrubs.S08E02.720p.HDTV.X264-DIMENSION.mkv
    Fetching series data for "scrubs"...
    --------------------------------------------------------------------------------------------------------------------------------------------
    Original Name                                                          New Name
    --------------------------------------------------------------------------------------------------------------------------------------------
    e7-scrubs.s08e09.720p-x264.mkv                                         Scrubs 8x09 - My Absence.mkv
    Scrubs.S08E02.720p.HDTV.X264-DIMENSION.mkv                             Scrubs 8x02 - My Last Words.mkv
    
    Run with "--confirm" to rename files
    

Directories
-----------
Run the script in a directory to have it parse all of the files.

    /mnt/media/.Downloads/Scrubs.S08.720p.HDTV.x264$ python ~/projects/scenerename/scenerename.py
    Fetching series data for "scrubs"...
    --------------------------------------------------------------------------------------------------------------------------------------------
    Original Name                                                          New Name
    --------------------------------------------------------------------------------------------------------------------------------------------
    e7-scrubs.s08e09.720p-x264.mkv                                         Scrubs 8x09 - My Absence.mkv
    scrubs.s08e16.720p.hdtv.x264-0tv.mkv                                   Scrubs 8x16 - My Cuz.mkv
    scrubs.s08e11.720p.hdtv.x264-ctu.mkv                                   Scrubs 8x11 - My Nah Nah Nah.mkv
    Scrubs.S08E07.720p.HDTV.X264-DIMENSION.mkv                             Scrubs 8x07 - My New Role.mkv
    Scrubs.S08E06.720p.HDTV.X264-DIMENSION.mkv                             Scrubs 8x06 - My Cookie Pants.mkv
    scrubs.s08e14.720p.hdtv.x264-ctu.mkv                                   Scrubs 8x14 - My Soul on Fire (1).mkv
    scrubs.s08e15.720p.hdtv.x264-ctu.mkv                                   Scrubs 8x15 - My Soul on Fire (2).mkv
    scrubs.s08e01.720p.hdtv.x264-ctu.mkv                                   Scrubs 8x01 - My Jerks.mkv
    e7-scrubs.s08e10.720p-x264.mkv                                         Scrubs 8x10 - My Comedy Show.mkv
    scrubs.812.proper.720p.hdtv.x264-sys.mkv                               Scrubs 8x12 - Their Story II.mkv
    scrubs.s08e17.720p.hdtv.x264-ctu.mkv                                   Scrubs 8x17 - My Chief Concern.mkv
    Scrubs.S08E18.720p.HDTV.X264-DIMENSION.mkv                             Scrubs 8x18 - My Finale.mkv
    Scrubs.S08E13.720p.HDTV.X264-DIMENSION.mkv                             Scrubs 8x13 - My Full Moon.mkv
    Scrubs.S08E02.720p.HDTV.X264-DIMENSION.mkv                             Scrubs 8x02 - My Last Words.mkv
    scrubs.s08e04.720p.hdtv.x264-ctu.mkv                                   Scrubs 8x04 - My Happy Place.mkv
    Scrubs.S08E05.720p.HDTV.X264-DIMENSION.mkv                             Scrubs 8x05 - My ABC's.mkv
    Scrubs.S08E08.720p.HDTV.X264-DIMENSION.mkv                             Scrubs 8x08 - My Lawyer's in Love.mkv
    scrubs.s08e03.720p.hdtv.x264-ctu.mkv                                   Scrubs 8x03 - My Saving Grace.mkv
    
    Run with "--confirm" to rename files


Dictionary Output
----------------
The dictionary output (`-d`/`--dict`) shows you all of the data that `scenerename` was
able to match.

    /mnt/media/.Downloads/Scrubs.S08.720p.HDTV.x264$ python ~/projects/scenerename/scenerename.py --dict Scrubs.S08E02.720p.HDTV.X264-DIMENSION.mkv
    Fetching series data for "scrubs"...
    Scrubs.S08E02.720p.HDTV.X264-DIMENSION.mkv --> Scrubs 8x02 - My Last Words.mkv
      episode: 02
      title: My Last Words
      season: 8
      vcodec: X264
      show: Scrubs
      source: HDTV
      ext: mkv
      group: DIMENSION
      resolution: 720p


Command Line Arguments
----------------------
*   `-s` / `--samples`
    
    Test out the parsing on a variety of samples which were designed to
    challenge the script.

*   `-d` / `--dict`
    
    Displays a verbose dictionary of all the matched elements in the name.

*   `-o` / `--output`
    
    Specifies an alternate output format. Use the python string format
    notation coupled with the names from `-d`.
    (i.e. `-o "%(show)s %(season)sx%(episode)2s - %(title)s.%(ext)s"`)

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
