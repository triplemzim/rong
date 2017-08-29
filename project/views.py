from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth
from .models import Item, Sr, Customer, Supplier, Memo, SaleItem, PurchaseItem , PurchaseMemo

from django.contrib.auth import logout
from datetime import datetime



# Create your views here.

# for logout
def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/login')



def show_login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')

    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_method(request):
    username = request.POST.get('username', '')

    password = request.POST.get('password', '')
    value = request.POST.get('Select1')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        print(value + 'hi')

        if value == 'Administrator':
            return HttpResponseRedirect("/admin")
        elif value == 'User':
            return HttpResponseRedirect("/home")



    else:
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)


def show_home_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')


    c = {}
    c.update(csrf(request))
    return render_to_response('home.html', c)


def show_item_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')


    c = {}
    c.update(csrf(request))
    return render_to_response('item.html', c)


def show_item_add_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')


    c = {}
    c.update(csrf(request))
    return render_to_response('item_add.html', c)

def item_add_search(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    type = request.POST.get('stype','')
    value = request.POST.get('value','')

    print(type)

    if value=='':
        obj = Item.objects.all
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_add.html', c)


    if type=='ID':

        obj = Item.objects.filter(id=int(value))
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_add.html', c)


    if type == 'Name':
        obj = Item.objects.filter(name__icontains=value)
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_add.html', c)

    if type == 'Size':
        obj = Item.objects.filter(size__icontains=value)
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_add.html', c)




def show_item_delete_page(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    item = Item.objects.filter(id=0)
    c = {'Item': item}
    c.update(csrf(request))
    return render_to_response('item_delete.html', c)


def item_delete_search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    type = request.POST.get('stype','')
    value = request.POST.get('value','')

    print(type)



    if value=="":
        obj = Item.objects.all()
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_delete.html', c)

    if type=='ID':
        obj = Item.objects.filter(id=int(value))
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_delete.html', c)


    if type == 'Name':
        obj = Item.objects.filter(name=value)
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_delete.html', c)

    if type == 'Size':
        obj = Item.objects.filter(size=value)
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_delete.html', c)

    if type == 'Show All':
        obj = Item.objects.all()
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_delete.html', c)



def item_edit_search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')


    type = request.POST.get('stype','')
    value = request.POST.get('value','')



    print(type)


    if value=="":
        obj = Item.objects.all()
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_edit.html', c)

    if type=='ID':
        obj = Item.objects.filter(id=int(value))
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_edit.html', c)


    if type == 'Name':
        obj = Item.objects.filter(name=value)
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_edit.html', c)

    if type == 'Size':
        obj = Item.objects.filter(size=value)
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_edit.html', c)

    if type == 'Show All':
        obj = Item.objects.all()
        if obj is not None:
            c = {'Item': obj}
            c.update(csrf(request))
            return render_to_response('item_edit.html', c)




def show_item_edit_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')


    c = {'Item':Item.objects.all()}
    c.update(csrf(request))
    return render_to_response('item_edit.html', c)


def item_edit_load_data(request,item_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    print(item_id)
    obj = Item.objects.filter( id = int(item_id)).get()
    print(obj.id)
    c={'obj':obj}

    c.update(csrf(request))
    return render_to_response('item_edit.html', c)

def item_edit_save(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    id = request.POST.get('ID','')
    obj = Item.objects.filter(id=int(id)).get()
    obj.name= request.POST.get('NAME','')
    obj.size= request.POST.get('SIZE','')
    obj.stock_rate= float(request.POST.get('STOCK_RATE',''))
    obj.sale_rate= float(request.POST.get('SALE_RATE',''))
    obj.save()
    c = {'Item': Item.objects.all()}
    c.update(csrf(request))
    return render_to_response('item_edit.html', c)


def add_item_database(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    name= request.POST.get('name','')
    size= request.POST.get('size','')
    stock_rate= request.POST.get('stock_rate','')
    sale_rate= request.POST.get('sale_rate','')

    obj= Item(name=name, size= size, stock_rate=float(stock_rate),sale_rate=float(sale_rate))

    obj.save();

    return  HttpResponseRedirect("/item/add/")

    #have to handle some error here


def delete_item_database(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    id = request.POST.get('slctId','')
    if id=='':
        print('invalid')
    else:
        Item.objects.filter(id=id).delete()
        print(id)
        return HttpResponseRedirect('/item/delete/')




#supplier and custonmer



def show_sc_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    c = {}
    c.update(csrf(request))
    return render_to_response('sc.html', c)


def show_sc_add_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    c = {'sr':Sr.objects.all()}
    c.update(csrf(request))
    return render_to_response('sc_add.html', c)


def show_sc_delete_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    c = {'supplier':Supplier.objects.all, 'customer': Customer.objects.all()}
    c.update(csrf(request))
    return render_to_response('sc_delete.html', c)
def show_sc_edit_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    c = {'supplier':Supplier.objects.all(), 'customer':Customer.objects.all(),'sr':Sr.objects.all()}
    c.update(csrf(request))
    return render_to_response('sc_edit.html', c)





def add_sc_database(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    s = request.POST.get('sr','')
    a,b=s.split(':')
    print(int(a))

    name = request.POST.get('name','')
    address = request.POST.get('address','')
    mobile_no = request.POST.get('mobile_no','')
    sr = Sr.objects.get(id=int(a))
    type = request.POST.get('type','')

    if type=='Customer':
        obj = Customer(name=name, address=address,mobile_no=mobile_no, sr=sr)
        obj.save()

    if type=='Supplier':
        obj = Supplier(name=name, address=address,mobile_no=mobile_no, sr=sr)
        obj.save()



    c = {'sr':Sr.objects.all()}
    c.update(csrf(request))
    return render_to_response('sc_add.html', c)


def sc_add_search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')


    type = request.POST.get('stype','')
    value = request.POST.get('value','')

    print(type)


    if value=='':
        obj1 = Supplier.objects.all()
        obj2 = Customer.objects.all()
        if obj1 is not None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2, 'sr': Sr.objects.all()}
            c.update(csrf(request))
            return render_to_response('sc_add.html', c)

    if type == 'Name':
        obj1 = Supplier.objects.filter(name=value)
        obj2 = Customer.objects.filter(name=value)
        if obj1 is not  None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2, 'sr':Sr.objects.all()}
            c.update(csrf(request))
            return render_to_response('sc_add.html', c)

    if type == 'Mobile No':
        obj1 = Supplier.objects.filter(mobile_no=value)
        obj2 = Customer.objects.filter(mobile_no=value)
        if obj1 is not  None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2, 'sr':Sr.objects.all()}
            c.update(csrf(request))
            return render_to_response('sc_add.html', c)

    if type == 'Show All':
        obj1 = Supplier.objects.all()
        obj2 = Customer.objects.all()
        if obj1 is not  None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2, 'sr':Sr.objects.all()}
            c.update(csrf(request))
            return render_to_response('sc_add.html', c)

    c = {}
    c.update(csrf(request))
    return render_to_response('sc_add.html', c)


def sc_delete_search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    type = request.POST.get('stype','')
    value = request.POST.get('value','')

    print(type)




    if type == 'Name':
        obj1 = Supplier.objects.filter(name=value)
        obj2 = Customer.objects.filter(name=value)
        if obj1 is not  None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2}
            c.update(csrf(request))
            return render_to_response('sc_delete.html', c)

    if type == 'Mobile No':
        obj1 = Supplier.objects.filter(mobile_no=value)
        obj2 = Customer.objects.filter(mobile_no=value)
        if obj1 is not  None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2}
            c.update(csrf(request))
            return render_to_response('sc_delete.html', c)

    if type == 'Show All':
        obj1 = Supplier.objects.all()
        obj2 = Customer.objects.all()
        if obj1 is not  None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2}
            c.update(csrf(request))
            return render_to_response('sc_delete.html', c)


def sc_delete_database(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    strng = request.POST.get('id', '')
    a,b= strng.split('_')

    if a=='S':
        Supplier.objects.filter(id=int(b)).delete()
    if a=='C':
        Customer.objects.filter(id = int(b)).delete()




    c = {'supplier': Supplier.objects.all, 'customer': Customer.objects.all()}
    c.update(csrf(request))
    return render_to_response('sc_delete.html', c)


def sc_edit_search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    type = request.POST.get('stype','')
    value = request.POST.get('value','')

    print(type)




    if type == 'Name':
        obj1 = Supplier.objects.filter(name=value)
        obj2 = Customer.objects.filter(name=value)
        if obj1 is not  None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2}
            c.update(csrf(request))
            return render_to_response('sc_edit.html', c)

    if type == 'Mobile No':
        obj1 = Supplier.objects.filter(mobile_no=value)
        obj2 = Customer.objects.filter(mobile_no=value)
        if obj1 is not  None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2}
            c.update(csrf(request))
            return render_to_response('sc_edit.html', c)

    if type == 'Show All':
        obj1 = Supplier.objects.all()
        obj2 = Customer.objects.all()
        if obj1 is not  None and obj2 is not None:
            c = {'supplier': obj1, 'customer': obj2}
            c.update(csrf(request))
            return render_to_response('sc_edit.html', c)




def sc_edit_load_supplier(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    obj = Supplier.objects.filter(id=int(id)).get()
    type='S_'

    c = {'supplier': Supplier.objects.all(), 'customer': Customer.objects.all(), 'sr': Sr.objects.all(), 'type':type,'obj':obj, 'DEFAULT':'Supplier',}
    c.update(csrf(request))
    return render_to_response('sc_edit.html', c)

def sc_edit_load_customer(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    obj = Customer.objects.filter(id=int(id)).get()
    type='C_'

    c = {'supplier': Supplier.objects.all(), 'customer': Customer.objects.all(), 'sr': Sr.objects.all(), 'type':type,'obj':obj,'DEFAULT':'Customer',}
    c.update(csrf(request))
    return render_to_response('sc_edit.html', c)





def sc_edit_done(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')



    t,id =request.POST.get('id','').split('_')

    if t=='C':
        obj = Customer.objects.filter(id= int(id)).get()



        obj.name= request.POST.get('name','')
        obj.address = request.POST.get('address','')
        obj.mobile_no = request.POST.get('mobile_no','')
        a,b= request.POST.get('sr','').split(':')
        obj.sr= Sr.objects.filter(id=int(a)).get()

        type= request.POST.get('type','')
        if type== 'Customer' :
            obj.save()
        else:
            Supplier.objects.create(name=obj.name, address=obj.address, mobile_no=obj.mobile_no, sr=obj.sr)
            Customer.objects.filter(id=obj.id).delete()

    if t == 'S':
        obj = Supplier.objects.filter(id=int(id)).get()

        obj.name = request.POST.get('name', '')
        obj.address = request.POST.get('address', '')
        obj.mobile_no = request.POST.get('mobile_no', '')
        a, b = request.POST.get('sr', '').split(':')
        obj.sr = Sr.objects.filter(id=int(a)).get()
        type = request.POST.get('type', '')

        if type== 'Supplier' :

            obj.save()
        else:
            Customer.objects.create(name=obj.name, address=obj.address, mobile_no=obj.mobile_no, sr=obj.sr)
            Supplier.objects.filter(id=obj.id).delete()



    c = {'supplier': Supplier.objects.all(), 'customer': Customer.objects.all(), 'sr': Sr.objects.all()}
    c.update(csrf(request))
    return render_to_response('sc_edit.html', c)





#sale

def sale_page_load(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    c = {}
    c.update(csrf(request))
    return render_to_response('sale.html', c)




def sale_add_page_load(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    c = {'party':Customer.objects.all(),}
    c.update(csrf(request))
    return render_to_response('sale_add.html', c)



def sale_add_page_load_1(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    obj = Customer.objects.filter(id=int(id)).get()
    c = {'CUSTOMER':obj,}
    c.update(csrf(request))
    return render_to_response('sale_add.html', c)



def sale_add_process(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    id = request.POST.get('Memo_no','')

    if id=='' and not request.POST.get('New') :
        c_id , c_name = request.POST.get('Select_party','').split('-')
        customer= Customer.objects.filter(id=int(c_id)).get()
        date ='2010-12-12'
        obj= Memo(party= customer, date=date )
        obj.save()

        item = Item.objects.all

        c = {'SALE_OBJ': obj, 'ALLITEM':item,  }
        c.update(csrf(request))
        return render_to_response('sale_add.html', c)



    elif request.POST.get('Add'):
        objMemo = Memo.objects.filter(id=int(id)).get()

        item_id,item_name, item_size = request.POST.get('Select_item', '').split('-')
        selected_item = Item.objects.filter(id=int(item_id)).get()

        quantity = request.POST.get('Unit','')
        free = request.POST.get('Free','')



        objSaleItem = SaleItem(quantity=quantity,free=free,item=selected_item)
        objSaleItem.save()
        objMemo.sale_item.filter(item =objSaleItem.item ).delete()
        objMemo.sale_item.add(objSaleItem)

        objMemo.save()
        total = objMemo.get_total()


        item = Item.objects.all
        c = {'SALE_OBJ': objMemo, 'ALLITEM': item, 'TOTAL':total}
        c.update(csrf(request))
        return render_to_response('sale_add.html', c)


    elif request.POST.get('Done'):
        objMemo = Memo.objects.filter(id=int(id)).get()
        objMemo.paid = request.POST.get('Paid')
        objMemo.discount = request.POST.get('Discount')
        objMemo.save()


        return HttpResponseRedirect("/sale/sale_add/")

    elif request.POST.get('New'):
        return HttpResponseRedirect("/sale/sale_add/")



    else :

        objMemo = Memo.objects.filter(id=int(id)).get()
        item_name, item_size = request.POST.get('Select_item', '').split('-')
        item = Item.objects.filter(name=item_name, size=item_size).get()

        total = objMemo.get_total()


        c = {'SALE_OBJ': objMemo,'CURRENT_ITEM':item, 'TOTAL':total }
        c.update(csrf(request))
        return render_to_response('sale_add.html', c)

def sale_edit_delete(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    if request.POST.get('Delete'):
        id= request.POST.get('Select_memo','')
        memo_obj= Memo.objects.get(id= int(id))
        all_sale_obj = Memo.objects.all

        gt =memo_obj.get_total()-memo_obj.discount
        due = gt - memo_obj.paid

        c = {'SALE_OBJ': memo_obj,'ALL_SALE_OBJ':all_sale_obj, 'DELETE':'true', 'TOTAL':memo_obj.get_total(), 'GT':gt, 'DUE': due}
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)


    elif request.POST.get('Delete_confirm'):
        id= request.POST.get('Memo_no','')
        Memo.objects.filter(id= int(id)).delete()

        all_sale_obj= Memo.objects.all
        c = {'ALL_SALE_OBJ': all_sale_obj}
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)

    elif request.POST.get('Print'):
        id= request.POST.get('Select_memo','')
        memo_obj= Memo.objects.get(id= int(id))
        all_sale_obj = Memo.objects.all

        gt =memo_obj.get_total()-memo_obj.discount
        due = gt - memo_obj.paid

        c = {'SALE_OBJ': memo_obj,'ALL_SALE_OBJ':all_sale_obj, 'PRINT':'true', 'TOTAL':memo_obj.get_total(), 'GT':gt, 'DUE': due}
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)
    elif request.POST.get('Print_confirm'):
        return  HttpResponseRedirect("/sale/sale_edit_delete/")

    elif request.POST.get('Edit'):
        id= request.POST.get('Select_memo','')
        memo_obj= Memo.objects.get(id= int(id))
        all_sale_obj = Memo.objects.all

        gt =memo_obj.get_total()-memo_obj.discount
        due = gt - memo_obj.paid

        customer= Customer.objects.all()
        item = Item.objects.all()
        c = {'ITEM':item ,'SALE_OBJ': memo_obj,'ALL_SALE_OBJ':all_sale_obj, 'CUSTOMER':customer, 'EDIT':'true', 'TOTAL':memo_obj.get_total(), 'GT':gt, 'DUE': due}
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)

    elif request.POST.get('Save_head'):

        id = request.POST.get('Memo_no', '')
        memo_obj = Memo.objects.get(id=int(id))

        customer_id, customer_name, customer_mobile_no = request.POST.get('Party', '').split('-')

        memo_obj.party= Customer.objects.get(id = int(customer_id))
        memo_obj.save()


        all_sale_obj = Memo.objects.all

        gt = memo_obj.get_total() - memo_obj.discount
        due = gt - memo_obj.paid

        customer = Customer.objects.all()
        item = Item.objects.all()
        c = {'ITEM': item, 'SALE_OBJ': memo_obj, 'ALL_SALE_OBJ': all_sale_obj, 'CUSTOMER': customer, 'EDIT': 'true',
             'TOTAL': memo_obj.get_total(), 'GT': gt, 'DUE': due}
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)


    elif request.POST.get('Delete_item'):
        id = request.POST.get('Memo_no', '')
        objMemo = Memo.objects.filter(id=int(id)).get()

        item_id, item_name, item_size = request.POST.get('Select_item', '').split('-')
        selected_item = Item.objects.filter(id=int(item_id)).get()

        quantity = request.POST.get('Unit', '')
        free = request.POST.get('Free', '')

        objSaleItem = SaleItem(quantity=quantity, free=free, item=selected_item)
        
        objMemo.sale_item.filter(item=objSaleItem.item).delete()


        objMemo.save()

        customer = Customer.objects.all()
        item = Item.objects.all()
        all_sale_obj = Memo.objects.all
        gt = objMemo.get_total() - objMemo.discount
        due = gt - objMemo.paid

        c = {
             'NEW': 'true',
             'ITEM': item,
             'SALE_OBJ': objMemo,
             'ALL_SALE_OBJ': all_sale_obj,
             'CUSTOMER': customer,
             'EDIT': 'true',
             'TOTAL': objMemo.get_total(),
             'GT': gt,
             'DUE': due
             }
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)

    elif request.POST.get('Save_item'):
        id = request.POST.get('Memo_no', '')
        objMemo = Memo.objects.filter(id=int(id)).get()

        item_id, item_name, item_size = request.POST.get('Select_item', '').split('-')
        selected_item = Item.objects.filter(id=int(item_id)).get()

        quantity = request.POST.get('Unit', '')
        free = request.POST.get('Free', '')

        objSaleItem = SaleItem(quantity=int(quantity), free=int(free), item=selected_item)
        objSaleItem.save()

        objMemo.sale_item.filter(item=objSaleItem.item).delete()
        objMemo.sale_item.add(objSaleItem)


        objMemo.save()

        customer = Customer.objects.all()
        item = Item.objects.all()
        all_sale_obj = Memo.objects.all
        gt = objMemo.get_total() - objMemo.discount
        due = gt - objMemo.paid

        c = {
            'NEW': 'true',
            'ITEM': item,
            'SALE_OBJ': objMemo,
            'ALL_SALE_OBJ': all_sale_obj,
            'CUSTOMER': customer,
            'EDIT': 'true',
            'TOTAL': objMemo.get_total(),
            'GT': gt,
            'DUE': due
        }
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)

    elif request.POST.get('Save_all'):
        id = request.POST.get('Memo_no', '')

        objMemo = Memo.objects.filter(id=int(id)).get()

        discount =  request.POST.get('Discount','')
        paid = request.POST.get('Paid','')


        objMemo.discount = discount
        objMemo.paid = paid

        objMemo.save()


        all_sale_obj = Memo.objects.all

        c = {'ALL_SALE_OBJ': all_sale_obj}
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)





    else:
        if request.POST.get('Select_item'):
            item_id, item_name, item_size = request.POST.get('Select_item', '').split('-')

            id = request.POST.get('Memo_no', '')

            objMemo = Memo.objects.filter(id=int(id)).get()

            item_id, item_name, item_size = request.POST.get('Select_item', '').split('-')

            if item_id == '':
                all_sale_obj = Memo.objects.all
                c = {'ALL_SALE_OBJ': all_sale_obj}
                c.update(csrf(request))
                return render_to_response('sale_edit_delete.html', c)
            else:
                s_item= Item.objects.get(id = int(item_id))
                selected_sale_item = objMemo.sale_item.filter(item=s_item)
                if selected_sale_item :
                    print('yes')
                    selected_sale_item = objMemo.sale_item.filter(item=s_item).get()
                    current_item = s_item

                    id = request.POST.get('Memo_no', '')
                    memo_obj = Memo.objects.get(id=int(id))
                    all_sale_obj = Memo.objects.all

                    gt = memo_obj.get_total() - memo_obj.discount
                    due = gt - memo_obj.paid

                    customer = Customer.objects.all()
                    item = Item.objects.all()


                    c = {'CURRENT_ITEM':s_item, 'OLD':'true', 'SALE_ITEM':selected_sale_item, 'ITEM': item, 'SALE_OBJ': memo_obj, 'ALL_SALE_OBJ': all_sale_obj, 'CUSTOMER': customer,
                         'EDIT': 'true', 'TOTAL': memo_obj.get_total(), 'GT': gt, 'DUE': due}
                    c.update(csrf(request))
                    return render_to_response('sale_edit_delete.html', c)




                else:
                    print('no')

                    current_item = s_item

                    id = request.POST.get('Memo_no', '')
                    memo_obj = Memo.objects.get(id=int(id))
                    all_sale_obj = Memo.objects.all

                    gt = memo_obj.get_total() - memo_obj.discount
                    due = gt - memo_obj.paid

                    customer = Customer.objects.all()
                    item = Item.objects.all()

                    c = {'CURRENT_ITEM': s_item ,
                         'NEW':'true',
                         'ITEM': item,
                         'SALE_OBJ': memo_obj,
                         'ALL_SALE_OBJ': all_sale_obj,
                         'CUSTOMER': customer,
                         'EDIT': 'true',
                         'TOTAL': memo_obj.get_total(),
                         'GT': gt,
                         'DUE': due
                         }
                    c.update(csrf(request))
                    return render_to_response('sale_edit_delete.html', c)







        all_sale_obj = Memo.objects.all
        c = {'ALL_SALE_OBJ':all_sale_obj}
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)


#purchase

def purchase_page_load(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    c = {}
    c.update(csrf(request))
    return render_to_response('purchase.html', c)

def purchase_add_page_load(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    all_sale_obj = PurchaseMemo.objects.all
    c = {'party':Supplier.objects.all(),'PRINT':'true','ALL_SALE_OBJ': all_sale_obj}
    c.update(csrf(request))
    return render_to_response('purchase_add.html', c)

def purchase_add_page_load_1(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    obj = Supplier.objects.filter(id=int(id)).get()

    all_sale_obj = PurchaseMemo.objects.all
    c = {'CUSTOMER':obj, 'PRINT':'true','ALL_SALE_OBJ': all_sale_obj}
    c.update(csrf(request))
    return render_to_response('purchase_add.html', c)

def purchase_add_process(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    id = request.POST.get('Memo_no','')


    if request.POST.get('Print'):
        return HttpResponse('print'+request.POST.get('Select_memo',''))

    elif request.POST.get('New'):
        return HttpResponseRedirect("/purchase/purchase_add/")

    elif id=='' and not request.POST.get('New') :
        c_id , c_name = request.POST.get('Select_party','').split('-')
        customer= Supplier.objects.filter(id=int(c_id)).get()
        d,m,y= request.POST.get('Date','//').split('/')

        valid_datetime = y+'-'+m+'-'+d

        #try:
         #   valid_datetime = datetime.strptime(request.POST['Date'], '%d/%m/%Y')
        #except ValueError:
         #   print('error')

        obj= PurchaseMemo(party= customer, date= valid_datetime )
        obj.save()

        item = Item.objects.all

        c = {'SALE_OBJ': obj, 'ALLITEM':item,  }
        c.update(csrf(request))
        return render_to_response('purchase_add.html', c)



    elif request.POST.get('Add'):
        objMemo = PurchaseMemo.objects.filter(id=int(id)).get()

        item_id,item_name, item_size = request.POST.get('Select_item', '').split('-')
        selected_item = Item.objects.filter(id=int(item_id)).get()

        quantity = request.POST.get('Unit','')
        free = request.POST.get('Free','')



        objPurchaseItem = PurchaseItem(quantity=quantity,free=free,item=selected_item)
        objPurchaseItem.save()
        objMemo.purchase_item.filter(item =objPurchaseItem.item ).delete()
        objMemo.purchase_item.add(objPurchaseItem)

        objMemo.save()
        total = objMemo.get_total()


        item = Item.objects.all
        c = {'SALE_OBJ': objMemo, 'ALLITEM': item, 'TOTAL':total}
        c.update(csrf(request))
        return render_to_response('purchase_add.html', c)


    elif request.POST.get('Done'):
        objMemo = PurchaseMemo.objects.filter(id=int(id)).get()
        objMemo.paid = request.POST.get('Paid')
        objMemo.discount = request.POST.get('Discount')
        objMemo.save()


        return HttpResponseRedirect("/purchase/purchase_add/")





    else :

        objMemo = PurchaseMemo.objects.filter(id=int(id)).get()
        item_name, item_size = request.POST.get('Select_item', '').split('-')
        item = Item.objects.filter(name=item_name, size=item_size).get()

        total = objMemo.get_total()

        all_item = Item.objects.all


        c = {'SALE_OBJ': objMemo,'CURRENT_ITEM':item, 'TOTAL':total,'ALLITEM': all_item }
        c.update(csrf(request))
        return render_to_response('purchase_add.html', c)


def purchase_edit_delete(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')


    if request.POST.get('Delete'):
        id = request.POST.get('Select_memo', '')
        memo_obj = PurchaseMemo.objects.get(id=int(id))
        all_sale_obj = PurchaseMemo.objects.all

        gt = memo_obj.get_total() - memo_obj.discount
        due = gt - memo_obj.paid

        c = {'SALE_OBJ': memo_obj, 'ALL_SALE_OBJ': all_sale_obj, 'DELETE': 'true', 'TOTAL': memo_obj.get_total(),
             'GT': gt, 'DUE': due}
        c.update(csrf(request))
        return render_to_response('purchase_edit_delete.html', c)


    elif request.POST.get('Delete_confirm'):
        id = request.POST.get('Memo_no', '')
        PurchaseMemo.objects.filter(id=int(id)).delete()

        all_sale_obj = PurchaseMemo.objects.all
        c = {'ALL_SALE_OBJ': all_sale_obj}
        c.update(csrf(request))
        return render_to_response('purchase_edit_delete.html', c)

    elif request.POST.get('Print'):
        id = request.POST.get('Select_memo', '')
        memo_obj = PurchaseMemo.objects.get(id=int(id))
        all_sale_obj = PurchaseMemo.objects.all

        gt = memo_obj.get_total() - memo_obj.discount
        due = gt - memo_obj.paid

        c = {'SALE_OBJ': memo_obj, 'ALL_SALE_OBJ': all_sale_obj, 'PRINT': 'true', 'TOTAL': memo_obj.get_total(),
             'GT': gt, 'DUE': due}
        c.update(csrf(request))
        return render_to_response('purchase_edit_delete.html', c)
    elif request.POST.get('Print_confirm'):
        return HttpResponseRedirect("/purchase/purchase_edit_delete/")

    elif request.POST.get('Edit'):
        id = request.POST.get('Select_memo', '')
        memo_obj = PurchaseMemo.objects.get(id=int(id))
        all_sale_obj = PurchaseMemo.objects.all

        gt = memo_obj.get_total() - memo_obj.discount
        due = gt - memo_obj.paid

        customer = Supplier.objects.all()
        item = Item.objects.all()
        c = {'ITEM': item, 'SALE_OBJ': memo_obj, 'ALL_SALE_OBJ': all_sale_obj, 'CUSTOMER': customer, 'EDIT': 'true',
             'TOTAL': memo_obj.get_total(), 'GT': gt, 'DUE': due}
        c.update(csrf(request))
        return render_to_response('purchase_edit_delete.html', c)

    elif request.POST.get('Save_head'):

        id = request.POST.get('Memo_no', '')
        memo_obj = PurchaseMemo.objects.get(id=int(id))

        customer_id, customer_name, customer_mobile_no = request.POST.get('Party', '').split('-')

        memo_obj.party = Supplier.objects.get(id=int(customer_id))
        memo_obj.save()

        all_sale_obj = PurchaseMemo.objects.all

        gt = memo_obj.get_total() - memo_obj.discount
        due = gt - memo_obj.paid

        customer = Supplier.objects.all()
        item = Item.objects.all()
        c = {'ITEM': item, 'SALE_OBJ': memo_obj, 'ALL_SALE_OBJ': all_sale_obj, 'CUSTOMER': customer, 'EDIT': 'true',
             'TOTAL': memo_obj.get_total(), 'GT': gt, 'DUE': due}
        c.update(csrf(request))
        return render_to_response('purchase_edit_delete.html', c)


    elif request.POST.get('Delete_item'):
        id = request.POST.get('Memo_no', '')
        objMemo = PurchaseMemo.objects.filter(id=int(id)).get()

        item_id, item_name, item_size = request.POST.get('Select_item', '').split('-')
        selected_item = Item.objects.filter(id=int(item_id)).get()

        quantity = request.POST.get('Unit', '')
        free = request.POST.get('Free', '')

        objPurchaseItem = PurchaseItem(quantity=quantity, free=free, item=selected_item)

        objMemo.sale_item.filter(item=objPurchaseItem.item).delete()

        objMemo.save()

        customer = Supplier.objects.all()
        item = Item.objects.all()
        all_sale_obj = PurchaseMemo.objects.all
        gt = objMemo.get_total() - objMemo.discount
        due = gt - objMemo.paid

        c = {
            'NEW': 'true',
            'ITEM': item,
            'SALE_OBJ': objMemo,
            'ALL_SALE_OBJ': all_sale_obj,
            'CUSTOMER': customer,
            'EDIT': 'true',
            'TOTAL': objMemo.get_total(),
            'GT': gt,
            'DUE': due
        }
        c.update(csrf(request))
        return render_to_response('purchase_edit_delete.html', c)

    elif request.POST.get('Save_item'):
        id = request.POST.get('Memo_no', '')
        objMemo = PurchaseMemo.objects.filter(id=int(id)).get()

        item_id, item_name, item_size = request.POST.get('Select_item', '').split('-')
        selected_item = Item.objects.filter(id=int(item_id)).get()

        quantity = request.POST.get('Unit', '')
        free = request.POST.get('Free', '')

        objPurchaseItem = PurchaseItem(quantity=int(quantity), free=int(free), item=selected_item)
        objPurchaseItem.save()

        objMemo.sale_item.filter(item=objPurchaseItem.item).delete()
        objMemo.sale_item.add(objPurchaseItem)

        objMemo.save()

        customer = Supplier.objects.all()
        item = Item.objects.all()
        all_sale_obj = PurchaseMemo.objects.all
        gt = objMemo.get_total() - objMemo.discount
        due = gt - objMemo.paid

        c = {
            'NEW': 'true',
            'ITEM': item,
            'SALE_OBJ': objMemo,
            'ALL_SALE_OBJ': all_sale_obj,
            'CUSTOMER': customer,
            'EDIT': 'true',
            'TOTAL': objMemo.get_total(),
            'GT': gt,
            'DUE': due
        }
        c.update(csrf(request))
        return render_to_response('purchase_edit_delete.html', c)

    elif request.POST.get('Save_all'):
        id = request.POST.get('Memo_no', '')

        objMemo = PurchaseMemo.objects.filter(id=int(id)).get()

        discount = request.POST.get('Discount', '')
        paid = request.POST.get('Paid', '')

        objMemo.discount = discount
        objMemo.paid = paid

        objMemo.save()

        all_sale_obj = PurchaseMemo.objects.all

        c = {'ALL_SALE_OBJ': all_sale_obj}
        c.update(csrf(request))
        return render_to_response('sale_edit_delete.html', c)





    else:
        if request.POST.get('Select_item'):
            item_id, item_name, item_size = request.POST.get('Select_item', '').split('-')

            id = request.POST.get('Memo_no', '')

            objMemo = PurchaseMemo.objects.filter(id=int(id)).get()

            item_id, item_name, item_size = request.POST.get('Select_item', '').split('-')

            if item_id == '':
                all_sale_obj = PurchaseMemo.objects.all
                c = {'ALL_SALE_OBJ': all_sale_obj}
                c.update(csrf(request))
                return render_to_response('purchase_edit_delete.html', c)
            else:
                s_item = Item.objects.get(id=int(item_id))
                selected_sale_item = objMemo.purchase_item.filter(item=s_item)
                if selected_sale_item:
                    print('yes')
                    selected_sale_item = objMemo.purchase_item.filter(item=s_item).get()
                    current_item = s_item

                    id = request.POST.get('Memo_no', '')
                    memo_obj = PurchaseMemo.objects.get(id=int(id))
                    all_sale_obj = PurchaseMemo.objects.all

                    gt = memo_obj.get_total() - memo_obj.discount
                    due = gt - memo_obj.paid

                    customer = Supplier.objects.all()
                    item = Item.objects.all()

                    c = {'CURRENT_ITEM': s_item, 'OLD': 'true', 'SALE_ITEM': selected_sale_item, 'ITEM': item,
                         'SALE_OBJ': memo_obj, 'ALL_SALE_OBJ': all_sale_obj, 'CUSTOMER': customer,
                         'EDIT': 'true', 'TOTAL': memo_obj.get_total(), 'GT': gt, 'DUE': due}
                    c.update(csrf(request))
                    return render_to_response('purchase_edit_delete.html', c)




                else:
                    print('no')

                    current_item = s_item

                    id = request.POST.get('Memo_no', '')
                    memo_obj = PurchaseMemo.objects.get(id=int(id))
                    all_sale_obj = PurchaseMemo.objects.all

                    gt = memo_obj.get_total() - memo_obj.discount
                    due = gt - memo_obj.paid

                    customer = Supplier.objects.all()
                    item = Item.objects.all()

                    c = {'CURRENT_ITEM': s_item,
                         'NEW': 'true',
                         'ITEM': item,
                         'SALE_OBJ': memo_obj,
                         'ALL_SALE_OBJ': all_sale_obj,
                         'CUSTOMER': customer,
                         'EDIT': 'true',
                         'TOTAL': memo_obj.get_total(),
                         'GT': gt,
                         'DUE': due
                         }
                    c.update(csrf(request))
                    return render_to_response('purchase_edit_delete.html', c)

        all_sale_obj = PurchaseMemo.objects.all
        c = {'ALL_SALE_OBJ': all_sale_obj}
        c.update(csrf(request))
        return render_to_response('purchase_edit_delete.html', c)










