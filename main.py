
print("================================")
print("     QUALITY DEFECT CALCULATOR")
print("================================")

# Get inspection information
total_parts = int(input("Enter total inspected parts: "))
defective_parts = int(input("Enter defective parts: "))

# Calculate results
if total_parts <= 0:
    print("Error: Total parts must be greater than zero.")

elif defective_parts < 0 or defective_parts > total_parts:
    print("Error: Invalid defective parts count.")

else:
    good_parts = total_parts - defective_parts

    defect_rate = (defective_parts / total_parts) * 100
    good_rate = (good_parts / total_parts) * 100

    print("\n========== RESULTS ==========")
    print(f"Total inspected: {total_parts}")
    print(f"Defective parts: {defective_parts}")
    print(f"Good parts: {good_parts}")
    print(f"Defect rate: {defect_rate:.2f}%")
    print(f"Good rate: {good_rate:.2f}%")
    print(f"PPM: {defect_rate * 10000:.0f}")
    print("=============================")
