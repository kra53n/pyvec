from math import sin, cos, atan2, radians, degrees, sqrt


class Vec2:
    def __init__(self, x: float = 0, y: float = 0, angle: int = 0, ln: float = 0):
        self._x = x
        self._y = y
        self._angle = angle
        self._ln = ln
        assert self._ln >= 0, 'Vec len can be only positive number or equals 0'

        self._process_args()

    def __str__(self):
        return f'Vec(x={self._x}, y={self._y})'

    def __len__(self):
        return self._ln

    def __add__(self, other):
        return self._change_val(other, '+')

    def __iadd__(self, other):
        return self._change_val(other, '+')

    def __sub__(self, other):
        return self._change_val(other, '-')

    def __isub__(self, other):
        return self._change_val(other, '-')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val
        self._set_ln_by_coords()
        self._set_angle_by_coords()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val
        self._set_ln_by_coords()
        self._set_angle_by_coords()

    @property
    def angle(self):
        return degrees(self._angle)

    @angle.setter
    def angle(self, val):
        self._angle = radians(val)
        self._set_coords_by_angle()

    @property
    def ln(self):
        return self._ln

    @ln.setter
    def ln(self, val):
        self._ln = val
        self._set_coords_by_angle()

    def _process_args(self):
        if self._x or self._y:
            self.x = self._x
            self.y = self._y
            return
        if self._angle and self._ln:
            self.angle = self._angle
            return
        if self._ln:
            self.ln = self._ln
            return

    def _change_val(self, other, action: str):
        assert type(other) in (type(self), float, int), 'Bad type, possibles: Vec, float, int'
        assert action in ('+', '-'), 'Unpossible operation, possibles: +, -'

        v = Vec2(x=self.x, y=self.y)
        if type(self) == type(other):
            exec(f'v.x {action}= other.x')
            exec(f'v.y {action}= other.y')
        if type(other) in (float, int):
            v.angle = eval(f'v.angle {action} other')
        return v

    def _set_ln_by_coords(self):
        self._ln = sqrt(self._x*self._x + self._y*self._y)

    def _set_angle_by_coords(self):
        self._angle = atan2(self._y, self._x)

    def _set_coords_by_angle(self):
        self._x = self._ln * cos(self._angle)
        self._y = self._ln * sin(self._angle)
