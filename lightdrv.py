from pca9685_driver import Device


class Lightdrv(object):
    val = [0.0, 0.0, 0.0, 0.0]
    dev = Device(0x40)

    def set(self, vec):
        for i in range(0, len(vec)):
            if (vec[i] < 0) | (vec[i] > 4095):
                continue
	    self.val = vec
            try:
                self.dev.set_pwm(i, int(vec[i]))
            except Exception:
                pass

    def get(self):
        return self.val
