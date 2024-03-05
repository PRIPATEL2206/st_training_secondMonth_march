rl1=[1,2,3]
rd1={
    1:"a",
    2:"b"
}
rs1={1,2,3}
print(f"{rl1} - {rd1} - {rs1}")

rl2=rl1
rl2[0]=0

rd2=rd1
rd2[1]="c"

rs2=rs1
rs2.add(4)

print(f"{rl1} - {rd1} - {rs1}")

