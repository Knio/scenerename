# a 3d vector class
# this might work. 

import math

class Vector(object):
    def __init__(self, *args):
        '''
        Vector([vect])
        A 3D Vector class.
        vect can be any one of the following:
            an instance of Vector()
            a tuple of cartesian coordinates, (x, y, z)
            a tuple of polar coordinates, ((theta, phi), magnitude)
        represented internally as a right-handed cartesian vector
        '''
        if len(args) == 0:
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
            return
        if len(args) == 1:
            if not args[0]:
                self.x = 0.0
                self.y = 0.0
                self.z = 0.0
                return
            elif isinstance(args[0], Vector):
                self.x = args[0].x
                self.y = args[0].y
                self.z = args[0].z
                return
            elif isinstance(args[0], tuple):
                self.__init__(*args[0])
            else:
                raise ValueError('wrong arguments or number of arguments')
        if len(args) == 2:
            self.spatial(*args)
        if len(args) == 3:
            self.cartesian(*args)
        
    def spatial(self, (a, o), m):
        '''
        vector.spatial((theta, phi), magnitude))
        set the vector to the spatial angles and magnitude.
        '''
        self.x = math.cos(a) * math.sin(o) * m
        self.y = math.sin(a) * math.sin(o) * m
        self.z = math.cos(o) * m
        
    def cartesian(self, x, y, z):
        '''
        vector.cartesian(x, y, z)
        set the vector to the cartesian coordinates.
        '''
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def distance(self, vect=None):
        '''
        vector.distance([vect])
        return the distance from here to vect.
        if vect is omitted, return the distance from the origin (the length of the vector).
        '''
        if not isinstance(vect, Vector):    vect = Vector(vect)
        return math.sqrt((self.x-vect.x)**2 + (self.y-vect.y)**2 + (self.z-vect.z)**2)
        
    def distancexy(self, vect=None):
        '''
        vector.distancexy([vect])
        return the distance from here to vect, restricted to the xy-plane.
        if vect is omitted, return the distance from the origin on the xy-plane.
        '''
        if not isinstance(vect, Vector):    vect = Vector(vect)
        return math.sqrt((self.x-vect.x)**2 + (self.y-vect.y)**2)
        
    def angle(self, vect=None):
        '''
        vector.angle([vect])
        return the angle (theta, phi) from here to vect.
        if vect is omitted, return the angle from the origin to here.
        '''
        if not vect: return Vector().angle(self)
        if not isinstance(vect, Vector):    vect = Vector(vect)
        return math.atan2(vect.y-self.y, vect.x-self.x), math.atan2(self.distancexy(vect), vect.z-self.z)
        
    def rotate(self, vect, (a, o)):
        '''
        vector.rotate(vect, (theta, phi))
        rotates around the point vect, by the angles theta and phi.
        '''
        if not isinstance(vect, Vector):    vect = Vector(vect)
        a1, o1 = vect.angle(self)
        a = a + a1
        o = o + o1
        self.spatial((a, o), vect.distance(self))
        self.add(vect)
        
    def normal(self):
        '''
        vector.normal()
        normalizes the vector.
        '''
        self.spatial(self.angle(), 1.0)

    def pos(self):
        '''
        vector.pos()
        returns the position of the vector, (x, y, x).
        '''
        return self.x, self.y, self.z
        
    def add(self, vect=None):
        '''
        vector.add([vect])
        adds by vect.
        '''
        if not isinstance(vect, Vector):    vect = Vector(vect)
        self.x += vect.x
        self.y += vect.y
        self.z += vect.z
        
    def sub(self, vect=None):
        '''
        vector.sub([vect])
        subtracts by vect.
        '''
        if not isinstance(vect, Vector):    vect = Vector(vect)
        self.x -= vect.x
        self.y -= vect.y
        self.z -= vect.z
        
    def mul(self, vect):
        '''
        vector.mul([vect])
        multiplies by vect
        '''
        if not isinstance(vect, Vector):    vect = Vector(vect)
        self.x *= vect.x
        self.y *= vect.y
        self.z *= vect.z

    def div(self, vect):
        '''
        vector.div([vect])
        divides by vect
        '''
        if not isinstance(vect, Vector):    vect = Vector(vect)
        self.x /= vect.x
        self.y /= vect.y
        self.z /= vect.z
        
    def __iadd__(self, vect):
        self.add(vect)
        return self
        
    def __iadd__(self, vect):
        self.sub(vect)
        return self
       
    def __imul__(self, vect):
        self.mul(vect)
        return self
        
    def __idiv__(self, vect):
        self.div(vect)
        return self
        
    def __add__(self, vect):
        self = Vector(self)
        self.add(vect)
        return self
        
    def __sub__(self, vect):
        self = Vector(self)
        self.sub(vect)
        return self
        
    def __div__(self, vect):
        self = Vector(self)
        self.div(vect)
        return self
        
    def __mul__(self, vect):
        self = Vector(self)
        self.mul(vect)
        return self
    
    def __abs__(self):
        return self.distance()
        
    def __repr__(self):
        return '<vector (%.2f, %.2f, %.2f)>' % (self.x, self.y, self.z)
