class Jump:            
    m, n = 10, 10  # 10 rows，10 columns
    entry = (0, 0)  # entry
    path = [entry]  # one path
    paths = []  # all paths
    # move directions
    directions = [(0, 1), (1, 0)]
    
    def conflict(self,nx, ny):    
        # whether can pass
        if 0 <= nx < self.m and 0 <= ny < self.n:                        
            return False
        return True
    
    def walk(self,grids,x, y):  # (x,y)grid   
        if x==9 and y==9:  # exit
            
            self.paths.append(self.path[:])         
        else:
            for d in self.directions:  # Traverse both directions
                nx, ny = x + d[0]*grids[x][y], y + d[1]*grids[x][y]
                self.path.append((nx, ny))  # new coordinate push
                if not self.conflict(nx, ny):  
                    
                    self.walk(grids,nx, ny)
                            
                self.path.pop()  # Backtracking,pop if conflict
