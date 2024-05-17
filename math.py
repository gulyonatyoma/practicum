from math import cos, sin,  radians, degrees, atan, acos, pi

class Math_functions:

    def distance_twopoints(self, x1, y1, x2, y2):
        # Расстояние между двумя точками на плоскости:
        # (x1,y1) - координаты первой точки, (x2,y2) - второй
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def straight_serif(self, x, y, d, a):
        # Прямая линейно-угловая засечка:
        # (x,y) - координаты изв точки, d - расстояние от неё до неизв точки, a - угол между d и горизонталью
        return (x + d * cos(radians(a)), y + d * sin(radians(a)))

    def reverse_serif(self, x1, y1, x2, y2):
        # Обратная линейно-угловая засечка:
        # (x1,y1) - координаты первой точки, (x2,y2) - второй
        d = self.distance_twopoints(x1, y1, x2, y2)
        if d == 0:
            raise ZeroDivisionError('Division by zero')
        if x1 > x2:
            a = degrees(pi*2 - acos((x2 - x1) / d))
        else:
            a = degrees(acos((x2 - x1) / d))
        return (d, a)

    def angle_between_lines(self, x1, y1, x2, y2, x3, y3, x4, y4):
        # Вычисление угла между прямыми, заданными координатами точек
        # x1, y1-координата А, x2, y2-координата B, x3, y3-координата C, x4, y4-координата D; прямые:AB, CD; ищем острый угол
        if x1 != x2 and x3 != x4:
            K_ab = (y2 - y1) / (x2 - x1)
            K_cd = (y4 - y3) / (x4 - x3)
            tg_f = (K_ab - K_cd) / (1 + K_ab * K_cd)
            f = degrees(atan(tg_f))
        elif x1 == x2:
            K_cd = (y4 - y3) / (x4 - x3)
            f = degrees(atan(K_cd))
        else:
            K_ab = (y2 - y1) / (x2 - x1)
            f = degrees(atan(K_ab))
        return f

    def circle_and_line(self, x1, y1, x2, y2, xc, yc, r):
        # Вычисление координат точек пересечения окружности и прямой
        # x1, y1-координата А, x2, y2-координата B, xc,yc-координаты центра, r-кадиус окружности; ищем пересечение AB и окружности
        if x2 != x1:
            k = (y2 - y1) / (x2 - x1)
            b = y2 - k * x2
            #a_k, b_k, c_k- коэффиценты
            a_k = 1 + k ** 2
            b_k = 2 * k * (b - yc) - 2 * xc
            c_k = xc ** 2 + (b - yc) ** 2 - r ** 2
            D = b_k ** 2 - 4 * a_k * c_k
            if D > 0:
                x_cross1 = (-b_k + D ** 0.5) / (2 * a_k)
                x_cross2 = (-b_k - D ** 0.5) / (2 * a_k)
                y_cross1 = k * x_cross1 + b
                y_cross2 = k * x_cross2 + b
                return (x_cross1, y_cross1, x_cross2, y_cross2)
            elif D == 0:
                x_cross = -b_k / (2 * a_k)
                y_cross = k * x_cross + b
                return (x_cross, y_cross)
            return ()
        else:
            a_k = 1
            b_k = -2 * yc
            c_k = (x1 - xc) ** 2 + yc ** 2 - r ** 2
            D = b_k ** 2 - 4 * a_k * c_k
            if D > 0:
                y_cross1 = (-b_k + D ** 0.5) / (2 * a_k)
                y_cross2 = (-b_k - D ** 0.5) / (2 * a_k)
                return (float(x1), y_cross1, float(x2), y_cross2)
            elif D == 0:
                y_cross = -b_k / (2 * a_k)
                return (float(x1), y_cross)
            D = 0
            return ()

    def parallel_line(self, x1, y1, x2, y2, x0, y0):
        # Построение прямой, параллельной заданной, через заданную точку:
        # (x1,y1) - координаты первой точки заданной прямой, (x2,y2) - второй, (x0,y0) - заданной точки
        a = self.reverse_serif(x1, y1, x2, y2)[1]
        d = 10  # условное ненулевое число
        return self.straight_serif(x0, y0, d, a)

    def speed(self, r1, f1, r2, f2, t, coeff_aim):
        # Скорость движения по изменению координат:
        v_x = coeff_aim * abs(r1*cos(radians(f1)) - r2*cos(radians(f2))) / t
        v_y = coeff_aim * abs(r1*sin(radians(f1)) - r2*sin(radians(f2))) / t
        return (-v_x, -v_y)
