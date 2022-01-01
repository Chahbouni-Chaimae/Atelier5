class Point:
        def __init__(self, x=0.0, y=0.0):
                self.px = float(x)
                self.py = float(y)
class Segment:
        def __init__(self, x1, y1, x2, y2):
                self.orig = Point(x1, y1)
                self.extrem = Point(x2, y2)
        def __str__(self):
              return ("Segment : [({0}, {1}), ({2}, {3})]"
                           .format(self.orig.px, self.orig.py, self.extrem.px, self.extrem.py))
if __name__ == '__main__':
        s = Segment(1, 2, 3, 4)
        print(s)