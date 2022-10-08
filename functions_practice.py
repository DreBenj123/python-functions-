def hello():
    print("Hello there!")


def pack(wolves, bears, lions):
    return [wolves, bears, lions]


def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("Lunch is empty")
    else:
        for i in range(len(lunch_list)):
            if i == 0:
                print(f"First I eat {lunch_list[0]}")
        else:
            print(f"Next I Eat {lunch_list[i]}")


hello()
print(pack("wolves", "bears", "lions"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["chicken"])
eat_lunch(["Fig Bar", "green beans", "pie", "pancakes"])
