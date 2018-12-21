class Lightdrv(object):
    val = [0.0, 0.0, 0.0, 0.0]

    def set(self, vec):
        print(vec)
        self.val = vec

    def get(self):
        return self.val
