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
]


import sys
import os
import re


def filter(n):
    
    def nice(s):
        return re.sub("[._]", " ", s).title().strip()
    
    formats = [
    r"^(?P<group>[\w.@-]+)-(?P<show>[\w.-]+)(?P<season>\d)(?P<episode>\d{2})\.(?P<ext>\w+)$",
    r"""^
        (?P<show>[ \w.-]+?)
        (?P<locale>US|UK)?  #Used for shows like The Office
        
        -?([ \.]s?(?P<season>\d{1,2}))?   
        (e|x)?(?P<episode>\d{1,2}([-_](?P<is_multiple>\d{2}))?)(of(?P<total_eps>\d))?
        
        (?P<title>[ \w.-]+?)?? #Non-aggressive!
        
        (
            ([ \._](?P<ar>ws|fs|oar))|
            ([ \._](?P<is_repack>repack))|
            ([ \._](?P<is_proper>proper))|
            ([ \._](?P<source>hdtv|blu-?ray|hd-?dvd|pdtv|dvdrip|dsr))|
            ([ \._](?P<resolution>720p|1080i|1080p))|
            ([ \._](?P<vcodec>xvid|x264|wmv-?hd))|
            ([ \._](?P<acodec>DD5\.1|AC3|DTS))
        )*
        
        ([-\s](?P<group>[\w.@-]+))?
        
        \.(?P<ext>\w+)
    $""",
    ]
    
    for r in formats:
        m = re.match(r, n, re.IGNORECASE | re.VERBOSE)
        if m:
            m = m.groupdict()
            m['show'] = nice(m['show'])
            if 'is_multiple' in m and m['is_multiple']:
                m['is_multiple'] = bool(m['is_multiple'])
                m['episode'] = m['episode'].replace('_', '-')
            else:
                m['episode'] = int(m['episode'])
            if 'total_eps' in m and m['total_eps']:
                m['total_eps'] = int(m['total_eps'])
            if m['season']:
                m['season'] = int(m['season'])
            if 'title' in m and m['title']:
                m['title'] = nice(m['title'])
            if 'is_repack' in m:
                m['is_repack'] = bool(m['is_repack'])
            if 'is_proper' in m:
                m['is_proper'] = bool(m['is_proper'])
            return m
    return None


def main():
    args = sys.argv[1:]
    
    confirm = False
    show_dict = False
    allow_rename = True
    names = []
    format = "%(show)s %(season)sx%(episode)2s - %(title)s.%(ext)s"
    
    while args:
        a = args.pop(0)
        if a == '--confirm' and allow_rename:
            confirm = True
            
        elif a == '-s' or a == '--samples':
            names = samples
            allow_rename = False
            
        elif a == '-d' or a == '--dict':
            show_dict = True
            
        elif a == '-o' or a == '--output':
            format = args.pop(0)
            
        else:
            allow_rename = confirm = False
            names.append(a)
    
    if not names:
        names = os.listdir('.')
    
    newdicts = map(filter,names)
    
    if not show_dict:
        print '-'*140
        print "%-60s %-100s" %  ('Original Name', 'New Name')
        print '-'*140
    
    for old, dict in zip(names,newdicts):
        
        if dict:
            new = None
            while not new:
                try:
                    new = format % dict
                except KeyError, e:
                    dict[e.args[0]] = None
        else:
            confirm = False
            new = "ERROR: Non-matching name"
        
        if show_dict:
            print '%s --> %s' % (old, new)
            if dict:
                for key, value in dict.items():
                    if value:
                        print '  %s: %s' % (key, value)
            print
        else:
            print "%-60s %-100s" % (old, new)
        
        if allow_rename and confirm and new:
            os.rename(old, new)
    
    print
    if confirm:
        print 'Files have been renamed'
    elif allow_rename:
        print 'Run with "confirm" to rename files'


if __name__ == '__main__':
    main()