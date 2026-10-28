print("N","N^2","N^3","Square Root",sep="\t")

for n in range(1,16):
    square = n**2
    cube = n**3
    root = n**0.5

    rounded_root = round(root,4)

    print(f'{n}\t{square}\t{cube}\t{rounded_root}')
