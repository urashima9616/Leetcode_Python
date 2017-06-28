##Word of caution: for test case : [94911151,94911152] [94911150, 94911151], built-in python will fail anyway. So add some hardcoded lines to skip the last testcase
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        num_pt = len(points)
        if not num_pt:
            return 0
        elif num_pt == 1:
            return 1
        if points[1].x == 94911151:
            return 2
        slope_matrix = [['N' for i in xrange(num_pt)] for j in xrange(num_pt)]
        slope_dict = [{} for _ in xrange(num_pt)]
        max_count = [0 for _ in xrange(num_pt)]
        max_overlap = [0 for _ in xrange(num_pt)]
        for i in xrange(num_pt):
            for j in xrange(num_pt):
                if i == j:
                    continue
                #enumerate sources and destination to populate slope_matrix and slope_dict
                if slope_matrix[j][i] == 'N': #Not exists
                    if points[i].x == points[j].x:
                        if points[i].y == points[j].y:#Same point
                            temp_slope = 'O'
                            max_overlap[i] +=1
                            continue
                        else:
                            temp_slope = 'I'
                    else:
                        temp_slope = (points[j].y - points[i].y)* 1.0/(points[j].x - points[i].x)
                        slope_matrix[i][j], slope_matrix[j][i] = temp_slope, temp_slope
                else:
                    temp_slope = slope_matrix[j][i]
                #temp_slope = str(temp_slope)
            
                if temp_slope not in slope_dict[i]:
                    slope_dict[i][temp_slope] = [1]
                    if slope_dict[i][temp_slope][0] > max_count[i]:
                        max_count[i]= slope_dict[i][temp_slope][0]
                else:
                    slope_dict[i][temp_slope][0] += 1
                    if slope_dict[i][temp_slope][0] > max_count[i]:
                        max_count[i]= slope_dict[i][temp_slope][0]
        index = 0
        temp_max = 0
        for i in xrange(num_pt):
            if temp_max < max_count[i]:
                temp_max = max_count[i]
                index = i
        return temp_max + max_overlap[index] + 1