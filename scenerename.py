#!/usr/bin/python

WIDTH = 100

samples = [
 'Dead.Like.Me.S02E15.Haunted.WS.DVDRip.XviD-TVEP.avi',
 'dead_like_me.1x01.pilot.something.ws_dvdrip_xvid-fov.avi',
 'eureka.s02e12.hdtv.xvid-bia.avi',
 'eureka.s02e13.repack.hdtv.xvid-bia.avi',
 'fringe.s01e14.proper.720p.hdtv.x264-2hd.mkv',
 'tpz-eureka101.avi',
 'History.Channel.The.Universe.S03E07.720p.HDTV.x264-DHD.mkv',
 'PBS.Unforgivable.Blackness.1of2.Rise.x264.AC3-MVGroup.avi',
 'Lost.S01E24_25.HDTV.720p.avi',
 'Firefly.S01E14.1080p.BluRay.DTS.x264-Z@X.mkv',
 'The.Office.US.S05E11.720p.HDTV.X264-DIMENSION.mkv',
 'Star Trek Enterprise - S04E14 The Aenar 720p DD5.1 x264 HDA.mkv',
 'Stargate 7x22 - The Lost City part 2.avi',
 'Stargate.SG-1.S05E17.DVDRip.DivX-SFM.avi',
 'Stargate.SG1.S01E06.AC3.DivX.DVDRip-AMC.avi',
 'stargate_sg-1.6x01.redemption_part1.ws_dvdrip_xvid-fov.avi',
 'terminator.the.sarah.connor.chronicles.s01e09.dvdrip.xvid.orpheus.avi',
 'Masters Of Science Fiction S01E01 NTSC DVD X264 AC3 5.1.mkv',
 'THE X-FILES - S07 E02 - THE SIXTH EXTINCTION (2) NTSC DVD DD2.0 x264 MMI.mkv',
 'Lost S01E01-E02 Title HDTV-Group.avi',
 'mythbusters.pilots.ep01.dvdrip.xvid-memetic.avi',
 '[BHD]battlestar.galactica.s04e20.720p.hdtv.x264-ctu.mkv',
 'aaf-bsg.s04e11.avi',
 'Lost 5x11 - Whatever Happened, Happened.avi',
]


import os
import re
import sys

from vendor import *
tvdb = tvdb_api.Tvdb()


r_show    = r"(?P<show>[-\w. ]+?)(?P<locale>US|UK)?[-. ]*"
r_title   = r"([-. ]*(?P<title>[-\w().,' ]+?)[-. ]*)??"

r_details = r"""
    (
        ([ ._](?P<ar>ws|fs|oar))|
        ([ ._](?P<is_repack>repack))|
        ([ ._](?P<is_proper>proper))|
        ([ ._](?P<source>hdtv|blu-?ray|hd-?dvd|pdtv|dvd(rip)?|dsr|bd-rip|webrip))|
        ([ ._](?P<resolution>576p|720p|1080i|1080p))|
        ([ ._\-](?P<vcodec>xvid|divx|x264|h264|vc1|mpeg2))|
        ([ ._](?P<acodec>DD|AC3|DTS))|
        ([ ._]?(?P<achannels>(1|2|5|6|7)[ .]?(0|1)))|
        ([ ._](?P<container>WMV-HD))|
        ([ ._](?P<broadcast>PAL|NTSC))
    )*"""
r_group   = r"([-. ](?P<group>[\w.@]+?))??"
r_fgroup  = r"((?P<group>[\w.@]+?)-)?"
r_ext     = r"\.(?P<ext>\w+)"
r_ending  = r_title + r_details + r_group + r_ext


def filter_name(n):

    def nice(s):
        return re.sub("[._]", " ", s).title().strip()

    formats = [
        # group-show.S##E##.details.ext
        r"^%s%sS(?P<season>\d{2})E(?P<episode>\d{2}(-\d{2})?)%s%s$" % (r_fgroup, r_show, r_details, r_ext),
        # group-show### .ext
        #           ####
        r"^%s%s(?P<season>\d{1,2})(?P<episode>\d{2}(-\d{2})?)%s$" % (r_fgroup, r_show, r_ext),
        # show.# of# .title.details-group.ext
        #      # of##
        #      ##of##
        r"^%s(?P<episode>\d{1,2}(-\d{2})?)of(?P<total_eps>\d{1,2})%s$" % (r_show, r_ending),
        # show.S##E##    .title.details-group.ext
        #      S##E##-##
        #      S##E##-E##
        r"^%sS(?P<season>\d{2}).?EP?(?P<episode>\d{2}([-_]E?\d{2})?)%s$" % (r_show, r_ending),
        # show.#x## .title.details-group.ext
        #      ##x##
        r"^%s(?P<season>\d{1,2})x(?P<episode>\d{2}(-\d{2})?)%s$" % (r_show, r_ending),
        # show.### .title.details-group.ext
        #      ####
        r"^%s(?P<season>\d{1,2})(?P<episode>\d{2}(-\d{2})?)%s$" % (r_show, r_ending),
    ]

    for r in formats:
        m = re.match(r, n, re.IGNORECASE | re.VERBOSE)
        if m:
            m = m.groupdict()
            m['show'] = nice(m['show'])
            m['episode'] = m['episode'].replace('_', '-').replace('E', '').rjust(2,'0')

            if 'total_eps' in m and m['total_eps']:
                m['total_eps'] = int(m['total_eps'])

            if 'season' in m:
                m['season'] = int(m['season'])
            else:
                m['season'] = 0

            try:
                lookup = m['show']
                if 'locale' in m and m['locale']:
                    lookup += ' ' + m['locale']
                lookup = lookup.lower()

                episode = m['episode']
                if '-' in episode:
                    episode = episode.split('-')[0]



                m['title'] = tvdb[lookup][int(m['season'])][int(episode)]['episodename']
                m['show'] = tvdb[lookup]['seriesname']
            except (tvdb_api.tvdb_error, tvdb_api.tvdb_shownotfound, tvdb_api.tvdb_seasonnotfound, tvdb_api.tvdb_episodenotfound):
                if 'title' in m and m['title']:
                    m['title'] = nice(m['title'])
                else:
                    m['title'] = None

            if 'is_repack' in m:
                m['is_repack'] = bool(m['is_repack'])
            if 'is_proper' in m:
                m['is_proper'] = bool(m['is_proper'])
            return m
    return None

def filename(s):
    '''
    converts a string to a valid filename
    by stripping out incvalid characters
    '''
    invalid = r'''?\/:<>|'''
    return ''.join(filter(lambda c:c not in invalid, list(s)))



def main():
    args = sys.argv[1:]

    confirm = False
    confirm_each = False
    show_dict = False
    allow_rename = True
    none_title = None
    names = []
    format = "%(show)s %(season)sx%(episode)2s - %(title)s.%(ext)s"

    filters1 = []
    filters2 = []

    while args:
        a = args.pop(0)
        if a == '-h' or a == '--help' or a == '-help':
            print '''
Command Line Arguments

-s / --samples          Test out the parsing on a variety of samples which
                        were designed to challenge the script.

-d / --dict             Displays a verbose dictionary of all the matched
                        elements in the name.

-o / --output           Specifies an alternate output format. Use the python
                        string format notation coupled with the names from -d.
            (i.e. -o "%(show)s %(season)sx%(episode)2s - %(title)s.%(ext)s")

-n / --none             Alternate string to use for unknown titles.
                        (Default: "None")

-f1 / --filter-before   Apply pre-parsing rules to difficult names to aid in
                        proper parsing. (i.e. -f1 '[{group|name]}'='groupname')

-f2 / --filter-after    Apply post-parsing replacements to difficult names to
                        aid in proper parsing. Works exactly like -f1 except
                        the replacement is done on the new filename.

--confirm               Be default the script only display how it would rename
                        the files but will not perform the action.
                        Append this to perform the renaming.
'''
            return


        elif a == '--confirm' and allow_rename:
            confirm = True

        elif a == '--confirm-each' and allow_rename:
            confirm_each = True

        elif a == '-s' or a == '--samples':
            names = samples
            allow_rename = False

        elif a == '-d' or a == '--dict':
            show_dict = True

        elif a == '-o' or a == '--output':
            format = args.pop(0)

        elif a == '-n' or a == '--none':
            none_title = args.pop(0)

        elif a == '--filter-before' or a == '-f1':
            filters1.append(args.pop(0).split('=',2))

        elif a == '--filter-after'  or a == '-f2':
            filters2.append(args.pop(0).split('=',2))

        else:
            allow_rename = confirm = False
            names.append(a)


    if not names:
        names = [i for i in  os.listdir('.') if os.path.isfile(i)]
        names.sort()

    def user_filter(f):
        if len(f) > 0:
            print f
        def filter(n):
            for a,b in f:
                n = re.sub('(?i)' + a, b, n)
            return n

        return filter

    newdicts = [filter_name(user_filter(filters1)(i)) for i in names]

    if not show_dict:
        print '-'*WIDTH
        print "%-*s %-*s" %  (WIDTH/2, 'Original Name',  WIDTH/2, 'New Name')
        print '-'*WIDTH

    for old, dict in zip(names,newdicts):
        cnf = True
        if dict:
            new = None
            if not 'title' in dict or not dict['title']:
                dict['title'] = str(none_title)
            while not new:
                try:
                    new = format % dict
                except KeyError, e:
                    dict[e.args[0]] = None
            new = filename(user_filter(filters2)(new))
        else:
            cnf = False
            new = "ERROR: Non-matching name"

        if show_dict:
            print '%s --> %s' % (old, new)
            if dict:
                for key, value in dict.items():
                    if value:
                        print '  %s: %s' % (key, value)
            print
        else:
            if len(old) > WIDTH/2:
                print old.encode('ascii','replace')
                print ' '*(WIDTH/2), '%-*s' % (WIDTH,new.encode('ascii','replace'))
            else:
                print "%-*s %-*s" % (WIDTH/2, old.encode('ascii','replace'), WIDTH/2, new.encode('ascii','replace'))

        if allow_rename and confirm and cnf and new:
            os.rename(old, new)

        elif allow_rename and confirm_each and cnf and new:
          print 'rename? (y/n)',
          import msvcrt
          c = msvcrt.getch()
          if c in ['y','Y']:
            os.rename(old, new)
          print '\b'*20,

    print
    if confirm:
        print 'Files have been renamed'
    elif allow_rename:
        print 'Run with "--confirm" to rename files'


if __name__ == '__main__':
    main()

