# Date: 27/01/2021
# Classify image 

# Library
import os 
import shutil

# Nhập dữ liệu
def inp():
    # Nhập đia chỉ folder ảnh gốc cần chia 
    root_image_dir = r"C:\Users\Admin\Desktop\My Hust\Ban Vu ao do Top 2412" #input("Name of directory of original iamge folder: ") 
    # Nhập địa chỉ chứa folder kết quả ví dụ: dir = r"C:\Users\Admin\Desktop\My Hust" thì folder sẽ nằm trong ý không cần tự tạo nhé
    re_image_dir = r"C:\Users\Admin\Desktop\My Hust\Note\t\ReTop"  #input("Name of directory of result folder: ")
    # Số lượng subject 
    num_sub = int(input("Number of subject: "))
    count = num_sub
    # Danh sách tên subject
    list_sub = []
    # Hướng chụp 
    list_dire = []
    dire = int(input("Number of directory which we take the photo: "))
    print("""Now we input directory which we take the photo please correct order
             For example: if in your phone left before right, please input left before right
          """)
    while dire != 0:
        list_dire.append(input("Directory: "))
        dire -= 1
        
    while count != 0:
        # Name file
        name_sub = input("Name of subject: ")
        # Số vị trí chụp
        num_place = int(input("Number of place: "))
        # Add tên file, số vị trí chụp
        list_sub.append([name_sub, num_place])
        count -= 1
    return root_image_dir, re_image_dir, num_sub, list_sub, list_dire

def check(gesture):
    l1 = list(range(2,18)) + list(range(19,32))
    l2 = [1, 18]
    l3 = 32
    if gesture in l1:
        return 3
    elif gesture in l2:
        return 6
    else:
        return 5
        
def prepare_out():
    l = ["All", "Half"]
    root_image_dir, re_image_dir, num_sub, list_sub, list_dire = inp()
    print("Input successfully")
    # Kiếm tra folder name "Datasets" có tồn tại không
    if os.path.exists(os.path.join(re_image_dir, "Datasets")):
        # Xóa toàn bộ dữ liệu trong file tồn tại
        shutil.rmtree(os.path.join(re_image_dir, "Datasets"))
        os.mkdir(os.path.join(re_image_dir, "Datasets"))
    else:
        os.mkdir(os.path.join(re_image_dir, "Datasets"))
    # Tạo gesture
    gesture = 1
    # Địa chỉ của folder Datasets
    img_dir = os.path.join(re_image_dir, "Datasets")
    # Hoàn thiện folder kết quả
    while gesture <= 32:
        # Địa chỉ của gesture
        ges_dir = os.path.join(img_dir, str(gesture))
        # Tạo folder gesture
        os.mkdir(ges_dir)
        for dire in list_dire:
            os.mkdir(os.path.join(ges_dir, dire))
            for sub in list_sub:
                path = os.path.join(ges_dir, dire)
                os.mkdir(os.path.join(path, sub[0]))
                for body in l:
                    re_path = os.path.join(path, sub[0])
                    os.mkdir(os.path.join(re_path, body))
        gesture += 1
    print("Done for prepare")
    print("-----------------------------------------------------")
    # Classify image
    print("Start classify image")
    gesture = 1
    run = 0
    limit = 0
    idx = 0
    list_sub_n = []
    list_image = os.listdir(root_image_dir)
    for i in list_sub:
        list_sub_n += [i[0]] * i[1]
        
    """
    while gesture <= 32:
        ges_dir = os.path.join(img_dir, str(gesture))
        limit = check(gesture) - 1
        print(limit)
        for sub in list_sub_n:
            for d in list_dire:
                path = os.path.join(ges_dir, d)
                path_n = os.path.join(path, sub)
                for body in l:
                    path_f = os.path.join(path_n, body)
                    while run <= limit:
                        shutil.move(os.path.join(root_image_dir, list_image[idx]), os.path.join(path_f, list_image[idx]))
                        idx += 1
                        run += 1
                        print(run)
                    run = 0
        print("Done {}".format(gesture))
        gesture += 1
    """
    for sub in list_sub_n:
        while gesture <= 32:
            ges_dir = ges_dir = os.path.join(img_dir, str(gesture))
            limit = check(gesture) - 1
            
            for d in list_dire:
                path = os.path.join(ges_dir, d)
                path_n = os.path.join(path, sub)
                for body in l:
                    path_f = os.path.join(path_n, body)
                    while run <= limit:
                        shutil.move(os.path.join(root_image_dir, list_image[idx]), os.path.join(path_f, list_image[idx]))
                        idx += 1
                        run += 1
                        print(run)
                    run = 0
            print("Done {}".format(gesture))
            gesture += 1
        gesture = 1
    print("Done all")
prepare_out()
