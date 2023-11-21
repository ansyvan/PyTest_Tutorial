import sqlite3


class Database():

# This part is an individual task to practice testing skills after the QA Automation Course

    def select_product_qnt_by_name(self, name):
        query = f"SELECT quantity FROM products WHERE name = {name}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_product_with_min_quantity(self):
        query = "SELECT name, quantity \
                   FROM products \
                  WHERE quantity = (SELECT MIN(quantity) FROM products)"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_product_with_max_quantity(self):
        query = "SELECT name, quantity \
                   FROM products \
                  WHERE quantity = (SELECT MAX(quantity) FROM products)"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_order(self, order_id, customer_id, product_id, order_date):
        query = f"INSERT INTO orders (id, customer_id, product_id, order_date) \
            VALUES ({order_id}, {customer_id}, {product_id}, '{order_date}')"
        self.cursor.execute(query)
        self.connection.commit()
        record = self.cursor.fetchall()
        return record
    
    def get_all_orders(self):
        query = "SELECT id, customer_id, product_id, order_date FROM orders"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_all_products(self):
        query = "SELECT id, name, description, quantity FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def delete_order_by_id(self, order_id):
        query = f"DELETE FROM orders WHERE id = {order_id}"
        self.cursor.execute(query)
        self.connection.commit()

# This part is from QA Automation Course

    def __init__(self):
        self.connection = sqlite3.connect('/Users/andrianasyvanych/Documents/GitHub/pytest_tutorial' + '/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Qery = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Qery)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, products.description, orders.order_date \
                   FROM orders \
                   JOIN customers ON orders.customer_id = customers.id \
                   JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
