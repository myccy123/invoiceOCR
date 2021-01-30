
class Base:

    def __init__(self, result):
        self.data = []
        for res in result:
            self.data.append({
                'x': res[0][0][0],
                'y': res[0][0][1],
                'width': res[0][1][0] - res[0][0][0],
                'height': res[0][2][1] - res[0][1][1],
                'text': res[1][0],
                'confidence': res[1][1],
            })
