"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

"""
import fractions

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    """
    Brutal force:
        - O(n^3)
        - go through every point tuples
    Idea:
        - O(n^2) solution
        - goes through each points, and find lines on two points tuple which unseen, save the linear parameters as map key
        - and then iterate through to add if point on the line (in map key)
        - find max at the end
    """
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)

        # at least 1 point
        res = 1
        params_map = {}
        for i in range(len(points)):
            max_now = 0
            count_same = 0 # number of same points

            for j in range(i+1, len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    count_same += 1
                else:
                    key = self.normalize(points[i], points[j])
                    if key in params_map:
                        count = params_map[key] + 1
                        params_map[key] = count
                        if count > max_now:
                            max_now = count
                    else:
                        params_map[key] = 1
                        if max_now == 0:
                            max_now += 1

            res = max(res, max_now + count_same + 1)  # +1 for starting point
            params_map = {}

        return res


    def normalize(self, p1, p2):
        """
        @purpose:
            Given 2 points, find and return linear equation parameters 'a|b|c'
        @params:
            (Point) p1
            (Point) p2
        @returns:
            'a|b|c'
        """
        # ax + by = c
        # horizontal
        if p1.x == p2.x:
            b = 0
            a = 1
            c = p1.x
        # vertical
        elif p1.y == p2.y:
            a = 0
            b = 1
            c = p1.y
        # ax + by = c
        else:
            dx = p1.x - p2.x
            dy = p1.y - p2.y
            gcd = fractions.gcd(dx, dy)
            a = dy / gcd
            b = dx / gcd
            # force to be negative (for key mapping purpose)
            if a * b < 0:
                a = -1 * abs(a)
                b = abs(b)
            # positive
            else:
                a = abs(a)
                b = abs(b)
            c = a * p1.x + b * p1.y

        return "{}|{}|{}".format(a, b, c)
