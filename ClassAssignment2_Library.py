class ClassAssignment2_class():
    def Subfields():
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for subfields in list:
            print(subfields)

    def OddEven():
        num=int(input("Enter a number: "))
        if num%2==0:
            print(num,"is Even Number")
            result="Even Number"
        else:
            print(num,"is Odd Number")
            result="Odd Number"
        return result   

    def Eligible():
        gender=input("Enter gender:")
        age=int(input("Enter age:"))
        if(gender=="Male"):
            if(age>21):
                print("Eligible")
                msg="Eligible"
            else:
                print("Not Eligible")
                msg="Not Eligible"
        else:
            if(age>18):
                print("Eligible")
                msg="Eligible"
            else:
                print("Not Eligible")
                msg="Not Eligible"
        return msg

    def percentage():
        sub1=float(input("Subject1="))
        sub2=float(input("Subject2="))
        sub3=float(input("Subject3="))
        sub4=float(input("Subject4="))
        sub5=float(input("Subject5="))
        Total=sub1+sub2+sub3+sub4+sub5
        Percentage=(Total/500)*100
        print("Total:",Total)
        print("Percentage:",Percentage)
        return Total,Percentage

    def triangle():
        def area_func():
            height=float(input("Height:"))
            breadth=float(input("Breadth:"))
            Area=(height*breadth)/2
            print("Area formula: (Height*Breadth)/2 ")
            print("Area of Triangle:",Area)
            return Area
        def perimeter_func():
            height1=float(input("Height1:"))
            height2=float(input("Height2:"))
            breadth=float(input("Breadth:"))
            Perimeter=height1+height2+breadth
            print("Perimeter formula: Height1+Height2+Breadth ")
            print("Perimeter of Triangle:",Perimeter)
            return Perimeter
        trianglearea=area_func()
        triangleperimeter=perimeter_func()
        return trianglearea,triangleperimeter

        
            
        
        



    
        
    