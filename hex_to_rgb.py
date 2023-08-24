def main():
   hex_color = input("Color: ")
   int_color = convert(hex_color)
   print(int_color)
   
def convert(hex_color):
    pass

def convert (hex_color):
    r = hex_color[1:3]
    g = hex_color[3:5]
    b = hex_color[5:7]
    r = int(r, 16)
    g = int(g, 16) 
    b = int(b, 16)
    return(r,g,b)

if __name__ == "__main__":
    main()
