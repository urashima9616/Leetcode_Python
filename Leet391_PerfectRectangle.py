class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        xmin, xmax = float('inf'), -float('inf')
        ymin, ymax = float('inf'), -float('inf')
        area_sum = 0
        #check overlapping
        for i in xrange(len(rectangles)):
            if rectangles[i][0] < xmin:
                xmin = rectangles[i][0]
            if rectangles[i][1] < ymin:
                ymin = rectangles[i][1]
            if rectangles[i][2] > xmax:
                xmax = rectangles[i][2]
            if rectangles[i][3] > ymax:
                ymax = rectangles[i][3]
            for j in xrange(i+1, len(rectangles)):
                if self.isOverlap(rectangles[i], rectangles[j]):
                    return False
            area_sum += (rectangles[i][2]-rectangles[i][0]) * (rectangles[i][3]-rectangles[i][1])
        if area_sum == (xmax-xmin) * (ymax-ymin):
            return True
        else:
            return False
                
    
    def isOverlap(self, r1, r2):
        """
        type r1, r2: List[int]
        rtype: Boolean
        """
        ymin_1, xmin_1, ymax_1, xmax_1 = r1[1], r1[0], r1[3], r1[2]
        ymin_2, xmin_2, ymax_2, xmax_2 = r2[1], r2[0], r2[3], r2[2]
        x_overlap, y_overlap = False, False
        
        if ymin_1 == ymax_2 or ymax_1 == ymin_2:
            y_overlap == False
        elif (ymin_1 < ymax_2 and ymin_1 > ymin_2) or (ymax_1 < ymax_2 and ymax_1 > ymin_2):
            y_overlap = True

        if xmin_1 == xmax_2 or xmax_1 == xmin_2:
            x_overlap == False
        elif (xmin_1 < xmax_2 and xmin_1 > xmin_2) or (xmax_1 < xmax_2 and xmax_1 > xmin_2):
            x_overlap = True
        return x_overlap & y_overlap
Solve = Solution()
rectangles = [[0,0,1,1],[0,1,3,2],[1,0,2,2]]
print Solve.isRectangleCover(rectangles)