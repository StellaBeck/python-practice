raw = input("Enter numbers separated by commas: ")
values = [float(x.strip()) for x in raw.split(",") if x.strip()]
if values:
    print("Count:", len(values))
    print("Min:", min(values))
    print("Max:", max(values))
    print("Average:", sum(values) / len(values))
else:
    print("No numbers entered")
