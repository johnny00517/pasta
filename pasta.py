import os   #operating system


#讀取檔案
def read_file(filename):
    food = []
    with open(filename, 'r', encoding='utf-8')as f:
            for line in f:
                if '商品,價格' in line:
                    continue   #continue跟break都只能寫在迴圈裡   #跳到下一迴的意思(在本例子就是跳過7 8行)
                name , price = line.strip().split(',')         #.strip去除換行符號  #.split(',')用逗點來切割  
                food.append([name,price])
    return food

#讓使用者輸入
def user_input(food):
    while True:
        name = input('商品名稱: ')
        if name == 'q':
            break
        price = input('商品價格: ')
        food.append([name,price])
    print(food)
    return food

#印出購買紀錄
def print_products(food):
    for foood in food:
        print('商品:', foood[0], '為', foood[1], '元')

#寫入檔案
def write_file(filename, food):
    with open(filename, 'w', encoding='utf-8')as f:        #.cvs可以用excel打開  #encoding='utf-8'  編碼
        f.write('商品,價格\n')
        for foood in food:
            f.write(foood[0] + ',' + foood[1] + '\n')

#主要程式碼
def main():
    filename = 'pasta.csv'
    if os.path.isfile(filename):  #檢查檔案在不在
        print('找到檔案了!')
        food = read_file(filename)
    else:
        print('找不到檔案!')  

    food = user_input(food)
    print_products(food)
    write_file('pasta.csv', food)

main()