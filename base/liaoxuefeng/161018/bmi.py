height = input ('请输入您的身高（M）:') 
weight = input ('请输入您的体重（KG）:') 
height = float(height) 
weight = float(weight) 
bmi = weight/(height*height)
if bmi > 32: 
 print ("您的BMI指数为：", '%.2f' %bmi, '严重肥胖')
elif 28 < bmi <= 32: 
 print ("您的BMI指数为：", '%.2f' %bmi, '肥胖')
elif 25 < bmi <= 28: 
 print ("您的BMI指数为：", '%.2f' %bmi, "过重")
elif 18.5 < bmi <= 25: 
 print ("您的BMI指数为：", '%.2f' %bmi, "正常")
else: 
 print ("您的BMI指数为：", '%.2f' %bmi, "过轻")