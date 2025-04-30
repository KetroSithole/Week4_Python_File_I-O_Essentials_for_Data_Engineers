with open(r'C:\Users\Ketro Sithole\OneDrive - University of Pretoria\Zaio_Institute_of_Technology\Week4\sample_data\data_1.txt', 'r') as file :
    for x in file : 
        name ,age , city=x.strip().split(',')
        print(f"Name: {name}, Age: {age}, City: {city}")
        
   