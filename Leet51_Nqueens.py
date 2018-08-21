class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set([_ for _ in xrange(n)])
        sum_set = set()
        diff_set = set()
        board = [["." for i in xrange(n)] for j in xrange(n)]
        res = []
        
        def placeQueens(k, path):
            if k == n:
                if path not in res:
                    res_temp = []
                    for i in xrange(n):
                        temp = ["." for _ in xrange(n)]
                        temp[path[i]] = "Q"
                        temp = "".join(temp)
                        res_temp.append(temp)
                    res.append(res_temp)
                return
            for i in xrange(n):# try each colum for this queeen
                if i in col and (k+i not in sum_set) and (k-i not in diff_set):
                    col.remove(i)
                    diff_set.add(k-i)
                    sum_set.add(k+i)
                    board[k][i] = "Q"
                    placeQueens(k+1, path + [(i)])
                    col.add(i)
                    diff_set.remove(k-i)
                    sum_set.remove(k+i)
                    board[k][i] = "."                    
            return
        placeQueens(0, [])
        return res