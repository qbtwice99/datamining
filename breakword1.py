from underthesea import word_tokenize
import os

def tokenize(type_): # bỏ folder chứa các bài viết

    path = type_ + "/"
    tokenize_path = "test" +"/"
    breakapath = "Breakword1" + "/thoi-su/"
    apath1 = type_ + "/thoi-su/"
    files = os.listdir(path)
    # print(files)
    k= os.path.join
    file2=[k(path, f) for f  in os.listdir(path)]
    # for i in files:
        # path2 = path+ i +"/"
    path3 = os.listdir(apath1)
        # print(path2)
        # for file in file2:
            
            # print(f'Tokenize file:{file}')
    print("working")
    for i in path3:
                # print(i)
                
        with open(f'{apath1}/{i}', 'r', encoding='utf-8') as fread,\
                open(f'{breakapath}{i}', 'w', encoding='utf-8') as fwrite:
            for line in fread:
                text = word_tokenize(line, format='text')
                fwrite.write(text + "\n")

def tokenize_(data): # Hàm này nếu m muốn tách chỉ 1 văn bản thì bỏ văn bản đó vào
    return word_tokenize(data, format="text")

tokenize(type_="data/articles")
if __name__ == "__main__":
    print('Done')
