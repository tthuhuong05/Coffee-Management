# app.py

from flask import Flask, render_template, request, redirect
from controller.menu_controller import MenuController

app = Flask(__name__)

@app.route("/")
def show_menu():
    controller = MenuController()
    return controller.request_menu()


# as BACK SYSTEM
@app.route("/admin/menu/list")
def show_menu_list():
    controller = MenuController()
    return controller.list_menu()

@app.route("/admin/menu/create")
def create_menu():
    controller = MenuController()
    return controller.create_menu()

@app.route("/admin/menu/store", methods=['POST'])
def store_menu():
    controller = MenuController()
    return controller.store_menu()

@app.route("/menu/edit/<int:item_id>", methods=['GET', 'POST'])
def edit_menu(item_id):
    controller = MenuController()
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        controller.update_menu(item_id, name, price, description)  # Cập nhật menu
        return redirect('/menu')  # Sau khi cập nhật, chuyển hướng về trang menu
    return controller.edit_menu(item_id)  # Nếu là GET, hiển thị form chỉnh sửa


@app.route("/menu/delete/<int:item_id>", methods=['GET'])
def delete_menu(item_id):
    controller = MenuController()
    return controller.delete_menu(item_id)

@app.route("/buy/<int:item_id>", methods=['GET', 'POST'])
def buy_now(item_id):
    if request.method == 'POST':
        # Lấy thông tin từ form
        name = request.form.get("name")
        quantity = int(request.form.get("quantity"))
        price = float(request.form.get("price"))
        
        # Tính tổng giá tiền
        total_price = quantity * price
        
        # Lưu thông tin hoặc xử lý đặt hàng ở đây (ví dụ: lưu vào cơ sở dữ liệu hoặc gửi email)
        
        # Trả về kết quả
        return render_template("order_confirmation.html", name=name, quantity=quantity, total_price=total_price)

    else:
        # Lấy thông tin món ăn từ cơ sở dữ liệu (dùng ID)
        controller = MenuController()
        menu_item = controller.model.get_menu_item_by_id(item_id)
        
        # Hiển thị form mua hàng
        return render_template("buy_now.html", item=menu_item)

if __name__ == "__main__":
    app.run(debug=True)
