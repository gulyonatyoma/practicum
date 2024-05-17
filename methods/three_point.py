
def m_three_point(obj, is_catch):
    table = obj.data
    if is_catch == False:
        (x_aim, y_aim) = obj.math_f.straight_serif(
            obj.xb, obj.yb, obj.r0, obj.f0)

        t_test = -3
        x_aim += obj.v_x * obj.t
        y_aim += obj.v_y * obj.t
        (r_c, f_c) = (0, 0)

        while t_test < 0:
            t_test += obj.t

            x_aim += obj.v_x * obj.t
            y_aim += obj.v_y * obj.t
            (r_aim, f_aim) = obj.math_f.reverse_serif(
                obj.xb, obj.yb, x_aim, y_aim)

            r_c += obj.v_c * obj.t
            f_c = f_aim
            (x_c, y_c) = obj.math_f.straight_serif(
                obj.xb, obj.yb, r_c, f_c)

            d = obj.math_f.distance_twopoints(x_c, y_c, x_aim, y_aim)

            f = {"moment": t_test, "aimPhi": f_aim, "aimR": r_aim, "aimX": x_aim, "aimY": y_aim,
                 "catcherPhi": f_c, "catcherRho": r_c, "catcherX": x_c, "catcherY": y_c, "distance": d}
            table["fly"].append(f)
    else:
        (x_aim, y_aim) = obj.math_f.straight_serif(
            obj.xb, obj.yb, obj.r0, obj.f0)

        t_test = -3
        x_aim += obj.v_x * obj.t
        y_aim += obj.v_y * obj.t
        (r_c, f_c) = (0, 0)

        while x_aim > obj.xb:
            t_test += obj.t

            x_aim += obj.v_x * obj.t
            y_aim += obj.v_y * obj.t
            (r_aim, f_aim) = obj.math_f.reverse_serif(
                obj.xb, obj.yb, x_aim, y_aim)

            r_c = 0
            f_c = 0
            (x_c, y_c) = (obj.xb, obj.yb)

            d = obj.math_f.distance_twopoints(x_c, y_c, x_aim, y_aim)

            f = {"moment": t_test, "aimPhi": f_aim, "aimR": r_aim, "aimX": x_aim, "aimY": y_aim,
                 "catcherPhi": f_c, "catcherRho": r_c, "catcherX": x_c, "catcherY": y_c, "distance": d}
            table["fly"].append(f)

        for i in range(2):
            t_test += obj.t

            x_aim += obj.v_x * obj.t
            y_aim += obj.v_y * obj.t
            (r_aim, f_aim) = obj.math_f.reverse_serif(
                obj.xb, obj.yb, x_aim, y_aim)

            r_c += obj.v_c * obj.t
            f_c = f_aim
            (x_c, y_c) = obj.math_f.straight_serif(
                obj.xb, obj.yb, r_c, f_c)

            d = obj.math_f.distance_twopoints(x_c, y_c, x_aim, y_aim)

            f = {"moment": t_test, "aimPhi": f_aim, "aimR": r_aim, "aimX": x_aim, "aimY": y_aim,
                 "catcherPhi": f_c, "catcherRho": r_c, "catcherX": x_c, "catcherY": y_c, "distance": d}
            table["fly"].append(f)

    delta_d_old, delta_d_new = 0, 0
    flag = 0

    while d > obj.max_dist:
        # Проверка на отсутствие беск цикла
        if flag == 1 and (delta_d_new - delta_d_old) < 0:
            return ("Method lose")
        delta_d_new = d - obj.max_dist
        delta_d = delta_d_new - delta_d_old
        if delta_d < 0:
            flag = 1
        delta_d_old = delta_d_new

        t_test += obj.t

        x_aim += obj.v_x * obj.t
        y_aim += obj.v_y * obj.t
        (r_aim, f_aim) = obj.math_f.reverse_serif(
            obj.xb, obj.yb, x_aim, y_aim)

        a = obj.math_f.circle_and_line(
            obj.xb, obj.yb, x_aim, y_aim, x_c, y_c, abs(obj.v_c))
        if len(a) == 4:
            d1 = obj.math_f.distance_twopoints(a[0], a[1], x_aim, y_aim)
            d2 = obj.math_f.distance_twopoints(a[2], a[3], x_aim, y_aim)
            if d1 > d2:
                d = d2
                x_c = a[2]
                y_c = a[3]
            else:
                d = d1
                x_c = a[0]
                y_c = a[1]

        elif len(a) == 2:
            x_c = a[0]
            y_c = a[1]
            d = obj.math_f.distance_twopoints(x_c, y_c, x_aim, y_aim)
        (r_c, f_c) = obj.math_f.reverse_serif(obj.xb, obj.yb, x_c, y_c)

        f = {"moment": t_test, "aimPhi": f_aim, "aimR": r_aim, "aimX": x_aim, "aimY": y_aim,
             "catcherPhi": f_c, "catcherRho": r_c, "catcherX": x_c, "catcherY": y_c, "distance": d}
        table["fly"].append(f)

    return table
