class SolarPanel:
    def __init__(self, serial_number, power_produced):
        self.serial_number = serial_number
        self.power_produced = float(power_produced)


class SolarArray:
    def __init__(self, x, y, solar_panels=[]):
        self.x = x
        self.y = y
        self.solar_panels = list(solar_panels)

    def total_power(self):
        total = 0
        for panel in self.solar_panels:
            total += panel.power_produced
        return total


panel1 = SolarPanel("SN001", 100.5)
panel2 = SolarPanel("SN002", 150.3)
panel3 = SolarPanel("SN003", 120.7)

solar_array = SolarArray(10, 20, [panel1, panel2, panel3])
print(f"Total power of the solar array: {solar_array.total_power()} units")
