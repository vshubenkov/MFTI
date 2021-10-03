  if self.y >= 550 and self.speed >= 10 and self.marker_wall == True:
            self.marker_wall = False
            self.speed = self.speed/1.5
            self.an = self.an/1.2
            print(self.x, self.y)
            self.delta_x = self.x
            self.delta_y = self.y
        elif self.x >= 780 and self.speed >= 10 and self.marker_wall == True:
            self.direction = 'left'
            self.marker_wall = False
            self.speed = self.speed/1.5
            self.an = self.an/1.2 - math.pi/2
            self.delta_x = self.x
            self.delta_y = self.y

        elif self.speed >= 10:
            if self.direction == 'right':
                dx = math.fabs(self.speed * math.cos(self.an))/5
                self.x_coord += dx
                self.y_coord = (self.x_coord - self.delta_x) * math.tan(self.an) + \
                               (9.8 * (self.x_coord - self.delta_x)**2)/(2 * (self.speed)**2 * math.cos(self.an)**2) + self.delta_y
                self.x = self.x_coord
                self.y = self.y_coord
                canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
                self.marker_wall = True
            else:
                dx = math.fabs(self.speed * math.cos(self.an))/5
                self.x_coord -= dx
                self.y_coord = -(self.x_coord - self.delta_x) * math.tan(self.an) - \
                               (9.8 * (self.x_coord - self.delta_x)**2)/(2 * (self.speed)**2 * math.cos(self.an)**2) + self.delta_y
                self.x = self.x_coord
                self.y = self.y_coord
                canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        else:
            pass
        if t1.live == 0:
            balls.clear()
        elif len(balls) > 3:
            canv.delete(balls.pop(0).id)