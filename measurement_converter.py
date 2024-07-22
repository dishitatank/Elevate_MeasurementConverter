class LengthConverter:
    conversion_factors = {
        'meter': 1.0,
        'kilometer': 0.001,
        'centimeter': 100.0,
        'millimeter': 1000.0,
        'mile': 0.000621371,
        'yard': 1.09361,
        'foot': 3.28084,
        'inch': 39.3701
    }

    @staticmethod
    def convert(from_unit, to_unit, value):
        if from_unit not in LengthConverter.conversion_factors or to_unit not in LengthConverter.conversion_factors:
            raise ValueError("Invalid units")
        base_value = value / LengthConverter.conversion_factors[from_unit]
        return base_value * LengthConverter.conversion_factors[to_unit]

class WeightConverter:
    conversion_factors = {
        'kilogram': 1.0,
        'gram': 1000.0,
        'milligram': 1000000.0,
        'pound': 2.20462,
        'ounce': 35.274
    }

    @staticmethod
    def convert(from_unit, to_unit, value):
        if from_unit not in WeightConverter.conversion_factors or to_unit not in WeightConverter.conversion_factors:
            raise ValueError("Invalid units")
        base_value = value / WeightConverter.conversion_factors[from_unit]
        return base_value * WeightConverter.conversion_factors[to_unit]

class VolumeConverter:
    conversion_factors = {
        'liter': 1.0,
        'milliliter': 1000.0,
        'cubic_meter': 0.001,
        'cubic_centimeter': 1000.0,
        'gallon': 0.264172,
        'quart': 1.05669,
        'pint': 2.11338,
        'cup': 4.22675,
        'fluid_ounce': 33.814
    }

    @staticmethod
    def convert(from_unit, to_unit, value):
        if from_unit not in VolumeConverter.conversion_factors or to_unit not in VolumeConverter.conversion_factors:
            raise ValueError("Invalid units")
        base_value = value / VolumeConverter.conversion_factors[from_unit]
        return base_value * VolumeConverter.conversion_factors[to_unit]

class TemperatureConverter:
    @staticmethod
    def convert(from_unit, to_unit, value):
        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                return (value * 9/5) + 32
            elif to_unit == 'kelvin':
                return value + 273.15
        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return (value - 32) * 5/9
            elif to_unit == 'kelvin':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                return value - 273.15
            elif to_unit == 'fahrenheit':
                return (value - 273.15) * 9/5 + 32
        else:
            raise ValueError("Invalid units")

class MeasurementConverter:
    def __init__(self):
        self.converters = {}

    def add_converter(self, unit_type, converter):
        self.converters[unit_type] = converter

    def convert(self, unit_type, from_unit, to_unit, value):
        if unit_type in self.converters:
            return self.converters[unit_type].convert(from_unit, to_unit, value)
        else:
            raise ValueError(f"No converter available for {unit_type}")

def display_menu():
    print("Measurement Converter")
    print("=====================")
    print("1. Length")
    print("2. Weight")
    print("3. Volume")
    print("4. Temperature")
    print("5. Exit")

def get_unit_type(choice):
    unit_types = {
        '1': 'length',
        '2': 'weight',
        '3': 'volume',
        '4': 'temperature'
    }
    return unit_types.get(choice)

def display_units(unit_type):
    units = {
        'length': ['meter', 'kilometer', 'centimeter', 'millimeter', 'mile', 'yard', 'foot', 'inch'],
        'weight': ['kilogram', 'gram', 'milligram', 'pound', 'ounce'],
        'volume': ['liter', 'milliliter', 'cubic_meter', 'cubic_centimeter', 'gallon', 'quart', 'pint', 'cup', 'fluid_ounce'],
        'temperature': ['celsius', 'fahrenheit', 'kelvin']
    }
    print(f"Available units for {unit_type}:")
    for unit in units[unit_type]:
        print(f"- {unit}")

def main():
    converter = MeasurementConverter()
    converter.add_converter('length', LengthConverter())
    converter.add_converter('weight', WeightConverter())
    converter.add_converter('volume', VolumeConverter())
    converter.add_converter('temperature', TemperatureConverter())

    while True:
        display_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == '5':
            print("Exiting the Measurement Converter. Goodbye!")
            break

        unit_type = get_unit_type(choice)
        if not unit_type:
            print("Invalid choice. Please try again.")
            continue

        display_units(unit_type)
        from_unit = input("Enter unit to convert from: ").strip().lower()
        to_unit = input("Enter unit to convert to: ").strip().lower()
        try:
            value = float(input("Enter value to convert: "))
            result = converter.convert(unit_type, from_unit, to_unit, value)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        except ValueError as e:
            print(e)

        repeat = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you for using the Measurement Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()
