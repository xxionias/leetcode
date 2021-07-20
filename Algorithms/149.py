import math
class Solution():
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        max_count = 0
        for i in range(len(points)):
            points_on_lines = {'i' : 1}  #for vertical lines
            duplicates, gcd = 0, 0
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x1, y2 = points[j][0], points[j][1]
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                    continue
                elif x1 == x2:
                    slope = 'i'  #vertical line
                else:
                    delta_x, delta_y = x2 - x1, y2 - y1
                    if delta_x < 0:
                        delta_x, delta_y = -delta_x, -delta_y
                    gcd = math.gcd(delta_x, delta_y)
                    slope = (delta_x / gcd, delta_y / gcd)
                points_on_lines[slope] = points_on_lines.get(slope, 1) + 1
            max_count = max(max_count, max(points_on_lines.values()) + duplicates)
        return max_count
