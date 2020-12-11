with open ('numbers.txt') as file:                             
    for line in file:                                          
        a = line.split(' ')                                     
        fizz = int(a[0])                                        
        buzz = int(a[1])                                       
        limit = int(a[2])                                       
        for i in range(1, limit + 1):        
            new_save_from_fb = open('results.txt', 'a')
            if i % fizz == 0 and i % buzz == 0:
                new_save_from_fb.writelines('FB ')
                print('FB', end = ' ')
            elif i % fizz == 0:
                print('F', end = ' ')
                new_save_from_fb.writelines('F ')
            elif i % buzz == 0:
                print('B', end = ' ')
                new_save_from_fb.writelines('B ')
            else:
                p = print (i, end = ' ')
                new_save_from_fb.writelines(str(i)+str(' '))
        print('\n Числа в строке из файла - ' + line)
        new_save_from_fb.writelines('\n Числа в строке из файла - ' + line + '\n') 
        new_save_from_fb.close()

