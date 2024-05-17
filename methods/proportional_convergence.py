
def m_proportional_convergence(obj, is_catch, k):
    table = obj.data
    if is_catch == False:
        (x_aim, y_aim) = obj.math_f.straight_serif(
            obj.xb, obj.yb, obj.r0, obj.f0)

        t_test = -3
        x_aim += obj.v_x * obj.t
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
    f0=obj.math_f.angle_between_lines(x_aim, y_aim, x_c, y_c, 0, 0, 5, 0)
    x_aim1 = obj.v_x * obj.t+x_aim
    y_aim1 = obj.v_y * obj.t+y_aim
    f1=obj.math_f.angle_between_lines(x_aim1, y_aim1, x_c, y_c, 0, 0, 5, 0)
    delta_f=(f1-f0)/obj.t
    delta_teta=k*delta_f
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
        delta_f=(f1-f0)/obj.t
        delta_teta=k*delta_f
        teta_0=obj.math_f.angle_between_lines(x_aim, y_aim, x_c, y_c, 0, 0, 5, 0)
        x_aim += obj.v_x * obj.t
        y_aim += obj.v_y * obj.t
        (r_aim, f_aim) = obj.math_f.reverse_serif(
            obj.xb, obj.yb, x_aim, y_aim)
        teta=delta_teta*obj.t+teta_0
        x1, y1=obj.math_f.straight_serif(x_c, y_c, -obj.max_dist+1, teta)
        x2, y2=obj.math_f.straight_serif(x_c, y_c, obj.max_dist+1, teta)
        a= obj.math_f.circle_and_line(
            x1, y1, x2, y2, x_c, y_c, abs(obj.v_c))

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
