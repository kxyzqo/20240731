class BMI():
    def __init__(self,name:str,height:float,weight:float):
        self.__name = name    #實體attribute(不可讓實體讀和寫)
        self.height = height  #實體attribute(可以讀出 修改)
        self.weight = weight

    @property #大部分可讀但不可改 #不要()
    def name(self)->str:
        return self.__name

    def bmi(self)->float:
        return round(self.weight / (self.height/100)**2, ndigits=2)
    
    def grade(self)->str:
        self.grade = self.bmi() #呼叫bmi的值

        if self.grade < 18.5:
            return "體重過輕"
        elif self.grade < 24:
            return "正常範圍"
        elif self.grade < 27:
            return "過重"
        elif self.grade < 30:
            return "輕度肥胖"
        elif self.grade < 35:
            return "中度肥胖"
        elif self.grade >= 35:
            return "重度肥胖"
        
    def description(self)->str:
        return f'我的名字叫{self.name}\nBMI為{self.bmi()}\n屬於{self.grade()}'
        
        
while True:
    try:
        name = input("請輸入姓名: ")
        height = float(input('請輸入身高（cm）: '))
        weight = float(input('請輸入體重（kg）: '))

        #建立一個bmi的實體
        ans = BMI(name=name,height=height,weight=weight)
        #myBMI.name = "xxxx" #在@property的情況下會出錯
        print(ans.description())

        
    except ValueError:
        print("格式錯誤，請重新輸入數據")
        continue

    stuff = input("請問是否繼續輸入資料 ('q': 離開, 任意鍵: 繼續)? ")

    if stuff == 'q':
        break

print("應用程式結束")

#這是一個不知道放哪裡所以丟在這裡的補充
#module裡面可放function/class/常數