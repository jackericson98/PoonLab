
R1 = 1
x2, y2, z2, R2 = 1, 0, 0, 1
x3, y3, z3, R3 = 0, 1, 0, 1
x4, y4, z4, R4 = -1, 0, 0, 1


a1 = 2 * x2
b1 = 2 * y2
c1 = 2 * z2
d1 = 2 * R1 - 2 * R2
f1 = R1 ** 2 - R2 ** 2 + x2 ** 2 + y2 ** 2 + z2 ** 2

a2 = 2 * x3
b2 = 2 * y3
c2 = 2 * z3
d2 = 2 * R1 - 2 * R3
f2 = R1 ** 2 - R3 ** 2 + x3 ** 2 + y3 ** 2 + z3 ** 2

a3 = 2 * x4
b3 = 2 * y4
c3 = 2 * z4
d3 = 2 * R1 - 2 * R4
f3 = R1 ** 2 - R4 ** 2 + x4 ** 2 + y4 ** 2 + z4 ** 2

F = a1 * b2 * c3 - a1 * b3 * c2 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
Fx0 = b1 * c2 * f3 - b1 * c3 * f2 - b2 * c1 * f3 + b2 * c3 * f1 + b3 * c1 * f2 - b3 * c2 * f1
Fx1 = b1 * c2 * d3 - b1 * c3 * d2 - b2 * c1 * d3 + b2 * c3 * d1 + b3 * c1 * d2 - b3 * c2 * d1
Fy0 = -a1 * c2 * f3 + a1 * c3 * f2 + a2 * c1 * f3 - a2 * c3 * f1 - a3 * c1 * f2 + a3 * c2 * f1
Fy1 = -a1 * c2 * d3 + a1 * c3 * d2 + a2 * c1 * d3 - a2 * c3 * d1 - a3 * c1 * d2 + a3 * c2 * d1
Fz0 = a1 * b2 * f3 - a1 * b3 * f2 - a2 * b1 * f3 + a2 * b3 * f1 + a3 * b1 * f2 - a3 * b2 * f1
Fz1 = a1 * b2 * d3 - a1 * b3 * d2 - a2 * b1 * d3 + a2 * b3 * d1 + a3 * b1 * d2 - a3 * b2 * d1


a = Fx1^2 / F^2 + Fy1^2 / F^2 + Fz1^2 / F^2 - 1
b = 2 * Fx0 * Fx1 / F^2 + 2 * Fy0 * Fy1 / F^2 + 2 * Fz0 * Fz1 / F^2 - 2 * R1
c = Fx0^2 / F^2 + Fy0^2 / F^2 + Fz0^2 / F^2 - R1^2