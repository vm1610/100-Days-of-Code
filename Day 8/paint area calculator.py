
# 🚨 Don't change the code below 👇
def paint_calc(height,width,cover):
    area=height*width
    num_cans=area//cover
    print(f"you'll need {num_cans} of paint")

def main():
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)
main()

