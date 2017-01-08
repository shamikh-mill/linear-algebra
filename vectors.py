#Library of common linear algebra vector operations. Used as exercise file for Udacity Linear Algebra Refresher Course 

from math import sqrt 
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
        return Vector([c*x for x in self.coordinates])


    # unit vector: vector with magnitude = 1, represents vector direction 
    # Normalization: find unit vector in same direction as given vector. Scalar multiplication of vector with 1/magnitude(v) 


    def magnitude(self): 
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalize(self): 
        try: 
            magnitude = self.magnitude()
            return self.scalar_product(1.0/magnitude)
        except: 
            # if exception occurs in try statement, this runs 
            raise Exception('Cannot normalize a zero vector!')



my_vector = Vector([1, 2, 3])
print my_vector
my_vector2 = Vector([1, 2, 3])
my_vector3 = Vector([-1, 2, 3])

print my_vector3 == my_vector2
a = Vector([8.218, -9.341])
b = Vector([-1.129, 2.111])
print a.sum(b)

v = Vector([1, 2])
print v.magnitude()
print v.normalize()