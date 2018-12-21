import numpy
from lightdrv import Lightdrv


class Lightmngr(object):
    lightdrv = Lightdrv()

    def set(self, cols):
        ist = numpy.array(self.lightdrv.get())
        soll = numpy.array(cols)

        if numpy.all(numpy.array(self.lightdrv.get()) == soll):
            return

        delta = soll - ist
        norm = numpy.linalg.norm(delta)
        print(delta)
        print(norm)
        delta /= norm
        delta *= 4

        while numpy.linalg.norm(numpy.array(self.lightdrv.get()) - soll) > 4:
            self.lightdrv.set(numpy.array(self.lightdrv.get()) + delta)
        self.lightdrv.set(soll)
