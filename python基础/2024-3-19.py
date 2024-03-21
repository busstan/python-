# class C0:
#     name = "C0"
# class C2(C0):
#     num = 2
# class C1:
#     num = 1
# class C3:
#     num = 3
# class C4(C3, C2, C1):
#     pass

# c = C4()
# print(c.num, c.name)

# class Student:
#     def int (self, name, job = None, time = 0.00, time_effective = 0.00):
#         self.name = name
#         self.job = job
#         self.time = time
#         self.time_effective = time_effective

#     def count_time(self, hour, rate):
#         self.time += hour
#         self.time_effective += hour * rate

# class programmer(Student):
#     time_effective = 1
#     job = "programmer"


class Book :
    def __init__(self, name, author, recommendation, status):
        self.name = name
        self.author = author
        self.recommendation = recommendation
        self.status = status
    def show_info(self):
        if self.status == 0:# 如果属性为0
            status = "未借出"
        else:
            status = "已借出"
        return "书名:%s\n作者:%s\n推荐指数:%s\n状态:%s"%(self.name, self.author, self.recommendation, status)
    
class BookManager:
    books = []
    def __init__(self):
        book1 = Book("Python编程从入门到实践", "埃里克·马瑟斯", 9.5, 0)
        book2 = Book("数据结构与算法分析", "Mark Allen Weiss", 9.0, 0)
        book3 = Book("计算机网络", "Andrew S. Tanenbaum", 8.5, 0)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    def menu(self): #查询所有书、添加、借阅、归还、退出系统
        print("欢迎使用西柚二手书借阅系统！")
        while True:
            print('1:查询所有书籍\n 2:添加书籍\n 3:借阅书籍\n 4:归还书籍\n 5:退出系统\n')
            choice = int(input("请输入你的选择："))
            if choice == 1:
                self.show_all()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                break
            else:
                print("输入有误，请重新输入！") 
    def show_all(self):
        for book in self.books:
            print(book.show_info())
    def add_book(self):
        new_name = input("请输入书名：")
        new_author = input("请输入作者：")
        new_recommendation = input("请输入推荐指数：")
        new_book = Book(new_name, new_author, new_recommendation, 0)
    def lend_book(self):
        name = input("请输入书名：")
        book = self.find_book(name)
        if book.status == 0:
            book.status = 1
            print("借阅成功！")
        else:
            print("该书籍已经被借阅！")
    def return_book(self):
        name = input("请输入书名：")
        book = self.find_book(name)
        if book.status == 1:
            book.status = 0
            print("归还成功！")
        else:
            print("该书籍未被借阅！")
    def find_book(self, name):
        for book in self.books:
            if book.name == name:
                return book
        print("没有找到该书籍！")
        return None
# class Book:
#     def __init__(self, name, author, recommendation, status):
#         self.name = name
#         self.author = author

# book = Book("name", "author", "recommendation", 0)
# print (book.show_info())

# manager = BookManager()
# manager.menu()
    
class FictionBook(Book):
    def __init__(self, name, author, recommendation, status, type):
        super().__init__(name, author, recommendation, status)
        self.type = "玄幻类"
    def show_info(self):
        return f"书名：{self.name}\n作者：{self.author}\n推荐指数：{self.recommendation}\n状态：{'可借阅' if self.status == 0 else '已被借阅'}\n类型：{self.type}"
    