import tkinter
import subprocess

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Bhavya123")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Database_Mgmt")
mycursor.execute("USE Database_Mgmt")

#CREATING TABLES
def dealer_info():
    mycursor.execute("CREATE TABLE IF NOT EXISTS DEALER (DL_ID VARCHAR(4) PRIMARY KEY, DL_CMPNY_NAME VARCHAR(50) ,  DL_CONTACT VARCHAR(30) , DL_CITY VARCHAR(25) ,DL_STATE VARCHAR(30))")
dealer_info()

def order_place():
    mycursor.execute("CREATE TABLE IF NOT EXISTS ORDER_P (ORDER_ID VARCHAR(4) , DL_ID VARCHAR(4) , PRODUCT_ID VARCHAR(4) , QTY_ORDER INT)")
order_place()

def bill_query():
    mycursor.execute("Select ORDER_ID ,DL_ID , QTY_ORDER , PRICE from PRODUCTS_Main , ORDER_P WHERE ORDER_P.PRODUCT_ID=PRODUCTS_Main.PRODUCT_ID")

    x = mycursor.fetchall()  
    y = [list(i) for i in x]
    dict1={}
    def pirce_after_discount(w,k):  #w is qty , k is price
        z=w*k
        if w<=50:
            d=0
            t1=z

        elif w>=50 and w<=100:
            d=(2/100)*z
            t1=z-d

        elif w>100 and w<=200:
            d=(5/100)*z
            t1=z-d

        elif w>200 and w<=500:
            d=(20/100)*z
            t1=z-d

        elif w>500:
            d=(25/100)*z
            t1=z-d

        t=(18/100)*t1
        f=t+t1
        return f

    for i in range (len(y)):

        if y[i][1] in dict1.keys():
            a=dict1[y[i][1]]
            f=pirce_after_discount(y[i][2],y[i][3])
            d=a+f
            dict1[y[i][1]] = d

        else:
            a=pirce_after_discount(y[i][2],y[i][3])
            print(y[i][1])
            dict1[y[i][1]] = a

    return dict1



def bill_place():

    mycursor.execute("CREATE TABLE if not exists BILL (BILL_ID  INT  NOT NULL AUTO_INCREMENT PRIMARY KEY, DL_ID VARCHAR(04) , TAX_PER INT , NET_AMOUNT DECIMAL)")
    d=bill_query()
    for key,value in d.items():
        mycursor.execute("INSERT INTO BILL(DL_ID,TAX_PER,NET_AMOUNT) VALUES (%s,%s,%s)",(key,18,value)) 
        mydb.commit()



root = tkinter.Tk()
root.title("Database Record System")

windowWidth = root.winfo_screenwidth()
windowHeight= root.winfo_screenheight()
root.resizable(False,False)
x_pos=int((root.winfo_screenwidth()/2) - (windowWidth/2))
y_pos=int((root.winfo_screenheight()/2) - (windowHeight/2))

root.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")

#PARENT WINDOW FRAMES
# FRAME 1
p_frame1 = tkinter.Frame(root, bg='white',width=int(root.winfo_screenwidth()),height=int(root.winfo_screenheight()/6))
p_frame1.grid(row=0,column=0)

#FRAME 2
p_frame2 = tkinter.Frame(root, bg='royalblue',width=int(root.winfo_screenwidth()),height=int(root.winfo_screenheight()/3))
p_frame2.grid(row=1,column=0)

#FRAME 3
p_frame3 = tkinter.Frame(root, bg='white',width=int(root.winfo_screenwidth()),height=int(root.winfo_screenheight()/2))
p_frame3.grid(row=2,column=0)

#CHILDREN OF FRAME 1
#label1
Label1=tkinter.Label(p_frame1,text="WELCOME!!",font=("Bodoni MT",30,'bold'),bg='white',fg='navyblue')
Label1.place(x=int(root.winfo_screenwidth()-1250), y=int(root.winfo_screenheight()-700))


Label2=tkinter.Label(p_frame2,text="FINE THREADS APPAREL",font=("Monotype Corsiva",50,'underline'),bg='royalblue',fg='white')
x_pos = int((windowWidth/2-Label2.winfo_width()/2)-380)
y_pos = int((windowHeight/2-Label2.winfo_height()/2)-285)
Label2.place(x=x_pos,y=y_pos)

#label3
Label3=tkinter.Label(root,text="-Quality Never Goes Out Of Style",font=("Monotype Corsiva",20,'italic'),bg='royalblue',fg='white')
Label3.place(x=800,y=300)

#FUNCTIONS
#function for buttons

#func for about_us
def _btn1():
    toplevel=tkinter.Toplevel()
    toplevel.title("ABOUT US")

    windowWidth = toplevel.winfo_screenwidth()
    windowHeight=toplevel.winfo_screenheight()
    toplevel.resizable(False,False)
    x_pos=int((toplevel.winfo_screenwidth()/2) - (windowWidth/2))
    y_pos=int((toplevel.winfo_screenheight()/2) - (windowHeight/2))
    
    toplevel.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")

    toplevel.configure(background='lightsteelblue')
    
    #ABOUT US WINDOW
    #adding text to about_us
    Label4=tkinter.Label(toplevel,text="WANNA KNOW ABOUT US??",font=("Ubuntu",22,'bold','underline'),bg='lightsteelblue',fg='navyblue')
    Label4.place(x=10,y=10)

    #TEXT TO BE ADDED
    txt=("Launched in 2020, FINE THREAD APPAREL offers a wide range of apparel to fit any person’s unique sense of style.\n"
        "Our clothing and accessories are carefully curated to provide our customers the latest fashions.\n"
        "To keep our customers in style we post new arrivals daily, as well as offer stylist picks to help any indecisive shoppers.\n"
        "FINE THREAD APPAREL is a fashionista’s best place to create the perfect wardrobe.\n"
        "Beyond helping you look your best, FINE THREAD APPAREL\n"
        "strives to make every purchase a positive experience.\n"
        "Our top priorities are excellent customer service,\n"
        "exceptionally quick order processing,\n"
        "ultra fast shipping times, and a hassle-free return policy.\n"
        "We value your feedback, whether positive or constructive and\n"
        "we are continuously working to improve your experience.\n"
        "If you are a first-time visitor or long-standing customer,\n"
        "we hope you will be thrilled with every aspect of your FINE THREAD APPAREL shopping experience.")

    Label5=tkinter.Label(toplevel,text=txt,font=("Ubuntu",15),bg='lightsteelblue',fg='navyblue')
    Label5.place(x=180,y=70)

    toplevel.mainloop()

#func for exit
def _btn2():
    root.destroy()

#func for admin
def _btn3():
    toplevel2=tkinter.Toplevel()
    toplevel2.title("ADMIN")

    windowWidth = toplevel2.winfo_screenwidth()
    windowHeight=toplevel2.winfo_screenheight()
    toplevel2.resizable(False,False)
    x_pos=int((toplevel2.winfo_screenwidth()/2) - (windowWidth/2))
    y_pos=int((toplevel2.winfo_screenheight()/2) - (windowHeight/2))
    
    toplevel2.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")

    #ADMIN WINDOW
    #frame for admin window
    admin_frame = tkinter.Frame(toplevel2, bg='lightsteelblue', width=int(toplevel2.winfo_screenwidth()/4), height=int(toplevel2.winfo_screenheight()))
    toplevel2.configure(background='white')
    admin_frame.place(x=12,y=5)

    #FUNCTION BUTTON
    #VIEW ORDER DETAILS
    def openPDF(view_fileName):
        subprocess.Popen([view_fileName], shell=True)
    def view_order_details_func():
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="Bhavya123")
        mycursor=mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS Database_Mgmt")
        mycursor.execute("USE Database_Mgmt")

        view_l=[]
        view_head=('DL_ID','COMPANY','DL_CONTACT','CITY','STATE','ORDER ID','QTY','PRODUCT ID','NET AMT')
        view_l.append(view_head)
        mycursor.execute("SELECT DEALER.*,ORDER_P.ORDER_ID , ORDER_P.QTY_ORDER,ORDER_P.PRODUCT_ID,BILL.NET_AMOUNT FROM DEALER INNER JOIN ORDER_P  ON ORDER_P.DL_ID=DEALER.DL_ID INNER JOIN BILL ON BILL.DL_ID=DEALER.DL_ID")
        view_records = mycursor.fetchall()
        for x in view_records:
            view_l.append(x)    
        mydb.commit()

        view_data=view_l

        view_filename='Order Details(ADMIN).pdf'
        from reportlab.platypus import SimpleDocTemplate
        from reportlab.lib.pagesizes import letter

        view_pdf=SimpleDocTemplate(view_filename,pagesize=letter)

        from reportlab.platypus import Table

        view_table=Table(view_data)

        from reportlab.platypus import TableStyle
        from reportlab.lib import colors

        style=TableStyle([
            ("BACKGROUND",(0,0),(8,0),colors.yellowgreen),
            ('TEXTCOLOR',(0,0),(2,0),colors.black),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('FONTNAME',(0,0),(-1,0),'Courier-Bold'),
            ('FONTSIZE',(0,0),(-1,0),10),
            ('BOTTOMPADDING',(0,0),(-1,0),12),
            ('BACKGROUND',(0,1),(-1,-1),colors.beige)
        ])

        view_table.setStyle(style)

        #ALTERNATE ROW COLOUR
        rowNumb=len(view_data)
        for i in range(1,rowNumb):
            if i%2==0:
                bc=colors.burlywood
            else:
                bc=colors.beige

            ts=TableStyle(
                [('BACKGROUND',(0,i),(-1,i),bc)])

            view_table.setStyle(ts)   

        #ADDING BORDER
        ts=TableStyle(
            [
                ('BOX',(0,0),(-1,-1),2,colors.blueviolet),
                ('LINEBEFORE',(2,1),(2,-1),2,colors.royalblue),
                ('LINEABOVE',(0,2),(-1,2),2,colors.red),
                ('GRID',(0,1),(-1,-1),2,colors.sienna)
            ]
        ) 

        view_table.setStyle(ts)

        view_elems=[]
        view_elems.append(view_table)

        view_pdf.build(view_elems)

        openPDF(view_filename)


    def a_btn1_func():
        toplevel2=tkinter.Toplevel()
        toplevel2.title("ADD PRODUCT")

        windowWidth = toplevel2.winfo_screenwidth()
        windowHeight=toplevel2.winfo_screenheight()
        toplevel2.resizable(False,False)
        x_pos=int((toplevel2.winfo_screenwidth()/2) - (windowWidth/2))
        y_pos=int((toplevel2.winfo_screenheight()/2) - (windowHeight/2))
        
        toplevel2.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")
        toplevel2.configure(background='lightsteelblue')

        #func exit btn
        def exit_add_pro():
            toplevel2.destroy()

        #func submit btn(ADD PRODUCT-ADMIN)
        def submit_add_product_func():
            nonlocal add_product_name_entry,add_product_id_entry,price_entry
            ADD_PRODUCT_NAME=add_product_name_entry.get()
            ADD_PRODUCT_ID=add_product_id_entry.get()
            PRICE=price_entry.get()

            mycursor.execute(f"insert into PRODUCTS_Main values ('{ADD_PRODUCT_ID}','{ADD_PRODUCT_NAME}','{PRICE}')")
            mydb.commit()

            add_product_name_entry.delete(0,'end')
            add_product_id_entry.delete(0,'end')
            price_entry.delete(0,'end')


        #creating add product form
        Label6=tkinter.Label(toplevel2,text="ADD PRODUCT FORM",font=("Courier New",25,'bold'),fg='navyblue',bg='lightsteelblue')
        Label6.place(x=500,y=25)

        add_product_id_label=tkinter.Label(toplevel2,text="Product ID :",font=("Ubuntu",18),fg='navyblue',bg='lightsteelblue')
        add_product_id_entry=tkinter.Entry(toplevel2,width=18,font=("Ubuntu",17))

        add_product_name_label=tkinter.Label(toplevel2,text="Product Name :",font=("Ubuntu",18),fg='navyblue',bg='lightsteelblue')
        add_product_name_entry=tkinter.Entry(toplevel2,width=18,font=("Ubuntu",17))

        price_label=tkinter.Label(toplevel2,text="Price :",font=("Ubuntu",18),fg='navyblue',bg='lightsteelblue')
        price_entry=tkinter.Entry(toplevel2,width=18,font=("Ubuntu",17))

        rupees_label=tkinter.Label(toplevel2,text="₹",font=("Ubuntu",18),fg='navyblue',bg='lightsteelblue')

        add_product_id_label.place(x=100,y=150)
        add_product_id_entry.place(x=280,y=150)

        add_product_name_label.place(x=100,y=220)
        add_product_name_entry.place(x=280,y=220)

        price_label.place(x=100,y=290)
        price_entry.place(x=280,y=290)

        rupees_label.place(x=263,y=290)

        #button in add product
        submit_pro_btn=tkinter.Button(toplevel2,text='Add Product',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',command=submit_add_product_func)
        submit_pro_btn.place(x=280,y=400)

        exit_add_product_btn=tkinter.Button(toplevel2,text='Exit',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',command=exit_add_pro)
        exit_add_product_btn.place(x=500,y=400)

        toplevel2.mainloop()

    def a_btn2():
        toplevel2=tkinter.Toplevel()
        toplevel2.title("MODIFY RECORD")

        windowWidth = int(toplevel2.winfo_screenwidth()/3)
        windowHeight=int(toplevel2.winfo_screenheight()/3)
        toplevel2.resizable(False,False)
        x_pos=int((toplevel2.winfo_screenwidth()/2) - (windowWidth/2))
        y_pos=int((toplevel2.winfo_screenheight()/2) - (windowHeight/2))
        
        toplevel2.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")
        toplevel2.configure(background='lightsteelblue')

        def exit_edit1():
            toplevel2.destroy()

        def conti():
            editform=tkinter.Toplevel()
            editform.title("EDIT FORM")
            windowWidth = int(editform.winfo_screenwidth())
            windowHeight=int(editform.winfo_screenheight())
            editform.resizable(False,False)
            x_pos=int((editform.winfo_screenwidth()/2) - (windowWidth/2))
            y_pos=int((editform.winfo_screenheight()/2) - (windowHeight/2))
            
            editform.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")
            editform.configure(background='lightsteelblue')

            def exit_editform():
                editform.destroy() 

            def modify_product(): 
                nonlocal edit_pro_id_entry
                EDIT_PRODUCT_NAME=edit_product_name_entry.get()
                EDIT_PRODUCT_ID=edit_pro_id_entry.get()
                EDIT_PRICE=edit_price_entry.get()

                mycursor.execute(f"UPDATE PRODUCTS_Main SET PRODUCT_NAME = '{EDIT_PRODUCT_NAME}' , PRICE = {EDIT_PRICE} where (PRODUCT_ID ='{EDIT_PRODUCT_ID}')")
                mydb.commit()

                edit_product_name_entry.delete(0,'end')
                edit_price_entry.delete(0,'end')
                  
            #edit form
            edit_head_label2=tkinter.Label(editform,text='EDIT PRODUCT FORM',font=("Courier New",25,'bold'),fg='navyblue',bg='lightsteelblue')
            edit_head_label2.place(x=500,y=10)

            edit_product_name_label=tkinter.Label(editform,text="Product Name :",font=("Ubuntu",18),fg='navyblue',bg='lightsteelblue')
            edit_product_name_entry=tkinter.Entry(editform,width=18,font=("Ubuntu",17))

            edit_price_label=tkinter.Label(editform,text="Price :",font=("Ubuntu",18),fg='navyblue',bg='lightsteelblue')
            edit_price_entry=tkinter.Entry(editform,width=18,font=("Ubuntu",17))

            edit_rupees_label=tkinter.Label(editform,text="₹",font=("Ubuntu",18),fg='navyblue',bg='lightsteelblue')

            edit_product_name_label.place(x=100,y=100)
            edit_product_name_entry.place(x=280,y=100)

            edit_price_label.place(x=100,y=170)
            edit_price_entry.place(x=280,y=170)

            edit_rupees_label.place(x=263,y=170)

            #button editform
            edit_save_changes=tkinter.Button(editform,text='Save Changes',relief='flat',font=("Ubuntu",15,'bold'),cursor='hand2',bg='navyblue',fg='white',command=modify_product) #cmd missing
            edit_save_changes.place(x=280,y=300)

            editform_exit=tkinter.Button(editform,text='Exit',relief='flat',font=("Ubuntu",15,'bold'),cursor='hand2',bg='navyblue',fg='white',command=exit_editform) 
            editform_exit.place(x=500,y=300)

            editform.mainloop()

        #creating edit product form
        head_edit_pro_label=tkinter.Label(toplevel2,text="EDIT PRODUCT FORM",font=("Courier New",15,'bold'),fg='navyblue',bg='lightsteelblue')
        head_edit_pro_label.place(x=100,y=10)

        edit_pro_id_label=tkinter.Label(toplevel2,text="Product ID :",font=("Ubuntu",15,'bold'),fg='navyblue',bg='lightsteelblue')
        edit_pro_id_entry=tkinter.Entry(toplevel2,width=10,font=("Ubuntu",17))

        edit_pro_id_label.place(x=60,y=80)
        edit_pro_id_entry.place(x=200,y=80)

        #buttons edit product form
        conti_btn=tkinter.Button(toplevel2,text='Continue',relief='flat',font=("Ubuntu",12,'bold'),cursor='hand2',bg='navyblue',fg='white',command=conti)
        conti_btn.place(x=100,y=180)

        #buttons edit product form
        exit_editpro_btn=tkinter.Button(toplevel2,text='Exit',relief='flat',font=("Ubuntu",12,'bold'),cursor='hand2',bg='navyblue',fg='white',command=exit_edit1)
        exit_editpro_btn.place(x=250,y=180)

        toplevel2.mainloop()

    def del_record_func():
        del_toplevel2=tkinter.Toplevel()
        del_toplevel2.title("DELETE RECORD")

        windowWidth = int(del_toplevel2.winfo_screenwidth()/3)
        windowHeight=int(del_toplevel2.winfo_screenheight()/3)
        del_toplevel2.resizable(False,False)
        x_pos=int((del_toplevel2.winfo_screenwidth()/2) - (windowWidth/2))
        y_pos=int((del_toplevel2.winfo_screenheight()/2) - (windowHeight/2))
        
        del_toplevel2.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")
        del_toplevel2.configure(background='lightsteelblue')

        def delete_product(): 
                nonlocal del_pro_id_entry
                DEL_PRODUCT_ID=del_pro_id_entry.get()
                mycursor.execute(f"DELETE FROM PRODUCTS_Main where (PRODUCT_ID ='{DEL_PRODUCT_ID}')")
                mydb.commit()

                del_pro_id_entry.delete(0,'end')


        #LABELS FOR DELETE RECORD FORM
        head_del_pro_label=tkinter.Label(del_toplevel2,text="DELETE PRODUCT FORM",font=("Courier New",15,'bold'),fg='navyblue',bg='lightsteelblue')
        head_del_pro_label.place(x=100,y=10)

        del_pro_id_label=tkinter.Label(del_toplevel2,text="Product ID :",font=("Ubuntu",15,'bold'),fg='navyblue',bg='lightsteelblue')
        del_pro_id_entry=tkinter.Entry(del_toplevel2,width=10,font=("Ubuntu",17))

        del_pro_id_label.place(x=60,y=80)
        del_pro_id_entry.place(x=200,y=80)

        #buttons edit product form
        del_btn=tkinter.Button(del_toplevel2,text='Delete',relief='flat',font=("Ubuntu",12,'bold'),cursor='hand2',bg='navyblue',fg='white',command=delete_product)
        del_btn.place(x=190,y=180)

        del_toplevel2.mainloop()
    

    #BUTTONS for admin window frame
    #btn for ADDING RECORDS
    a_btn1=tkinter.Button(toplevel2,text='Add Product',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',width=int(20),command=a_btn1_func)
    a_btn1.place(x=30,y=19)

    #btn for MODIFYING RECORDS
    a_btn2=tkinter.Button(toplevel2,text='Modify Record',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',width=int(20),command=a_btn2) 
    a_btn2.place(x=30,y=79)

    #btn to VIEW ORDER DETAILS
    a_btn3=tkinter.Button(toplevel2,text='View Order Details',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',width=int(20),command=view_order_details_func)
    a_btn3.place(x=30,y=199)

    #btn DELETE RECORD
    a_btn4=tkinter.Button(toplevel2,text='Delete Records',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',width=int(20),command=del_record_func)
    a_btn4.place(x=30,y=139)

    toplevel2.mainloop()

#func for product_info
def openPDF(fileName):
    subprocess.Popen([fileName], shell=True)
def _btn4():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Bhavya123")
    mycursor=mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS Database_Mgmt")
    mycursor.execute("USE Database_Mgmt")

    l=[]
    head=('PRODUCT ID','PRODUCT NAME','PRICE')
    l.append(head)
    mycursor.execute("select * from PRODUCTS_Main")
    records = mycursor.fetchall()
    for x in records:
        l.append(x)    
    mydb.commit()

    data=l

    filename='Product_Details_Table.pdf'
    from reportlab.platypus import SimpleDocTemplate
    from reportlab.lib.pagesizes import letter

    pdf=SimpleDocTemplate(filename,pagesize=letter)

    from reportlab.platypus import Table

    table=Table(data)

    from reportlab.platypus import TableStyle
    from reportlab.lib import colors

    style=TableStyle([
        ("BACKGROUND",(0,0),(2,0),colors.yellowgreen),
        ('TEXTCOLOR',(0,0),(2,0),colors.red),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME',(0,0),(-1,0),'Courier-Bold'),
        ('FONTSIZE',(0,0),(-1,0),14),
        ('BOTTOMPADDING',(0,0),(-1,0),12),
        ('BACKGROUND',(0,1),(-1,-1),colors.beige)
    ])

    table.setStyle(style)

    '''#ALTERNATE ROW COLOUR
    rowNumb=len(data)
    for i in range(1,rowNumb):
        if i%2==0:
            bc=colors.burlywood
        else:
            bc=colors.beige

        ts=TableStyle(
            [('BACKGROUND',(0,i),(-1,i),bc)])

        table.setStyle(ts)   

    #ADDING BORDER
    ts=TableStyle(
        [
            ('BOX',(0,0),(-1,-1),2,colors.blueviolet),
            ('LINEBEFORE',(2,1),(2,-1),2,colors.royalblue),
            ('LINEABOVE',(0,2),(-1,2),2,colors.red),
            ('GRID',(0,1),(-1,-1),2,colors.sienna)
        ]
    ) 

    table.setStyle(ts)'''

    elems=[]
    elems.append(table)

    pdf.build(elems)

    openPDF(filename)
  
#func for dealer
def _btn5():
    dealer=tkinter.Toplevel()
    dealer.title("DEALER")

    windowWidth = dealer.winfo_screenwidth()
    windowHeight=dealer.winfo_screenheight()
    dealer.resizable(False,False)
    x_pos=int((dealer.winfo_screenwidth()/2) - (windowWidth/2))
    y_pos=int((dealer.winfo_screenheight()/2) - (windowHeight/2))
    
    dealer.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")

    dealer.configure(background='lightsteelblue')

    
    #func for BILL BUTTON
    def bill_btn_func():
        bill_toplevel2=tkinter.Toplevel()
        bill_toplevel2.title("BILL")

        windowWidth = int(bill_toplevel2.winfo_screenwidth()/3)
        windowHeight=int(bill_toplevel2.winfo_screenheight()/3)
        bill_toplevel2.resizable(False,False)
        x_pos=int((bill_toplevel2.winfo_screenwidth()/2) - (windowWidth/2))
        y_pos=int((bill_toplevel2.winfo_screenheight()/2) - (windowHeight/2))
        
        bill_toplevel2.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")
        bill_toplevel2.configure(background='lightsteelblue')

        #lables bill window
        head_bill_pro_label=tkinter.Label(bill_toplevel2,text="ENTER YOUR DEALER ID",font=("Courier New",15,'bold'),fg='navyblue',bg='lightsteelblue')
        head_bill_pro_label.place(x=100,y=10)

        bill_dealer_id_label=tkinter.Label(bill_toplevel2,text="Dealer ID :",font=("Ubuntu",15,'bold'),fg='navyblue',bg='lightsteelblue')
        bill_dealer_id_entry=tkinter.Entry(bill_toplevel2,width=10,font=("Ubuntu",17))

        bill_dealer_id_label.place(x=60,y=80)
        bill_dealer_id_entry.place(x=200,y=80)

        #BILL
        def openPDF(bill_fileName):
            subprocess.Popen([bill_fileName], shell=True)
        def view_bill():
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="Bhavya123")
            
            mycursor=mydb.cursor()

            mycursor.execute("CREATE DATABASE IF NOT EXISTS Database_Mgmt")
            mycursor.execute("USE Database_Mgmt")
            bill_place()

            nonlocal bill_dealer_id_entry
            BILL_DEALER_ID=bill_dealer_id_entry.get()

            bill_l=[]
            bill_head=('BILL ID','DEALER NAME','TAX PERCENT(GST)','NET AMOUNT')
            bill_l.append(bill_head)
            mycursor.execute(f"SELECT * FROM BILL where (DL_ID ='{BILL_DEALER_ID}')")
            bill_records = mycursor.fetchall()
            mydb.commit()
            for x in bill_records:
                bill_l.append(x)    

            bill_data=bill_l

            bill_filename='Bill.pdf'
            from reportlab.platypus import SimpleDocTemplate
            from reportlab.lib.pagesizes import letter

            pdf=SimpleDocTemplate(bill_filename,pagesize=letter)

            from reportlab.platypus import Table

            table=Table(bill_data)

            from reportlab.platypus import TableStyle
            from reportlab.lib import colors

            style=TableStyle([
                ("BACKGROUND",(0,0),(3,0),colors.yellowgreen),
                ('TEXTCOLOR',(0,0),(2,0),colors.black),
                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                ('FONTNAME',(0,0),(-1,0),'Courier-Bold'),
                ('FONTSIZE',(0,0),(-1,0),14),
                ('BOTTOMPADDING',(0,0),(-1,0),12),
                ('BACKGROUND',(0,1),(-1,-1),colors.beige)
            ])

            table.setStyle(style)

            #ALTERNATE ROW COLOUR
            rowNumb=len(bill_data)
            for i in range(1,rowNumb):
                if i%2==0:
                    bc=colors.burlywood
                else:
                    bc=colors.beige

                ts=TableStyle(
                    [('BACKGROUND',(0,i),(-1,i),bc)])

                table.setStyle(ts)   

            #ADDING BORDER
            ts=TableStyle(
                [
                    ('BOX',(0,0),(-1,-1),2,colors.blueviolet),
                    ('LINEBEFORE',(2,1),(2,-1),2,colors.royalblue),
                    ('LINEABOVE',(0,2),(-1,2),2,colors.red),
                    ('GRID',(0,1),(-1,-1),2,colors.sienna)
                ]
            ) 

            table.setStyle(ts)

            bill_elems=[]
            bill_elems.append(table)

            pdf.build(bill_elems)

            openPDF(bill_filename)


        #BTN BILL WINDOW
        bill_btn=tkinter.Button(bill_toplevel2,text='View Bill',relief='flat',font=("Ubuntu",12,'bold'),cursor='hand2',bg='navyblue',fg='white',command=view_bill)
        bill_btn.place(x=190,y=180)    

        bill_toplevel2.mainloop()


    #func for d_btn2
    def discount():
        discount=tkinter.Toplevel()
        discount.title("DISCOUNTS")

        windowWidth = discount.winfo_screenwidth()
        windowHeight=discount.winfo_screenheight()
        discount.resizable(False,False)
        x_pos=int((discount.winfo_screenwidth()/2) - (windowWidth/2))
        y_pos=int((discount.winfo_screenheight()/2) - (windowHeight/2))
        
        discount.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")

        discount.configure(background='lightsteelblue')

        #adding text to discount table
        dis_Label=tkinter.Label(discount,text="DISCOUNTS AVAILABLE",font=("Courier New",25,'bold','underline'),bg='lightsteelblue',fg='navyblue')
        dis_Label.place(x=450,y=10)

        discount_table='''               AMOUNT RANGE(₹)      |       DISCOUNT(%)
                     ---------------------------------------------------
                50-100               |               2
                100-200             |               5
                 200-500             |              20
                500 and More     |              25'''

        dis_table_Label=tkinter.Label(discount,text=discount_table,font=("Ubuntu",22,'bold'),bg='lightsteelblue',fg='darkslategray')
        dis_table_Label.place(x=210,y=135)      

        discount.mainloop()

    #func for Place order button
    def d_place_order():
        place_order=tkinter.Toplevel()
        place_order.title("PLACE ORDER")

        windowWidth = place_order.winfo_screenwidth()
        windowHeight=place_order.winfo_screenheight()
        place_order.resizable(False,False)
        x_pos=int((place_order.winfo_screenwidth()/2) - (windowWidth/2))
        y_pos=int((place_order.winfo_screenheight()/2) - (windowHeight/2))
            
        place_order.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")

        place_order.configure(background='lightsteelblue')

        #insert delear_info into DEALER TABLE func
        def insert_dealer_info():
            #nonlocal dealer_id_, company_name_entry, contact_entry, city_entry, state_entry
            dealer_id = dealer_id_.get()
            DL_CMPNY_NAME=company_name_entry.get()
            DL_CONTACT=contact_entry.get()
            DL_CITY=city_entry.get()
            DL_STATE=state_entry.get()

            mycursor.execute(f"insert into DEALER(DL_ID,DL_CMPNY_NAME,DL_CONTACT,DL_CITY,DL_STATE) values ('{dealer_id}','{DL_CMPNY_NAME}','{DL_CONTACT}','{DL_CITY}','{DL_STATE}')")
            mydb.commit()

            # place_order.destroy()
            # d_place_order()
            #dealer_id_.delete(0, 'end')

        def order_dealer_info():
            nonlocal order_id_entry,dealer_id_entry_order,product_id_entry,Qty_entry
            ORDER_ID=order_id_entry.get()
            DL_ID=dealer_id_entry_order.get()
            PRODUCT_ID=product_id_entry.get()
            QTY_ORDER=Qty_entry.get()

            mycursor.execute(f"insert into ORDER_P values ('{ORDER_ID}','{DL_ID}','{PRODUCT_ID}',{QTY_ORDER})")
            mydb.commit()

            product_id_entry.delete(0,'end')
            Qty_entry.delete(0,'end')

        #form for placing order
        #dealer details
        head_place_order=tkinter.Label(place_order,text='PLACING ORDER FORM',font=("Courier New",25,'bold','underline'),bg='lightsteelblue',fg='navyblue')
        head_place_order.place(x=450,y=10)

        head_dealer_info=tkinter.Label(place_order,text="*DEALER'S INFORMATION",font=("Courier New",25,'bold','underline'),bg='lightsteelblue',fg='navyblue')
        head_dealer_info.place(x=10,y=90)

        dealer_id_label=tkinter.Label(place_order,text="DEALER ID :",font=("Courier New",17),bg='lightsteelblue',fg='navyblue')
        dealer_id_=tkinter.Entry(place_order,width=13,font=("Ubuntu",16))

        dealer_id_label.place(x=100,y=160)
        dealer_id_.place(x=270,y=160)

        company_name_label=tkinter.Label(place_order,text="COMPANY NAME :",font=("Courier New",17),bg='lightsteelblue',fg='navyblue')
        company_name_entry=tkinter.Entry(place_order,width=15,font=("Ubuntu",16))

        company_name_label.place(x=500,y=160)
        company_name_entry.place(x=700,y=160)

        city_label=tkinter.Label(place_order,text="CITY :",font=("Courier New",17),bg='lightsteelblue',fg='navyblue')
        city_entry=tkinter.Entry(place_order,width=13,font=("Ubuntu",16))

        city_label.place(x=100,y=220)
        city_entry.place(x=270,y=220)

        state_label=tkinter.Label(place_order,text="STATE :",font=("Courier New",17),bg='lightsteelblue',fg='navyblue')
        state_entry=tkinter.Entry(place_order,width=15,font=("Ubuntu",16))

        state_label.place(x=500,y=220)
        state_entry.place(x=700,y=220)

        contact_label=tkinter.Label(place_order,text="CONTACT NO. :",font=("Courier New",17),bg='lightsteelblue',fg='navyblue')
        contact_entry=tkinter.Entry(place_order,width=13,font=("Ubuntu",16))

        contact_label.place(x=100,y=280)
        contact_entry.place(x=270,y=280)

        submit_dealer_info_btn=tkinter.Button(place_order,text='Submit',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',command=insert_dealer_info)
        submit_dealer_info_btn.place(x=910,y=290)

        #order details
        head_order_info=tkinter.Label(place_order,text="*ORDER DETAILS",font=("Courier New",25,'bold','underline'),bg='lightsteelblue',fg='navyblue')
        head_order_info.place(x=10,y=340)

        order_id_label=tkinter.Label(place_order,text="ORDER ID :",font=("Courier New",17),bg='lightsteelblue',fg='navyblue')
        order_id_entry=tkinter.Entry(place_order,width=13,font=("Ubuntu",16))

        order_id_label.place(x=100,y=400)
        order_id_entry.place(x=270,y=400)

        dealer_id_label=tkinter.Label(place_order,text="DEALER ID :",font=("Courier New",17),bg='lightsteelblue',fg='navyblue')
        dealer_id_entry_order=tkinter.Entry(place_order,width=13,font=("Ubuntu",16))

        dealer_id_label.place(x=500,y=400)
        dealer_id_entry_order.place(x=700,y=400)

        product_id_label=tkinter.Label(place_order,text="PRODUCT ID :",font=("Courier New",17),bg='lightsteelblue',fg='navyblue')
        product_id_entry=tkinter.Entry(place_order,width=13,font=("Ubuntu",16))

        product_id_label.place(x=100,y=460)
        product_id_entry.place(x=270,y=460)

        Qty_label=tkinter.Label(place_order,text="QUANTITY :",font=("Courier New",17),bg='lightsteelblue',fg='navyblue')
        Qty_entry=tkinter.Entry(place_order,width=13,font=("Ubuntu",16))

        Qty_label.place(x=500,y=460)
        Qty_entry.place(x=700,y=460)

        submit_order_details_btn=tkinter.Button(place_order,text='Submit',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',command= order_dealer_info)#cmd missing
        submit_order_details_btn.place(x=910,y=510)


        place_order.mainloop()

    #Dealer window
    #buttons dealer window

    #btn for view bill
    d_btn1=tkinter.Button(dealer,text='Bill',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',width=int(25),command=bill_btn_func)
    d_btn1.place(x=30,y=139)

    #btn for Dicounts
    d_btn2=tkinter.Button(dealer,text='Discount/Schemes Available',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',width=int(25),command=discount) 
    d_btn2.place(x=30,y=19)

    #btn to PLACE ORDER
    d_btn3=tkinter.Button(dealer,text='Place Order',relief='flat',font=("Ubuntu",16,'bold'),cursor='hand2',bg='navyblue',fg='white',width=int(25),command=d_place_order)
    d_btn3.place(x=30,y=79)

    dealer.mainloop()


#BUTTONS of parent window
#button about_us
btn1=tkinter.Button(p_frame1,text='About Us',relief='flat',font=("Ubuntu",15,'bold'),cursor='hand2',command=_btn1,bg='navyblue',fg='white')
btn1.place(x=1155,y=19)

#button to exit
btn2=tkinter.Button(p_frame3,text='EXIT',relief='flat',font=("Ubuntu",17,'bold'),cursor='hand2',command=_btn2,bg='navyblue',fg='white')
btn2.place(x=1167,y=260)

#button admin
btn3=tkinter.Button(p_frame3,text='ADMIN',relief='flat',font=("Ubuntu",17,'bold'),cursor='hand2',command=_btn3,bg='navyblue',fg='white')
btn3.place(x=10,y=20)

#button product_info
btn4=tkinter.Button(p_frame3,text='PRODUCT DETAILS',relief='flat',font=("Ubuntu",17,'bold'),cursor='hand2',command=_btn4,bg='navyblue',fg='white')
btn4.place(x=10,y=90)

#button dealer
btn4=tkinter.Button(p_frame3,text='DEALER',relief='flat',font=("Ubuntu",17,'bold'),cursor='hand2',command=_btn5,bg='navyblue',fg='white')
btn4.place(x=10,y=160)

root.mainloop()
