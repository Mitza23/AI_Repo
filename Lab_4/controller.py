from domain import Map, Drone


class Controller:
    def __init__(self):
        self.drone = None
        self.map = None

    def read_file(self, file_name):
        with open(file_name, 'r') as fi:
            # Drone
            line = fi.readline()
            x, y = (int(s) for s in line.split())
            line = fi.readline()
            energy = int(line.strip())
            self.drone = Drone(x, y, energy)

            # Map
            line = fi.readline()
            n, m = (int(s) for s in line.split())
            self.map = Map(n, m)
            for i in range(n):
                line = fi.readline()
                tokens = line.split(" ")
                for j, val in enumerate(tokens):
                    self.map.set_cell(i, int(j), int(val))

            # Sensors
            line = fi.readline()
            self.map.sensor_count = int(line.strip())
            for i in range(self.map.sensor_count):
                line = fi.readline()
                x, y = (int(s) for s in line.split())
                self.map.sensors.append((x, y))
