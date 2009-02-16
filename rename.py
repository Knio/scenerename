


samples = [
 'Dead.Like.Me.S02E15.Haunted.WS.DVDRip.XviD-TVEP.avi',
 'dead_like_me.1x01.pilot.something.ws_dvdrip_xvid-fov.avi',
 'eureka.s02e12.hdtv.xvid-bia.avi',
 'eureka.s02e13.repack.hdtv.xvid-bia.avi',
 'Eureka.S03E05.HDTV.XviD-SAiNTS.avi',
 'tpz-eureka101.avi',
]




import sys
import os
import re


filters = [
('tpz-', '')

]


def filter(n):
    
    
    for a,b in filters:
        n = re.sub(a,b,n)
    
    
    def nice(s):
        return re.sub("[._]", " ", s).title()
    
    formats = [
    #r"^([\w.]+?)\.(?:s|)(\d+)(?:E|x)(\d+)\.([\w.]+?)\.(?:ws|hdtv)[\w.-]+?\.(\w+)$",
    r"^([\w.-]+?)\.?(?:s|)(\d{1,2})(?:e|x|)(\d{2})(?:\.)?([\w.]*?)\.?(?:WS|ws|hdtv|repack)[\w.-]*?\.(\w+)$",
    r"^([\w.-]+?)\.?(?:s|)(\d{1,2})(?:e|x|)(\d{2})(?:\.)?([\w.]*?)\.?(?:WS|ws|hdtv|repack)?[\w.-]*?\.(\w+)$",
    ]
    
    for r in formats:
        m = re.match(r, n, re.IGNORECASE)
        if m:
            show    = nice(m.group(1))
            s       = int(m.group(2))
            e       = int(m.group(3))
            title   = nice(m.group(4))
            ext     = m.group(5)
            return '%s %dx%02d - %s.%s' % (show, s, e, title, ext)
        




def main():
    args = sys.argv[1:]
    
    confirm = False
    
    names = os.listdir('.')
    
    
    while args:
        a = args.pop(0)
        if a == 'confirm':
            confirm = True
            
        elif a == 'sample':
            names = samples
            
        else:
            print 'Invalid argument: %s' % a
            return
    
    
    
    newnames = map(filter,names)
    
    
    print '-'*140
    print "%-60s %-100s" %  ('Original Name', 'New Name')
    print '-'*140
    for old, new in zip(names,newnames):
        
        print "%-60s %-100s" % (old, new)
        
        if confirm and new:
            os.rename(old, new)
            pass
    
    print
    if confirm:
        print 'Files have been renamed'
    else:
        print 'Run with "confirm" to rename files'
    


if __name__ == '__main__':
    main()
    