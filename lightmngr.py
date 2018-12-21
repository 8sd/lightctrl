import numpy
from lightdrv import Lightdrv


class Lightmngr(object):
    lightdrv = Lightdrv()
    speed = 4

    def getReal(self):
        return self.lightdrv.getReal()

    def set(self, cols):
        ist = numpy.array(self.lightdrv.get())
        soll = numpy.array(cols)

        if numpy.all(numpy.array(self.lightdrv.get()) == soll):
            return

        delta = soll - ist
        norm = numpy.linalg.norm(delta)
        delta /= norm
        delta *= self.speed

        while numpy.linalg.norm(numpy.array(self.lightdrv.get()) - soll) > 4:
            self.lightdrv.set(numpy.array(self.lightdrv.get()) + delta)
        self.lightdrv.set(soll + [0.0, 0.0, 0.0, 0.0])
