#Library of common linear algebra vector operations. Used as exercise file for Udacity Linear Algebra Refresher Course 

from math import acos, pi, sqrt 
from decimal import Decimal, getcontext 
getcontext().prec = 30 

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates]) #coordinates are decimals objects 
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def sum(self, v):
        #return Vector([self.coordinates[i] + v.coordinates[i] for i in range(len(self))])
        return Vector([x+y for x, y in zip(self.coordinates, v.coordinates)])
        #zip combines two iterables for operations 

    def difference(self, v):
        #return Vector([self.coordinates[i] - v.coordinates[i] for i in range(len(self))])
        return Vector([x-y for x, y in zip(self.coordinates, v.coordinates)])

    def scalar_product(self, c): #each number in vector x c
        return Vector([Decimal(c)*x for x in self.coordinates])


    # unit vector: vector with magnitude = 1, represents vector direction 
    # Normalization: find unit vector in same direction as given vector. Scalar multiplication of vector with 1/magnitude(v) 


    def magnitude(self): 
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalize(self): 
        try: 
            magnitude = self.magnitude()
            return self.scalar_product(Decimal('1.0')/magnitude)
        except: 
            # if exception occurs in try statement, this runs 
            raise Exception('Cannot normalize a zero vector')

    #used to find angle between two vectors. Results in an NUMBER, not a vector 
    def dotproduct(self, v): 
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees = False): #if in_degrees = True, will output angle in degrees, False- radians 
        try: 
            u1 = self.normalize()
            u2 = v.normalize()
            angle_radians = acos(u1.dotproduct(u2))

            if in_degrees: # in_degrees == True
                degrees_per_radian = 180.0/pi 
                return angle_radians * degrees_per_radian

            else:
                return angle_radians

        except Exception as e: 
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG: 
                raise Exception('Cannot compute an angle with the zero vector')
            else: 
                raise e


    # vectors are parallel if one vector is a scalar multiple of the other. They can be parallel even if pointing in opposite directions 
    # vectors are perpendicular (orthogonal) if their dot product = 0. One is 0 vector, or they are perpendicular 

    def is_orthogonal(self, v, tolerance = 1e - 10): #tolerance is small value. Use this as a check instead of zero, if abs(dot) < tolerance 
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v): 
        return ( self.is_zero() or 
            v.is_zero() or 
            self.angle_with(v) == 0 or #same direction
            self.angle_with(v) == pi)  #opposite direction 
            # these are all the conditionals for parallel vectors, booleans 

    def is_zero(self, v, tolerance = 1e - 10): 
        return self.magnitude() < tolerance 

    def component_orthoganol_to(self, basis): 
        try: 
            projection = self.component_parallel_to(basis)
            return self.difference(projection)

        except Exception as e: 
            if str(e) == NO_UNIQUE_PARALLEL_COMPONENT_MSG: 
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else: 
                raise e




    def component_parallel_to(self, basis): 
        try: 
            basis.normalize() #make unit vector
            weight = self.dot(u) #make dot product of u with vector being projected 
            return u.scalar_product(weight)

        except Exception as e: 
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG: 
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else: 
                raise e 

    def is_orthoganol_to(self, v, tolerance= 1e - 10): 
        return abs(self.dot(v)) < tolerance 


    #cross product 


my_vector = Vector([1, 2, 3])
print my_vector
my_vector2 = Vector([1, 2, 3])
my_vector3 = Vector([-1, 2, 3])

print my_vector3 == my_vector2
a = Vector([8.218, -9.341])
b = Vector([-1.129, 2.111])
print a.sum(b)

