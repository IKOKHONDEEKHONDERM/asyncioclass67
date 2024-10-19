import asyncio
import math


async def calculate_distance(other_points, reference_point):
    x1, y1 = reference_point
    x2, y2 = other_points

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"distance from {reference_point} to {other_points} distance: {distance:.2f}")
    return distance


async def main():
    reference_point = (3, 3)
    other_points = [(2, 8), (3, 7), (4, 6), (3, 5), (6, 9), (7, 4), (5, 3), (8, 2), (6, 1), (1, 2)]
    
   
    distances = await asyncio.gather(*[calculate_distance(village, reference_point) for village in other_points])
    min_distance = min(distances)
    max_distance = max(distances)
    min2_distance = (sorted(distances)[0])
   
    
    closest_village = other_points[distances.index(min_distance)]
    farthest_village = other_points[distances.index(max_distance)]
    
    print(f"\n หมู่บ้านที่ใกล้ตำแหน่ง (5, 3) ที่ระยะทาง {min2_distance:.2f}")
    print(f" หมู่บ้านที่ใกล้ตำแหน่ง {closest_village} ที่ระยะทาง {min_distance:.2f}")
    print(f"หมู่บ้านที่ไกล {farthest_village} ที่ระยะทาง {max_distance:.2f}")

asyncio.run(main())
