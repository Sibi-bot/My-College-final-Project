age=input("Enter the age :")
gulcose=float(input("\nEnter the value of Glucose :"))
blood_pressure=float(input("\nEnter the value of blood pressure :"))
skin_thickness=float(input("\nEnter the value of skin thickness :"))
insulin=float(input("\nEnter the value of insulin :"))
bmi=float(input("\nEnter the value of BMI :"))
diabetes_pedigree_function=float(input("\nEnter the value of Diabetes Pedigree Function :"))


affected_by_diabetes=float(input("\nEnter the value of Affected by diabetes :"))

#lingustic value 
if (0<=affected_by_diabetes<=0.34):
    print(age)
    print("\n",affected_by_diabetes)
    print("\nVery Low")
    l=("Very low")
elif (0<=affected_by_diabetes<=0.44):
    print(age)
    print("\n",affected_by_diabetes)
    print("\nLow")
    l=("Low")
elif (0.45<=affected_by_diabetes<=0.49):
    print(age)
    print("\n",affected_by_diabetes)
    print("\nNormal")
    l=("Normal")
elif (0.50<=affected_by_diabetes<=0.59):
    print(age)
    print("\n",affected_by_diabetes)
    print("\nHigh")
    l=("High")
else :
    print(age)
    print("\n",affected_by_diabetes)
    print("\nVery High")
    l=("Very high")
 
#scale point  
if(l=="Very low"):
    scale_point=1
elif(l=="Low"):
    scale_point=2
elif(l=="Normal"):
    scale_point=3
elif(l=="High"):
    scale_point=4
elif(l=="Very high"):
    scale_point=5
else:
    print("\nInvalid function")

print("\nScale point :",scale_point)
print("\nAffected by diabetics :",affected_by_diabetes)
print("\nlinguistic value of POD :",l)

weightage=0.142
weightage=float(weightage)

print("\nGlucose = Non-Benificial")
print("\nBlood Pressure = Non-Benificial")
print("\nSkin thicness = Non-Benificial")
print("\nInsulin = Benificial")
print("\nScale Point = Non-Benificial")
print("\nBMI = Non-Benificial")
print("\nDiabetes Pedigree Function = Non-Benificial")

max_insulin=float(input("\nEnter the maximum value of insuline :"))
min_glucose=float(input("\nEnter the minimam value of glucose :"))
min_blood_pressure=float(input("\nEnter the minimum value of Blood Pressure :"))
min_skin_thickness=float(input("\nEnter the minimum value of Skin thickness :"))
min_scale_point=float(input("\nEnter the minimum value of Scale point :"))
min_bmi=float(input("\nEnter the minimum value of BMI :"))
min_diabetes=float(input("\nEnter the minimum value of Diabetes pedigree function :"))

a=(min_glucose/gulcose)
a=float(a)
b=(min_blood_pressure/blood_pressure)
b=float(b)
c=(min_skin_thickness/skin_thickness)
c=float(c)
d=(insulin/max_insulin)
d=float(d)
e=(min_scale_point/scale_point)
e=float(e)
f=(min_bmi/bmi)
f=float(f)
g=(min_diabetes/diabetes_pedigree_function)
g=float(g)

print("\nAge :",age)
print("\nGlucose :",a)
print("\nBlood pressure :",b)
print("\nSkin thickness :",c)
print("\nInsulin :",d)
print("\nBMI :",f)
print("\nDiabetes prdigree function :",g)
print("\nScale point :",e)

h=(a*weightage)
h=float(h)
i=(b*weightage)
i=float(i)
j=(c*weightage)
j=float(j)
k=(d*weightage)
k=float(k)
m=(e*weightage)
m=float(m)
n=(f*weightage)
n=float(n)
o=(g*weightage)
o=float(o)

print("\nAge :",age)
print("\nGlucose :",h)
print("\nBlood pressure :",i)
print("\nSkin thickness :",j)
print("\nInsulin :",k)
print("\nBMI :",n)
print("\nDiabetes prdigree function :",o)
print("\nScal_point:",m)

total=(h+i+j+k+m+n+o)
total=float(total)

print("\n",age)
print("Total:",total)