# นำเข้าโมดูล
import math

# สร้างฟังก์ชั่นสำหรับการคำนวณ
def calculate_sequence(sequence_type):
    if sequence_type == 1:
        # ลำดับเลขคู่
        result = [2 * i + 1 for i in range(8)]
    elif sequence_type == 2:
        # ลำดับเลขคี่ที่เพิ่มขึ้นทีละ 3
        result = [2 + 3 * i for i in range(6)]
    elif sequence_type == 3:
        # ลำดับเลขลดลงทีละ 10
        result = [30 - 10 * i for i in range(7)]
    elif sequence_type == 4:
        # ลำดับเลขเพิ่มขึ้นทีละ 8
        result = [15 + 8 * i for i in range(6)]
    else:
        result = []

    return result

# แสดงผลลัพธ์
for i in range(1, 5):
    sequence_result = calculate_sequence(i)
    print(f"{i}.{sequence_result}")