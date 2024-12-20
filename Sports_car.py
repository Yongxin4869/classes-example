from Vehicle import Vehicle

class Sports_car(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load

    def display_info(self):
        """Override the parent class method for a Sport Car."""
        return f"Sport car: {self._brand} {self._model}, Max load: {self.max_load} tons ({self._year})"

    def honk(self):
        """Specific implementation for a sport car."""
        return "Vroom Vroom !!!"