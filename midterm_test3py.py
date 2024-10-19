import random
import time
import asyncio

class SolarCell:
    def __init__(self, id):
        self.id = id
        self.hardware_readtime = random.randint(1, 3)
        print(f"Solar cell {id} hardware speed: {self.hardware_readtime}")
     
    async def read_voltage(self):
        voltage = round(random.uniform(3.2, 6.0), 2)
        await asyncio.sleep(self.hardware_readtime)
        return voltage
    
async def read_from_solar_cells(solar_cells):
    try:
        while True:
            tasks = []
            for solar_cell in solar_cells:
                tasks.append(read_and_print_voltage(solar_cell))
            await asyncio.gather(*tasks)  # Run all tasks concurrently
    except KeyboardInterrupt:
        print("\nProgram stopped")

async def read_and_print_voltage(solar_cell):
    voltage = await solar_cell.read_voltage()
    print(f"{time.ctime()} Solar Cell #{solar_cell.id} Voltage: {voltage} V")

if __name__ == "__main__":
    numcells = 5
    print(f"Number of solar cells created: {numcells}")

    solar_cells = [SolarCell(i+1) for i in range(numcells)]
    asyncio.run(read_from_solar_cells(solar_cells))
